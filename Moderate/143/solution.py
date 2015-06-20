import sys
import re


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        original, target = line.split(';')
        
        # Replace contiguous spaces with one space
        original = re.sub(r"\s+", " ", original)
        
        # Split target into targets
        targets = target.split()
        
        redacted, current_target, i, not_possible, space_next = '', 0, 0, False, False
        while i < len(original):
            if not space_next and current_target is not None and targets and len(targets) > 0 and len(original) >= i+len(targets[current_target]) and original[i:i+len(targets[current_target])].lower() == targets[current_target].lower():
                redacted += targets[current_target]
                i += len(targets[current_target])
                
                if current_target < len(targets)-1:
                    current_target += 1
                    space_next = True
                else:
                    current_target = None
            
            elif original[i] == ' ':
                 redacted += ' '
                 space_next = False
                 i += 1
            else:
                redacted += '_'
                i += 1
        
        #print(line + ' :: ' + ('I cannot fix history' if current_target is not None else redacted))
        print('I cannot fix history' if current_target is not None else redacted)