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
        line2 = ''.join(sorted([char for char in line]))

        # Work out transformation vector T
        T = []
        dollar_index = None
        for i, char in enumerate(line):
            T.append(find_index(T, line2, char))
            if char == '$':
                dollar_index = i
                
        indices = [[x for x in range(len(line)-1)],T]
        
        for col_index in range(1, len(line)+1):
            index_list = [None for _ in range(len(T))]
            read_col = indices[col_index]
            
            for i, index in enumerate(T):
                index_list[index] = read_col[i]

            indices.append(index_list)
        
        # Move last column to end of list
        indices.append(indices.pop(0))
            
        print(''.join([line[index[dollar_index]] for index in indices])[2:])