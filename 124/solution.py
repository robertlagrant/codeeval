import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
        
    # Cut out that final pesky semicolon
    line = line[:-1]
  
    pairs = line.split('; ')
    
    distance_so_far = 0
    distances = sorted((int(pair.split(',')[1].strip()) for pair in pairs))
    
    out = list()
    current_point = 0
    for distance in distances:
        out.append(str(distance-current_point))
        current_point = distance
    
    print(','.join(out))

lines.close()
