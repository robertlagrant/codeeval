import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        nums = set()
        
        for x in line.split(';')[1].split(','):
            if x not in nums:
                nums.add(x)
            else:
                print(x)
                break