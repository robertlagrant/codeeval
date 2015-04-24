import sys

ops = '+*/'

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        ops_list = []; op_index = -1; current = None
        
        for char in line.split():
            if char in ops:
                ops_list.append(char)
                op_index += 1
            else:
                num = int(char)
                if current == None:
                    current = num
                else:
                    op = ops_list[op_index]
                    if op == '+':
                        current += num
                    elif op == '*':
                        current *= num
                    elif op == '/':
                        current /= num
                    
                    op_index -= 1

        print(str(int(current)))