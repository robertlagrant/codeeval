import sys

rules = {
    4: ('M', 'M', 'M', 'M'),
    3: ('C', 'CD', 'D', 'CM'),
    2: ('X', 'XL', 'L', 'XC'),
    1: ('I', 'IV', 'V', 'IX'),
}

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
    
    out = ''
    
    for x in range(len(line), 0, -1):
        a, b, c, d = rules[x]
        count = int(line[0])
        if count < 4:
            out += a * count
        elif count is 4:
            out += b
        elif count is 5:
            out += c
        elif count < 9:
            out += c + a * (count-5)
        else:
            out += d
                
        line = line[1:]
    
    print(out)

lines.close()
