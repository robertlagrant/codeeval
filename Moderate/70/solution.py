import sys

class Rectangle:
    def __init__(self, ulx, uly, brx, bry):
        self.ul = (ulx,uly)
        self.ur = (brx,uly)
        self.bl = (ulx,bry)
        self.br = (brx,bry)
        
        self.lx = ulx
        self.rx = brx
        self.by = bry
        self.ty = uly
    
    def intersects(self, rect2):
        for x,y in [rect2.ul, rect2.ur, rect2.bl, rect2.br]:
            if x >= self.lx and x <= self.rx and y >= self.by and y <= self.ty:
                return True
        return False
        
    def __repr__(self):
        return 'ul: ' + str(self.ul) + ', ur: ' + str(self.ur) + ', bl: ' + str(self.bl) + ', br: ' + str(self.br)

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        params = list(map(int, line.split(',')))
        r1 = Rectangle(*params[0:4])
        r2 = Rectangle(*params[4:8])
        
        print(r1.intersects(r2))