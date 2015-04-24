import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line == '':
        continue
  
    params = line.split('.')
    
    fraction = float('0.'+params[1])
    
    major = str(60 * fraction)
    minor = str(60 * float('0.'+major.split('.')[1]))
    
    print(line.split('.')[0]+"."+major.split('.')[0].zfill(2)+"'"+minor.split('.')[0].zfill(2)+'"')
    
 
    #y = fraction * 3600
    
    #print("fraction: " + str(fraction))
    #print(divmod(y, 60))
    
    # I need to rethink my life.

lines.close()
