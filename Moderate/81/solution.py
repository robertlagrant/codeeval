import sys
from itertools import combinations

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        print(sum([1 for combo in combinations(map(int, line.split(',')), 4) if sum(combo) == 0]))