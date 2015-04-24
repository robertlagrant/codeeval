import sys
from collections import Counter

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        counts = Counter(line)
        
        for char in line:
            if counts[char] == 1:
                print(char)
                break