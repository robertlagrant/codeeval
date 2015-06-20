import sys,re

numbers = [0b11111100, 0b01100000, 0b11011010, 0b11110010, 0b01100110, 0b10110110, 0b10111110, 0b11100000, 0b11111110, 0b11110110]

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        params = line.split(';')
        states = [int(state, 2) for state in params[0].split()]
        
        number = params[1]
        number = number if '.' in number else number + '.'
        nums = [num for num in re.split('(\d\.?)',number) if num != '']
        binary_nums = []
        for i, num in enumerate(number):
            if num != '.':
                binary_nums.append(numbers[int(num)])
            else:
                binary_nums[i-1] += 0b1
        
        success = False
        nums_length = len(binary_nums)
        for i in range(len(states)-nums_length + 1):
            matched_letters = 0
            for j in range(nums_length):
                if states[i+j] & binary_nums[j] == binary_nums[j]:
                    matched_letters += 1
                else:
                    break
            
            if matched_letters == nums_length:
                success = True
                break
        
        print('1' if success else '0')
        
        
        
     