import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        
        diffs = set()
        needed_diffs = None
        previous_num = None
        
        for num in map(int, line.split(' ')):
            if needed_diffs is None:
                needed_diffs = set(range(1, num))
            else:
                if previous_num is None:
                    previous_num = num
                else:
                    diffs.add(abs(num-previous_num))
                    previous_num = num
        
        if len(diffs ^ needed_diffs) == 0:
            print("Jolly")
        else:
            print("Not jolly")