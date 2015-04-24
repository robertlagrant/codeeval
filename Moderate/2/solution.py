import sys

limit = 0; longest_lines = []

with open(sys.argv[1], 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line == '':
            continue
            
        # Read the limit from the first line
        if i is 0:
            limit = int(line)
        else:
            longest_lines.append(line)

for l in sorted(longest_lines, key=len, reverse=True)[:limit]:
    print(l)