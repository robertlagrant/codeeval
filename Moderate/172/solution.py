import sys
from collections import Counter

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        line = line.replace(' ', '')
        
        total = 0
        
        for i, char in enumerate(reversed(line)):
            if (i + 1) % 2 == 0:
                num = int(char)*2
                if num > 9:
                    for c in str(num):
                        total += int(c)
                else:
                    total += num
            else:
                total += int(char)
        
        if total % 10 == 0:
            print('1')
        else:
            print('0')