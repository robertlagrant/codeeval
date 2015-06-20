import sys
from itertools import groupby

def sort_cols_by_index(cols, index):
    return sorted(cols, key=lambda col: col[index])


def detect_duplicates(cols, index):
    counts = {}
    for i, col in enumerate(cols):
        val = col[index]
        if not val in counts:
            counts[val] = [i]
        else:
            counts[val].append(i)

    # Filter out everything that isn't a duplicate
    return { k:v for k,v in counts.items() if len(v) > 1 }
    
    
def sort_with_duplicates(cols, index):
    if index == len(cols):
        return cols
        
    duplicates = detect_duplicates(cols, index)
    
    if duplicates:
        for _,sub_indices in duplicates.items():
            sub_cols = [cols[i] for i in sub_indices]
            sub_cols = sort_cols_by_index(sub_cols, index+1)
            sub_cols = sort_with_duplicates(sub_cols, index+1)
            temp_index = 0
            for i in sub_indices:
                cols[i] = sub_cols[temp_index]
                temp_index += 1
            
    return cols
    

def print_cols(cols, pre_message):
    print()
    print(pre_message)
    for c in cols:
        print(c)


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        # Get a list of lists of ints
        rows = [list(map(int, l.split())) for l in line.split(' | ')]
        
        # Get cols as well
        cols = []
        for i in range(len(rows)):
            col = []
            
            for row in rows:
                col.append(row[i])
            
            cols.append(col)
        
        # Starting index
        index = 0
        depth = len(cols[0])

        #print_cols(cols, "Initial cols")
        # Initial sort
        cols = sort_cols_by_index(cols, index)
        
        #print_cols(cols, "After initial sort")
        
        # All the subsorts
        cols = sort_with_duplicates(cols, 0)
        
        #print_cols(cols, "After subsorts")
        
        rows = []
        for i in range(len(cols[0])):
            row = []
            for col in cols:
                row.append(str(col[i]))
            rows.append(' '.join(row))
        
        print(' | '.join(rows))