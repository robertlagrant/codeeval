import sys
from string import ascii_lowercase

alphabets = set(ascii_lowercase)

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        print(''.join(sorted(alphabets - set(line.lower()))) or 'NULL')