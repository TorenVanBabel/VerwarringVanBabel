import time
import functions

def setup():
    # Sets required global variables
    global currentScreen, timer, backgroundImg, regularFont, d
    currentScreen = 'start'
    timer = 10
    d = 0
    
    # Sets the default visual settings (fullscreen/font)
    fullScreen()
    backgroundImg = loadImage('achtergrond.jpg')
    backgroundImg.resize(width, height)
    regularFont = createFont('Felix Titling', 50)
    textFont(regularFont)
    textSize(200)
    fill(0)
    textAlign(CENTER, CENTER)
    
def draw():
    
    
    # Draws start screen
    if currentScreen == 'start':
        textSize(200)
        text(currentScreen, width/2, height/2)
        
    # Draws timer screen
    elif currentScreen == 'timer':
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
    elif currentScreen == 'random':
        global d
        if mousePressed and d == 0:
            textSize(50)
            d = d + 1
            l = [40, 100, 160, 220]
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
            l = [40, 100, 160, 220]
            e = 4
            x = int(random(0, 4))
            f = x
            while e > 0:
                if f > 0:
                    x = int(random(0, len(l)))
                    text("X", 70, l.pop(x))
                    f = f - 1
                else:
                    text("O", 70, l.pop())
                e  = e - 1
            l = [40, 100, 160, 220]
            e = 4
            x = int(random(0, 4))
            f = x
            while e > 0:
                if f > 0:
                    x = int(random(0, len(l)))
                    text("X", 130, l.pop(x))
                    f = f - 1
                else:
                    text("O", 130, l.pop())
                e  = e - 1
            l = [40, 100, 160, 220]
            e = 4
            x = int(random(0, 4))
            f = x
            while e > 0:
                if f > 0:
                    x = int(random(0, len(l)))
                    text("X", 170, l.pop(x))
                    f = f - 1
                else:
                    text("O", 170, l.pop())
                e  = e - 1
        
def keyPressed():    
    global currentScreen, d, timer
    print(keyCode)
    if str(key) == 't':
        currentScreen = 'timer'
        timer = 10
    elif str(key) == 'r':
        currentScreen = 'random'
    
def mouseReleased():
    global d
    d = d - 1
