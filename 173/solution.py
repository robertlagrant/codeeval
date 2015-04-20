import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
  
    previous = '$$$$$'             # something that can't match a single letter
    out = ''
    for letter in line:
        if letter != previous:
            out += letter
            previous = letter
    
    print(out)

lines.close()