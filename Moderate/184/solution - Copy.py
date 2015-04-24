import sys

def find_index(indices, chars, char):
    for i, c in enumerate(chars):
        if i not in indices and char == c:
            return i


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        line = line[2:-2]
        line2 = ''.join(sorted(cols[0]))

        # Work out transformation vector T
        T = []
        dollar_index = None
        for i, char in enumerate(line):
            T.append(find_index(T, line2, char))
            if char == '$':
                dollar_index = i
                
        indices = []
        
        for col_index in range(1, len(line)-1):
            char_list = [None for _ in range(len(T))]
            read_col = cols[col_index]
            
            for i, index in enumerate(T):
                char_list[index] = read_col[i]

            cols.append(''.join(char_list))
        
        # Move last column to end of list
        cols.append(cols.pop(0))
            
        print(''.join([col[dollar_index] for col in cols]))