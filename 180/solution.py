import sys

# Make it easier to think about
xs = { 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7 }
ys = { '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7 }

def key_from_value(dictionary, value):
    for k, v in dictionary.items():
        if v is value:
            return k

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
    
    x = xs[line[0]]
    y = ys[line[1]]
    
    possible_moves = [
        (x-2, y+1),
        (x-2, y-1),
        (x+2, y+1),
        (x+2, y-1),
        (x+1, y-2),
        (x-1, y-2),
        (x+1, y+2),
        (x-1, y+2)
    ]
    
    moves = list()
    for x_coord, y_coord in possible_moves:
      
        # Remove illegal moves
        if x_coord >= xs['a'] and x_coord <= xs['h'] and y_coord >= ys['1'] and y_coord <= ys['8']:
            moves.append(key_from_value(xs, x_coord) + key_from_value(ys, y_coord))

    print(' '.join(sorted(moves))) 
     
lines.close()