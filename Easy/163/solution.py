import sys

defs = {
    0: ('-**--','*--*-','*--*-','*--*-','-**--','-----'),
    1: ('--*--','-**--','--*--','--*--','-***-','-----'),
    2: ('***--','---*-','-**--','*----','****-','-----'),
    3: ('***--','---*-','-**--','---*-','***--','-----'),
    4: ('-*---','*--*-','****-','---*-','---*-','-----'),
    5: ('****-','*----','***--','---*-','***--','-----'),
    6: ('-**--','*----','***--','*--*-','-**--','-----'),
    7: ('****-','---*-','--*--','-*---','-*---','-----'),
    8: ('-**--','*--*-','-**--','*--*-','-**--','-----'),
    9: ('-**--','*--*-','-***-','---*-','-**--','-----'),
}

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
    
    nums = [int(x) for x in line if x.isdigit()]
    
    for x in range(6):
        out = ''
        for num in nums:
            out += defs[num][x]
        
        print(out)

lines.close()