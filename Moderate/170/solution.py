import sys
from math import floor

def find_index(l):
    if l % 2 == 0:
        return int(l/2)
    else:
        return int(floor(l/2))
        

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        params = line.split()
        
        r = range(int(params[0])+1)

        for instruction in params[1:]:
            guessIndex = find_index(len(r))
            
            if instruction == 'Lower':
                r = r[0:guessIndex]
                
            if instruction == 'Higher':
                r = r[guessIndex+1:]
            
            if instruction == 'Yay!':
                print(r[guessIndex])