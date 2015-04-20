import sys
from json import loads

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
    
    total = 0
    
    data = loads(line)
    for item in data['menu']['items']:
        if item is not None and 'label' in item:
            total += int(item['id'])
    
    print(str(total))

lines.close()