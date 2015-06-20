import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        params = line.split()
        
        print(''.join([text.upper() if mask == '1' else text for text, mask in zip(params[0], params[1])]))