import sys

# Set up the grid with zeroes
grid = list()
for x in range(256):
    row = list()
    for cell in range(256):
        row.append(0)
    grid.append(row)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if test == '':
        continue

    params = test.split()
    command = params[0]
    index = int(params[1])

    if command == 'SetCol':
        value = int(params[2])
        
        for row in grid:
            row[index] = value
    
    if command == 'SetRow':
        value = int(params[2])
        
        grid[index] = [value for cell in range(256)]
    
    if command == 'QueryCol':
        print(str(sum([row[index] for row in grid])))
        
    if command == 'QueryRow':
        print(str(sum(grid[index])))
    
test_cases.close()