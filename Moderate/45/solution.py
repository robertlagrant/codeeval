import sys

def reverse(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    s = str(num)
    l = len(s)
    if l % 2 == 0:
        left, right = s[:int(l/2)], s[int(l/2):]
    else:
        left, right = s[:int(l/2)], s[int(l/2)+1:]
    
    return left == right[::-1]


with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        number,count = int(line), 0
        
        while not is_palindrome(number):
            count += 1
            number = number + reverse(number)
            
        print(str(count) + ' ' + str(number))