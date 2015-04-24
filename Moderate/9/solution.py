import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        stack = list(line.split())
        out = []
        for x in range(len(stack)):
            item = stack.pop()
           
            if x % 2 == 0:
                out.append(item)
        
        print(' '.join(out))