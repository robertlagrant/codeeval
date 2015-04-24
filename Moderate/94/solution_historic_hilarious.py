import sys

def process_stack(stack):

    print('start: ' + str(stack))

    state = 'EMPTY'
    current_value = 0
    current_op = ''

    for i, (t, s) in enumerate(stack):
        if state == 'EMPTY':
            if t == 'number':
                current_value = float(s)
                state = 'NUMBER'
            if t == 'open_bracket':
                print("Open bracket found at index " + str(i))
                # Find the corresponding close bracket
                bracket_count = 1
                print("Looking in " + str(stack[i+1:]))
                for j, (t1,c2) in enumerate(stack[i+1:]):
                    print("Index " + str(j))
                    if t1 == 'open_bracket':
                        bracket_count += 1
                    elif t1 == 'close_bracket':
                        bracket_count -= 1

                    if bracket_count == 0:
                        print("End found at " + str(j))
                        print("Processing " + str(stack[i+1:i+j+1]))
                        process_stack(stack[i+1:i+j+1])

                state = 'EMPTY'

        if state == 'NUMBER':
            if t == 'op':
                current_op = s
                state = 'AWAITING_NUMBER'
                
        if state == 'AWAITING_NUMBER':
            if t == 'number':
                if current_op == '+':
                    current_value += float(s)
                if current_op == '-':
                    current_value -= float(s)
                if current_op == '*':
                    current_value *= float(s)
                if current_op == '/':
                    current_value /= float(s)
                if current_op == '^':
                    current_value = current_value ** float(s)
                    
                current_op = ''    
                state = 'EMPTY'
                
            if t == 'open_bracket':
                print("Open bracket found at index " + str(i))
                # Find the corresponding close bracket
                bracket_count = 1
                print("Looking in " + str(stack[i+1:]))
                for j, (t1,c2) in enumerate(stack[i+1:]):
                    print("Looking in " + str(j))
                    print('Searching for close bracket from index ' + str(i+j))
                    if t1 == 'open_bracket':
                        bracket_count += 1
                    elif t1 == 'close_bracket':
                        bracket_count -= 1
                    
                    if bracket_count == 0:
                        print("End found at " + str(i+j+2) + ": " + str(stack[i+j+1]))
                        print("Processing " + str(stack[i+1:i+j+1]))
                        current_value += process_stack(stack[i:i+j])
                        break
                        
                state = 'EMPTY'
    
    return current_value
                
            

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # Convert this thing into something I can even vaguely work with
        state = 'EMPTY'
        ops = '+-*/'
        open_bracket = '('
        close_bracket = ')'
        stack = []
        
        for char in line:
            if state == 'EMPTY':
                if char.isdigit():
                    state = 'NUMBER'
                    stack.append(('number', char))
                elif char == '-':
                    state = 'NEGATE'
                elif char == open_bracket:
                    stack.append(('open_bracket', char))
                elif char == close_bracket:
                    stack.append(('close_bracket', char))
            elif state == 'NUMBER':
                if char.isdigit() or char == '.':
                    stack[len(stack)-1] = (stack[len(stack)-1][0], stack[len(stack)-1][1]+char)
                elif char in ops:
                    state = 'OP'
                    stack.append(('op', char))
                elif char == open_bracket:
                    stack.append(('open_bracket', char))
                elif char == close_bracket:
                    stack.append(('close_bracket', char))
            elif state == 'OP':
                if char.isdigit():
                    state = 'NUMBER'
                    stack.append(('number', char))
                elif char == '-':
                    state = 'NEGATE'
                elif char == open_bracket:
                    stack.append(('open_bracket', char))
                elif char == close_bracket:
                    stack.append(('close_bracket', char))
            elif state == 'NEGATE':
                if char.isdigit():
                    state = 'NUMBER'
                    stack.append(('number', '-'+char))
        
        
        print(str(process_stack(stack)))
        
        #print(line + " " + str(stack))
                