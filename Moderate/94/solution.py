import sys, re

def is_number(num):
    try:
        float(num)
        return True
    except (TypeError, ValueError):
        return False
            

def remove_trailing_numerics(floatstring):
    if '.' not in floatstring:
        return floatstring
        
    out = ''
    flag = True
    for s in reversed(floatstring):
        
        if s == '0' and len(out) == 0 and flag:
            continue
        elif s == '.' and len(out) == 0:
            flag = False
            continue
        else:
            out += s
    
    return out[::-1]
    

def prioritise_ops(stuff, op):
    out = []
    #print("Prioritising for "+op+" "+ str(stuff))
    
    skip = False
    for i, el in enumerate(stuff):
        if skip:
            skip = False
            continue
            
        if type(el) is str and el in op and len(stuff) > 3:
            #print("MATCH!")
            out[len(out)-1] = [out[len(out)-1], el, stuff[i+1]]
            skip = True
        elif type(el) is list:
            sublist = prioritise_ops(el, op)
            out.append(sublist)
        else:
            out.append(el)
    
    #print("Done! " + str(out))
    
    return out
    
    
def process_string(raw_string):
    ops = '+-*/^'
    state = 'START'
    tokens = []
    
    # Get rid of annoying things like (-159.5). Convert them straight away to -159.5
    raw_string = re.sub(r'\((-?\d+\.?\d*)\)',r'\1', raw_string)

    chars = enumerate(raw_string)
    
    # Basically just sort out the brackets into a list of lists structure. Everything else strings for now.
    for i, char in chars:
        if char == '(':
            bracket_count = 1; inner_string = ''; cont = True
            while cont:
                _, next_char = next(chars)
                if next_char == ')':
                    bracket_count -= 1
                    if bracket_count == 0:
                        cont = False
                    else:
                        inner_string += next_char
                elif next_char == '(':
                    bracket_count += 1
                    inner_string += next_char
                else:
                    inner_string += next_char
            
            tokens.append(process_string(inner_string))
        elif i > 0 and type(tokens[len(tokens)-1]) is str:
            tokens[len(tokens)-1] += char
        elif i == 0 and raw_string[1] == '(':
            tokens.append('-1')
            tokens.append('*')
        else:
            tokens.append(char)

    # Tokenise strings between brackets
    out = []
    titer = enumerate(tokens)
    for i, token in titer:
        if type(token) is not list:
            subtokens = re.findall('(\(.*\)|\-?\d+\.?\d*|\+|\-|\*|\/|\^)', token)
            siter = enumerate(subtokens)
            for j, subtoken in siter:
                # If current token starts with '-', 
                # check the previous token to see whether it's unary or not
                if len(subtoken) > 1 and subtoken.startswith('-'):
                    if len(out) > 0:
                        previous = out[len(out)-1]
                        if type(previous) is list or previous not in '^*/-+':
                            out.append('-')
                            out.append(subtoken[1:])
                        else:
                            out.append(subtoken)
                    else:
                        out.append(subtoken)
                else:
                    out.append(subtoken)
        else:
            out.append(token)

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
    
    try:
        loperand = float(l[0])
    except OverflowError:
        loperand = int(l[0])
    
    try:
        roperand = float(l[2])
    except OverflowError:
        roperand = int(l[2])

    #print(str(loperand) + " " + op + " " + str(roperand))
    
    outcome = 0
    
    if op == '+':
        outcome = loperand + roperand
    elif op == '-':
        outcome = loperand - roperand
    elif op == '*':
        outcome = loperand * roperand
    elif op == '/':
        #print(str(loperand) + "/" + str(roperand))
        outcome = loperand / roperand
    elif op == '^':
        if roperand > 300:
            roperand = int(roperand)
        if loperand > 300:
            loperand = int(loperand)
        #print(str(loperand) + "^" + str(roperand))
        outcome = loperand ** roperand
        
    #print("OUTCOME " + str(outcome))
        
    if len(l) > 3:
        out = [outcome]
        for el in l[3:]:
            out.append(el)
        return process_tree(out)
    else:
        return outcome
    
    raise ValueError


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        #print()
        #print(line)    
        line = line.replace(' ', '')

        tree = process_string(line)
        #print(str(tree))
        tree = prioritise_ops(tree, '^')
        #print(str(tree))
        tree = prioritise_ops(tree, '*/')
        #print(str(tree))
        result = str(round(process_tree(tree),5))
        me = remove_trailing_numerics(result)
        line = line.replace('^', '**')
        #ev = remove_trailing_numerics(str(round(eval(line),5)))
        print(me)
        #if me != ev:
        #    print("NO MATCH: " + line + " (me=" + me + "), (ev=" + ev + ")")
        #else:
        #    print(me + " == " + ev)
        #print(line + " " + me + " vs " + ev + " " + "" if me == ev else "NO MATCH")