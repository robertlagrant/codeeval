import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line == '':
        continue
    
    out = ''
    upper = True
    line = line.lower()
    
    for letter in line:
        if letter in 'qwertyuiopasdfghjklzxcvbnm':
            if upper:
                upper = False
                out += letter.upper()
            else:
                upper = True
                out += letter.lower()
        else:
            out += letter
    
    print(out)

lines.close()