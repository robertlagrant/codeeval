import sys


def find_linked_pair(current, i, pairs):
    for pair in pairs:
        if pair[i] == current[i]:
            return pair
            
    return None


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        line = line[1:-1]
        params = line.split('), (')
        #print('[' + '], ['.join(params) + ']')
        pairs = set()
        first, fourth = None, None
        
        for param in params:
            a,b = map(int, param.split(','))
            if first is None:
                first = (a,b)
            else:
                pairs.add((a,b))
        
        # Detect four identical coordinates
        if set(first) == pairs:
            print('true')
        else:
        
            second = find_linked_pair(first, 0, pairs)
        
            if second:
                pairs.remove(second)
                third = find_linked_pair(second, 1, pairs)
            
                if third:  
                    pairs.remove(third)
                    fourth = find_linked_pair(third, 0, pairs)
                
                    if fourth:
                        pairs.remove(fourth)
        
            if len(pairs) == 0 and fourth and fourth[1] == first[1] and abs(first[0]-third[0]) == abs(first[1]-second[1]):
                print('true')
            else:
                print('false')