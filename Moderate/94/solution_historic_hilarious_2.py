import sys

def process_string(s):
    ops = '+-*/^'
    tree = []
    subtree = []
    state = 'START'
            
    for i, char in enumerate(s):
        if char == ' ':
            continue
            
        #print("State=" + state + ", char=" + char)
        if state == 'START':
            if char == '(':
                state = 'BRACKETS'
                #subtree.append('(')
                subtree.append('')
            elif char.isdigit():
                state = 'DIGIT'
                tree.append(char)
            elif char == '-':
                state = 'NEGATED'
            elif char in ops:
                tree.append(char)
                state = 'OP'
        
        elif state == 'DIGIT':
            if char.isdigit() or char == '.':
                tree[len(tree)-1] += char
            elif char in ops:
                if char == '^':
                    state = 'POW'
                    tree[len(tree)-1] = [tree[len(tree)-1], char, '']
                else:
                    state = 'OP'
                    tree.append(char)
        
        elif state =='OP':
            if char.isdigit():
                state = 'DIGIT'
                tree.append(char)
            elif char == '-':
                state = 'NEGATED'
            elif char in ops:
                tree.append(char)
        
        elif state == 'POW' or state == 'MD':
            if char.isdigit() or char == '.':
                tree[len(tree)-1][2] += char
            elif char == '-':
                state = 'NEGATED'
            else:
                state = 'DIGIT'
                tree.append(char)
        
        elif state == 'NEGATED':
            if char.isdigit():
                state = 'DIGIT'
                tree.append('-'+char)
                
        elif state == 'BRACKETS':
            if char == ')':
                #subtree.append(')')
                print("Subprocessing " + str(subtree[0]))
                subtree[0] = process_string(subtree[0])
                tree.append(subtree)
                state = 'START'
            else:
                subtree[0] += char
    
    return tree


def prioritise_md(tree):
    out = []
    state = 'START'
    for el in tree:
        if state == 'START':
            if type(el) is list:
                out.append(prioritise_md(el))
            elif el in '*/':
                out[len(out)-1] = [out[len(out)-1], el, '']
                state = 'MD'
            else:
                out.append(el)
        elif state == 'MD':
            out[len(out)-1][2] = el
            state = 'START'

    return tree

def process_tree(tree):
    total = 0
    
    state = 'START'
    op = ''
    
    for el in tree:
        if state == 'START':
            if type(el) is list:
                state = 'DIGIT'
                total = process_tree(el)
            else:
                state = 'DIGIT'
                total = float(el)
                
        elif state == 'DIGIT':
            state = 'OP'
            op = el
        
        elif state == 'OP':
            state = 'DIGIT'
            temp = 0
            
            if type(el) is list:
                temp = process_tree(el)
            else:
                print(str(el))
                temp = float(el)
                
            if op == '+':
                total += temp
            elif op == '-':
                total -= temp
            elif op == '*':
                total *= temp
            elif op == '/':
                total /= temp
            elif op == '^':
                total = total ** temp
                
    return total
        

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        print("Processing " + str(line))
        tree = process_string(line)
        
        print("Tree: " + str(tree))
        
        tree = prioritise_md(tree)
        print("MD: " + str(tree))
        
        print(str(process_tree(tree)))
            