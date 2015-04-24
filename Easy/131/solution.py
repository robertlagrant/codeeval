import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
  
    params = line.split()
    nums = params[0]
    command = params[1]
    op = ''
    commandparams = ''
    
    if '+' in command:
        op = '+'
        commandparams = command.split('+')
    
    if '-' in command:
        op = '-'
        commandparams = command.split('-')
    
    leftcount = len(commandparams[0])
    rightcount = len(commandparams[1])
    
    if leftcount > 0:
        leftnum = int(nums[:leftcount])
    else:
        leftnum = 0
        
    if rightcount > 0:
        rightnum = int(nums[-rightcount:])
    else:
        rightnum = 0
    
    if op is '+':
        print(str(leftnum + rightnum))
    if op is '-':
        print(str(leftnum - rightnum))

lines.close()