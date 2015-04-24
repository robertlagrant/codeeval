import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line == '':
        continue

    def test(input):
        length = len(line)
        
        for x in range(1, length+1):
            if(length % x is not 0):
                continue
        
            slice = input[0:x]
            slength = len(slice)
            if input == slice * int(length/slength):
                return slength
        
    print(str(test(line)))

lines.close()