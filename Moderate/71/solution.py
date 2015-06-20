import sys
from itertools import zip_longest

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        params = line.split(';')
        size = int(params[1])
        groups = list((zip_longest(*[iter(map(int, params[0].split(',')))]*size)))
        
        out = []
        for group in groups:
            group_out = []
            for item in group:
                if item:
                    group_out.append(str(item))
            if len(group_out) == size:
                out.extend(list(reversed(group_out)))
            else:
                out.extend(list(group_out))
        
        print(','.join(out))