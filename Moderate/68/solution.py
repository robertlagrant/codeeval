import sys

pairs = {'(': ')', '{': '}', '[': ']'}

def process_line(line):
    stack = []
    for char in line:
        if char in pairs.keys():
            stack.append(pairs[char])
        else:
            if len(stack) == 0 or char != stack.pop():
                return False
    
    if len(stack) > 0:
        return False
        
    return True


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        #print(line)
        print(process_line(line))