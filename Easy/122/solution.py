import sys

conversions = {
    'a': '0',
    'b': '1',
    'c': '2',
    'd': '3',
    'e': '4',
    'f': '5',
    'g': '6',
    'h': '7',
    'i': '8',
    'j': '9'
}

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
  
    out = ''
    for letter in line:
        if letter.isdigit():
            out += letter
        if letter in conversions:
            out += conversions[letter]
    
    if out is '':
        out = 'NONE'
    
    print(out)

lines.close()
