import sys
from math import sqrt

def row_in_grid(required, grid):
    for row in grid:
        if set(row) != required:
            return False
    return True

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        params = line.split(';')
        size = int(params[0])
        required = set(range(1, size+1))
        grid = list((zip(*[iter(map(int, params[1].split(',')))]*size)))
        new_grid = []
        for x in range(size):
            new_row = []
            for y in range(size):
                new_row.append(grid[y][x])
            new_grid.append(new_row)

        valid = False

        if row_in_grid(required, grid):
            if row_in_grid(required, new_grid):
                
                # Number of squares to check is equal to size
                x,y,square_side = 0,0,int(sqrt(size))
                
                squares = []
                for zone in range(size):
                    square = []
                    for y_side in range(y,y+square_side+1):
                        for x_side in range(x,x+square_side+1):
                            square.append(grid[y_side][x_side])
                        squares.append(square)
                
                if row_in_grid(required, squares):
                    valid = True
                    
        print(valid)