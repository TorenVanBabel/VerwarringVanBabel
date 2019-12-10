def setup():
    global b,img
    size(400,400)    
    img = loadImage('achtergrond.jpg')
    background(img)
    b = 50
    fullScreen()
    

def draw():
    global message,img
    message =' '
    image(img,300,400)
    
    

def keyTyped():
    global message,d,s,b
    
    print(message)
    
    print keyPressed
    if key == BACKSPACE: 
        pass
    else:
        h=150
        message=message + key
        text(message,b,h)
        b=b+textWidth(message)


    
