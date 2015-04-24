import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if line == '':
            continue
  
        params = line.split(', ')
    
        for char in params[1]:
            params[0] = params[0].replace(char, '')
    
        print(params[0])