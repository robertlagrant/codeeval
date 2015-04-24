import sys, re

def is_number(num):
    try:
        float(num)
        return True
    except (TypeError, ValueError):
        return False

def remove_trailing_numerics(floatstring):
    out = ''
    for s in reversed(floatstring):
        if s == '0' and len(out) == 0:
            continue
        elif s == '.' and len(out) == 0:
            continue
        else:
            out += s
    
    return out[::-1]

def sort_out_neg(stuff):
    # Fix negative vs subtraction
    ops = '+-*/^'
    out = []
    state = 'START'

    for i, s in enumerate(stuff):

        if state == 'START':
            if type(s) is str and ((s.startswith('-') and is_number(s[1:])) or is_number(s)):
                state = 'DIGIT'
                out.append(s)
            elif s == '-' and type(stuff[i+1]) is list:
                state = 'NEGATE'
            elif type(s) is str and s in ops:
                state = 'OPS'
                out.append(s)
            elif type(s) is list:
                state = 'DIGIT'
                out.append(s)
            else:
                out.append(s)
                    
        elif state == 'OPS':
            if s == '-':
                state = 'NEGATE'
            elif type(s) is str and s.startswith('-'):
                state = 'DIGIT'
                out.append(s)
            else:
                out.append(s)
                    
        elif state == 'DIGIT':
            if type(s) is str and is_number(s[1:]) and s.startswith('-'):
                out.append('-')
                out.append(s[1:])
            elif s in ops:
                out.append(s)
                state = 'OPS'
            else:
                out.append(s)
                
        elif state == 'NEGATE':
            if is_number(s):
                out.append('-'+s)
                state = 'DIGIT'
            elif type(s) is list:
                # Multiply list output by -1
                out.append(['-1', '*', s])
                
    return out
    

def prioritise_ops(stuff, op):
    out = []
    
    skip = False
    for i, el in enumerate(stuff):
        if skip:
            skip = False
            continue
            
        if type(el) is str and el in op:
            out[len(out)-1] = [out[len(out)-1], el, stuff[i+1]]
            skip = True
        elif type(el) is list:
            sublist = prioritise_ops(el, op)
            out.append(sublist)
        else:
            out.append(el)
    
    return out
            

def process_string(s):
    ops = '+-*/^'
    state = 'START'
    stuff = re.findall('(\(.*\)|\-?\d+\.?\d*|\+|\-|\*|\/|\^)',s)
    #print("Tokens: " + str(stuff))
    out = []
    
    for st in stuff:
        if type(st) is str and st.startswith('('):
            if is_number(st):
                out.append(st[1:len(st)-1])
            else:
                out.append(process_string(st[1:len(st)-1]))
        else:
            out.append(st)
    
    out = sort_out_neg(out)

    for s in out:
        if type(s) is str and s.startswith('('):
            if is_number(s):
                out.append(st[1:len(st)-1])
            else:
                process_string(s[1:len(s)-1])
    
    return out

def process_tree(l):
    #print("Processing " + str(l))
    if len(l) == 1 or type(l) is str:
        if type(l) is list:
            return process_tree(l[0])
        else:
            return float(l)
    
    if len(l) == 2:
        if type(l[1]) is list:
            return -1 * process_tree(l[1])
        else:
            return -1 * l[1]
    
    
    if type(l[0]) is list:
        l[0] = process_tree(l[0])
        
    if type(l[2]) is list:
        l[2] = process_tree(l[2])
        
    op = l[1]
    
    loperand = float(l[0])
    roperand = float(l[2])
    
    if op == '+':
        return loperand + roperand
    elif op == '-':
        return loperand - roperand
    elif op == '*':
        return loperand * roperand
    elif op == '/':
        return loperand / roperand
    elif op == '^':
        return loperand ** roperand
    
    raise ValueError
        

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        line = line.replace(' ', '')
        
        print(line)

        tree = process_string(line)
        #print("FIRST TREE: " + str(tree))
        tree = prioritise_ops(tree, '^')
        #print("^ TREE: " + str(tree))
        tree = prioritise_ops(tree, '*/')
        print("FINAL TREE: " + str(tree))
        
        result = str(round(process_tree(tree),5))
        #print("Unrounded result: " + result)
        print(remove_trailing_numerics(result))