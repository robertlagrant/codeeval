import sys

def distance(c1, c2):
    xdist = abs(c1[0] - c2[0])
    ydist = abs(c1[1] - c2[1])
    
    # Just keep it as squared dists, as this is just for comparisons
    return xdist ** 2 + ydist ** 2
    

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        line = line[1:-1]
        params = line.split('), (')
        pairs = []
        
        for param in params:
            a,b = map(int, param.split(','))
            pairs.append((a,b))
            
        if len(pairs) != len(set(pairs)):
            print('false')
        else:
        
            a,b,c,d = pairs[0],None,None,None
            dists_from_a = []
            unique_dists_from_a = set()
            for point in pairs[1:]:
                dist = distance(a, point)
                dists_from_a.append((point,dist))
                unique_dists_from_a.add(dist)
        
            # Drop out unless 2 dists are equal and one is different
            if len(unique_dists_from_a) != 2:
                print('false')
            else:
                # Find point c, opposite point a in a square, and assign b and d as the other points
                for k,v in dists_from_a:
                    if v == max(unique_dists_from_a):
                        c = k
                    elif b is None:
                        b = k
                    else:
                        d = k

                ab = distance(a,b)
                ac = distance(a,c)
                ad = distance(a,d)
                bd = distance(b,d)
            
                if ac == bd and ab == ad:
                    print('true')
                else:
                    print('false')