import time
import functions

def setup():
    # Sets required global variables
    global currentScreen, timer, backgroundImg, regularFont
    currentScreen = 'start'
    timer = 10
    
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
    background(backgroundImg)
    
    # Draws start screen
    if currentScreen == 'start':
        text(currentScreen, width/2, height/2)
        
    # Draws timer screen
    elif currentScreen == 'timer':
        global timer    
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
    
def keyPressed():    
    global currentScreen
    print(keyCode)
    currentScreen = 'timer'
    fontList = PFont.list()
    print(fontList)
