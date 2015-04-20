import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
  
    count = 0
    previous = '-1'
    nums = line.split()
    
    out = ''
    for num in nums:
        if num == previous:
            count += 1
        else:
            if previous is '-1':
                previous = num
                count = 1
            else:
                out += str(count) + " " + previous + " "
                count = 1
                previous = num
    
    out += str(count) + " " + previous + " "
        
    print(out)

lines.close()