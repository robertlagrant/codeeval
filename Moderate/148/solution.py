import sys
from decimal import Decimal, ROUND_HALF_UP
from colorsys import hsv_to_rgb, hls_to_rgb

def from_cmyk(param,k):
    return str(Decimal(255 * (1-param) * (1-k)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        # Hex
        if line.startswith('#'):
            r,g,b = str(int(line[1:3],16)),str(int(line[3:5],16)),str(int(line[5:7],16))

        # CMYK
        elif line.startswith('('):
            c,m,y,k = map(float, line[1:-1].split(','))
            r,g,b = from_cmyk(c,k), from_cmyk(m,k), from_cmyk(y,k)

        # HSL
        elif line.startswith('HSL'):
            h,s,l = map(int, line[4:-1].split(','))
            
            r,g,b = hls_to_rgb(h/360, l/100, s/100)
            r,g,b = map(lambda x: x*255,[r,g,b])
            r,g,b = map(lambda x: str(Decimal(x).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),[r,g,b])
                    
        # HSV
        elif line.startswith('HSV'):
            h,s,v = map(int, line[4:-1].split(','))
        
            r,g,b = hsv_to_rgb(h/360, s/100, v/100)
            r,g,b = map(lambda x: x*255,[r,g,b])
            r,g,b = map(lambda x: str(Decimal(x).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),[r,g,b])
            
	
        print('RGB('+r+','+g+','+b+')')