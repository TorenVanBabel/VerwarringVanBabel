import time
import functions

def setup():
    # Sets required global variables
    global currentScreen, timer, backgroundImg, regularFont, d, instrImg
    currentScreen = 'start'
    timer = 10
    d = 0
    instrImg = loadImage('instructie')
    
    # Sets the default visual settings (fullscreen/font)
    fullScreen()
    backgroundImg = loadImage('achtergrond.jpg')
    backgroundImg.resize(width, height)
    regularFont = createFont('Felix Titling', 50)
    textFont(regularFont)
    textSize(200)
    fill(0)
    textAlign(CENTER, CENTER)
    background(backgroundImg)
    
def draw():
    global d
    
    
    # Draws start screen
    if currentScreen == 'start':
        textSize(200)
        text(currentScreen, width/2, height/2)
        
    # Draws timer screen
    elif currentScreen == 'timer':
        d= 0
        textSize(200)
        global timer    
        background(backgroundImg)
        text(timer, width/2, height/2)
        time.sleep(1)
        if timer == 1 or timer == 'De tijd is op!':
            timer = 'De tijd is op!'
        else:
            timer = timer - 1
            
    # Draws main menu screen
    elif currentScreen == 'mainmenu':
        text(currentScreen, width/2, height/2)
        #code
    
    # Draws the cards screen
    elif currentScreen == 'card':
        text(currentScreen, width/2, height/2)
        #code
        
    # Draws the manual screen
    elif currentScreen == 'manual':
        text(currentScreen, width/2, height/2)
        #code
    
    # Draws the random screen
    elif currentScreen == 'random' and d == 0:
        background(backgroundImg)
        instructie()
        
         
def instructie():
    global d , instrImg
    textSize(50)
    
    d = d + 1
    l = [40, 100, 160, 220]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(20, l.pop(x), 40)
            f = f - 1
        else:
            noFill()
            circle(20, l.pop(), 40)
        e  = e - 1
    l = [40, 100, 160, 220]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(80, l.pop(x), 40)
            f = f - 1
        else:
            noFill()
            circle(80, l.pop(), 40)
        e  = e - 1
    l = [40, 100, 160, 220]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(140, l.pop(x), 40)
            f = f - 1
        else:
            noFill()
            circle(140, l.pop(), 40)
        e  = e - 1
    l = [40, 100, 160, 220]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(200, l.pop(x), 40)
            f = f - 1
        else:
            noFill()
            circle(200, l.pop(), 40)
        e  = e - 1
        
def keyPressed():    
    global currentScreen, d, timer
    print(keyCode)
    if str(key) == 't':
        currentScreen = 'timer'
        timer = 10
    if str(key) == 'r':
        currentScreen = 'random'
    
def mouseReleased():
    global d
    d = d - 1
