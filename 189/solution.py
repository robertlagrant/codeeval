import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
    
    params = list(map(int, line.split()[1:]))
    lowest_total_distance = -1
    
    for x in range(0, max(params)):
        total_distances = 0
        for param in params:
            total_distances += abs(param - x)
        
        if lowest_total_distance is -1 or lowest_total_distance > total_distances:
            lowest_total_distance = total_distances

    print(str(lowest_total_distance))
    
lines.close()