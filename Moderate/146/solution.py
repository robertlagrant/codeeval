import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        primes = set()
        
        for x in range(2, int(line)):
            if all(x % p != 0 for p in primes):
                primes.add(x)
        
        print(','.join(map(str, sorted(primes))))