import sys

# Create grid
adjacencies = ['l', 'ul', 'u', 'ur', 'r', 'dr', 'd', 'dl']
grid = []

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        row = [char for char in line]
        
        grid.append(row)

side_length = len(grid)


def print_grid(grid):
    out = []
    for row in grid:
        out.append(''.join(row))

    print('\n'.join(out))


# Cope with edges in here
def get_cell(i,j):
    if i == -1 or i == side_length or j == -1 or j == side_length:
        return False

    c = grid[i][j]
    
    return True if c == '*' else False


def calculate_char(i,j):
    this_cell_lives = get_cell(i,j)
    live_cells = []

    for a in adjacencies:
        if a == 'l':
            live_cells.append(get_cell(i-1,j))
        if a == 'ul':
            live_cells.append(get_cell(i-1,j-1))
        if a == 'u':
            live_cells.append(get_cell(i,j-1))
        if a == 'ur':
            live_cells.append(get_cell(i+1,j-1))
        if a == 'r':
            live_cells.append(get_cell(i+1,j))
        if a == 'dr':
            live_cells.append(get_cell(i+1,j+1))
        if a == 'd':
            live_cells.append(get_cell(i,j+1))
        if a == 'dl':
            live_cells.append(get_cell(i-1,j+1))
    
    live_count = 0
    for live_cell in live_cells:
        if live_cell:
            live_count += 1
    
    if this_cell_lives and live_count < 2:
        return '.'
    
    if this_cell_lives and 2 <= live_count <= 3:
        return '*'
    
    if this_cell_lives and live_count > 3:
        return '.'
        
    if not this_cell_lives and live_count == 3:
        return '.'
    
    return '.'


def update_grid(grid):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            grid[i][j] = calculate_char(i, j)

print_grid(grid)
print()
print('==========')
print()

for it in range(10):
    update_grid(grid)
    print_grid(grid)
    print()
    print('----------')
    print()

print_grid(grid)
