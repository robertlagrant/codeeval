import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue
  
    lowercount = 0
    uppercount = 0
    
    for letter in line:
        if letter.isupper():
            uppercount += 1
        else:
            lowercount += 1
    
    total = lowercount+uppercount

    lowerpercent = 100 * lowercount / total
    upperpercent = 100 * uppercount / total
    
    print("lowercase: " + "{0:.2f}".format(lowerpercent) + " uppercase: " + "{0:.2f}".format(upperpercent))

lines.close()
