import sys
from collections import Counter

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        print(str(len([char for char in str(bin(int(line)))[2:] if char == '1'])))