import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        print(' '.join([word[-1]+word[1:-1]+word[0] for word in line.split()]))