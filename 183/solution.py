import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue

    rows = line.split(',')
    min_dotcount = -1
    
    for row in rows:
        row = row[0:row.find('Y')+1]
        count = row.count('.')
        if min_dotcount is -1 or count < min_dotcount:
            min_dotcount = count
    
    print(str(min_dotcount))

lines.close()