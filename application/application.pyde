def setup():
    size(800, 800)
    fill(0)
    d = 0
    global d 
    
    
def draw():
    global d
    
    if mousePressed and d == 0:
        d = d + 1
        l = [10, 20, 30, 40]
        e = 4
        x = int(random(0, 4))
        f = x
        while e > 0:
            if f > 0:
                x = int(random(0, len(l)))
                text("X", 10, l.pop(x))
                f = f - 1
            else:
                text("O", 10, l.pop())
            e  = e - 1
        l = [10, 20, 30, 40]
        e = 4
        x = int(random(0, 4))
        f = x
        while e > 0:
            if f > 0:
                x = int(random(0, len(l)))
                text("X", 20, l.pop(x))
                f = f - 1
            else:
                text("O", 20, l.pop())
            e  = e - 1
        l = [10, 20, 30, 40]
        e = 4
        x = int(random(0, 4))
        f = x
        while e > 0:
            if f > 0:
                x = int(random(0, len(l)))
                text("X", 30, l.pop(x))
                f = f - 1
            else:
                text("O", 30, l.pop())
            e  = e - 1
        l = [10, 20, 30, 40]
        e = 4
        x = int(random(0, 4))
        f = x
        while e > 0:
            if f > 0:
                x = int(random(0, len(l)))
                text("X", 40, l.pop(x))
                f = f - 1
            else:
                text("O", 40, l.pop())
            e  = e - 1
            

    
    
    
def mouseReleased():
    global d
    d = d - 1

  
