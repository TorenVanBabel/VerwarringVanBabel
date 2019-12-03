import time
import functions

def setup():
    # Sets required global variables
    global currentScreen, timer, backgroundImg, regularFont, d, instrImg, font, font2, imgLogo
    currentScreen = 'start'
    timer = 10
    d = 0
    instrImg = loadImage('instructie.jpeg')
    font = createFont("Arial", 100)
    font2= createFont("Arial", 35)
    imgLogo = loadImage("BabelLogo.jpeg")
    
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
        global font, font2, imgLogo
        fill(218,165,32)    
    
        rectMode(CENTER)
        rect(340,340,465,60) 
        stroke(0,25,0)
    
        rectMode(CENTER)
        rect(340,490,465,60)
    
        rectMode(CENTER)
        rect(340,640,465,60)
    
        textFont(font)
        fill(0,0,0)
    
        textAlign(CENTER)
        text("Hoofdmenu",width/2,120)
   
        textFont(font2)
        fill(0,0,0)
    
        textAlign(RIGHT)
        text("Randomizer instructiekaarten",570,350)
    
        textFont(font2)
        fill(0,0,0)
    
        textAlign(CENTER)
        text("Gebruikersnamen invoeren",325,500)
    
        textAlign(CENTER)
        text("Stopwatch", 200, 650)
    
        image(imgLogo,1350,700,450,350)
    
        if (mousePressed == True):
            if ((mouseX > 200) and (mouseX < 450) and (mouseY > 75) and (mouseY < 300)):
                 fill(0)     
    
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
    image(instrImg, (width // 2) -300 , 30)
    d = d + 1
    l = [525, 150, 275 , 400]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(width / 2 - 0, l.pop(x), 60)
            f = f - 1
        else:
            noFill()
            circle(width / 2 - 0, l.pop(), 60)
        e  = e - 1
    l = [525, 150, 275 , 400]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(width / 2 + 130, l.pop(x), 60)
            f = f - 1
        else:
            noFill()
            circle(width / 2 + 130, l.pop(), 60)
        e  = e - 1
    l = [525, 150, 275 , 400 ]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(width / 2 + 260, l.pop(x), 60)
            f = f - 1
        else:
            noFill()
            circle(width / 2 + 260, l.pop(), 60)
        e  = e - 1
    l = [525, 150, 275 , 400]
    e = 4
    x = int(random(0, 4))
    f = x
    while e > 0:
        if f > 0:
            x = int(random(0, len(l)))
            fill(0)
            circle(width / 2 - 125, l.pop(x), 60)
            f = f - 1
        else:
            noFill()
            circle(width / 2 - 125, l.pop(), 60)
        e  = e - 1
    x = int(random(0, 4))
    instrlist = ['je mag geen links of rechts zeggen', 'je mag geen coordinaten gebruiken', 'je mag geen ja of nee zeggen','je mag geen omhoog of omlaag gebruiken']
    textSize(30)
    text(instrlist.pop(x), width / 1.95 ,height / 1.3 )
    
    
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
