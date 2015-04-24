import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        params = list(reversed(line.split()))
        index = int(params[0])
        
        if index < len(params):
            print(params[index])