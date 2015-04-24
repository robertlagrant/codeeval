import sys

def return_combos(s):
    if len(s) == 1:
        return s
    
    out = []
    
    for i, char in enumerate(s):
        start_with = char; str_out = ''
        
        indexes = list(range(len(s)))
        indexes.remove(i)
        remainder = ''.join([s[j] for j in indexes])
        
        for subcombo in return_combos(remainder):
            out.append(char + subcombo)
    
    return out
        

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        print(','.join(sorted(return_combos(line))))