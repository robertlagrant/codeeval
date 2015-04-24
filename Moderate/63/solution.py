import sys
from collections import Counter

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        low,high = map(int, line.split(','))
        
        primes = set()
        
        for x in range(2, high+1):
            isprime = True
        
            for prime in primes:
                if isprime is False:
                    continue
                
                if x % prime == 0:
                    isprime = False
            
            if isprime:
                primes.add(x)
                    
        print(len([prime for prime in primes if prime >= low and prime <= high]))