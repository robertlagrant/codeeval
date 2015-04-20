import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
    
    params = list(map(int, line.split()))
    x_now = params[0]
    y_now = params[1]
    x_dest = params[2]
    y_dest = params[3]
    
    out = ''
    
    if x_now == x_dest and y_now == y_dest:
        out = 'here'
    else:
        if y_now < y_dest:
            out += 'N'
        elif y_now > y_dest:
            out += 'S'
        if x_now < x_dest:
            out += 'E'
        elif x_now > x_dest:
            out += 'W'
    
    print(out)    
    
lines.close()