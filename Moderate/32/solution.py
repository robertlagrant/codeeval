import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        params = line.split(',')
        if params[0].endswith(params[1]):
            print('1')
        else:
            print('0')