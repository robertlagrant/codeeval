morse_code = {
    '.-':   'A', 
    '-...': 'B', 
    '-.-.': 'C', 
    '-..':  'D', 
    '.':    'E', 
    '..-.': 'F', 
    '--.':  'G', 
    '....': 'H', 
    '..':   'I', 
    '.---': 'J', 
    '-.-':  'K', 
    '.-..': 'L', 
    '--':   'M', 
    '-.':   'N', 
    '---':  'O', 
    '.--.': 'P', 
    '--.-': 'Q', 
    '.-.':  'R', 
    '...':  'S', 
    '-':    'T', 
    '..-':  'U', 
    '...-': 'V', 
    '.--':  'W', 
    '-..-': 'X', 
    '-.--': 'Y', 
    '--..': 'Z', 
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',     		 
    '.....': '5',  	 		 
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
}

import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line == '':
        continue
    
    words = line.split('  ')
    out = ''
    
    for word in words:
        letters = word.split()
        out += ''.join(morse_code[letter] for letter in letters) + ' '
    
    print(out.strip())
lines.close()