import sys
from copy import deepcopy

rows = list()
course = list()

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue

    gate_location = line.find('_')
    checkpoint_location = line.find('C')
    
    #if checkpoint_location is -1:
    #    rows.append((gate_location,))
    #else:
    #    rows.append((gate_location, checkpoint_location))
    rows.append((gate_location, checkpoint_location))
    course.append(line)

lines.close()

def find_route(rows, route):
    if len(rows) == 0:
        return rows, route, True
    
    gate, checkpoint = rows[0]
    if len(route) > 0:
        last_route_index = route[-1]
    else:
        last_route_index = -1
    
    if checkpoint is -1:
        if last_route_index is -1 or abs(last_route_index-gate) < 2:
            route.append(gate)
            return find_route(rows[1:], route)
        else:
            return rows, route, False
    else:
        trial_route = deepcopy(route)
        checkpoint_worked = True
        
        if last_route_index is -1 or abs(last_route_index-checkpoint) < 2:
            trial_route.append(checkpoint)
            _, _, result = find_route(rows[1:], trial_route)
        
            if result:
                route.append(checkpoint)
            else:
                checkpoint_worked = False
        else:
            checkpoint_worked = False
            
        if not checkpoint_worked:
            if abs(last_route_index-gate) < 2:
                route.append(gate)
            else:
                return rows, route, False
        
        return find_route(rows[1:], route)


_, route, _ = find_route(rows, list())

for count, pair in enumerate(zip(course, route)):
    out = list(pair[0])
    index = pair[1]
    
    # Correct routing!
    #if count is len(course)-1:
    #    out[index] = '|'
    #else:
    #    next_route = route[count+1]
    #    
    #    if index < next_route:
    #       out[index] = '\\'
    #    elif index > next_route:
    #        out[index] = '/'
    #    else:
    #        out[index] = '|'
    
    # Pass routing
    if count is 0:
        out[index] = '|'
    else:
        last_route = route[count-1]

        if index < last_route:
            out[index] = '/'
        elif index > last_route:
            out[index] = '\\'
        else:
            out[index] = '|'
    
    print(''.join(out))    