import sys
from itertools import combinations

def create_sequential_indices(length):
    possible_lengths = range(1, length+1)
    
    out = []
    for possible_length in possible_lengths:
        start = 0
        end = possible_length
        
        while end <= length:
            out.append(range(start, end))
            start += 1
            end += 1
    
    return out


def sum_by_indices(indices, nums, current):
    total = sum([nums[i] for i in indices])
    
    return total if total > current else current


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        nums = list(map(int, line.split(',')))
        length = len(nums)
        possible_indices = create_sequential_indices(length)
        #print(str(possible_indices))
        current = float('-inf')
        for p_i in possible_indices:
            current = sum_by_indices(p_i, nums, current)
        
        #print(str(current) + ": " + line)
        print(str(current))