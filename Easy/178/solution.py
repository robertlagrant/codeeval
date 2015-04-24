import sys
from math import sqrt
from itertools import chain

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
    
    params = line.split()
    
    side_length = int(sqrt(len(params)))
    
    square = list()
    for x in range(0, len(params), side_length):
        square.append([params[x+y] for y in range(side_length)])
    
    
    rotated = list()
    for x in range(side_length):
        rotated.append([square[y][x] for y in range(side_length-1, -1, -1)])
 
    out = list()
    for row in rotated:
        for item in row:
            out.append(item)
    
    print(' '.join(out))
     
lines.close()