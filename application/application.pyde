import time
import functions

def setup():
    # Sets required global variables
    global currentScreen, timer, backgroundImg, regularFont, d, instrImg, img, img2, img3, img4, img5
    currentScreen = 'start'
    timer = 10
    d = 0
    

    #Startscherm afbeeldingen en highlight button
    img = loadImage("startscherm1.jpg")
    img2 = loadImage("starttekst.png")
    img3 = loadImage("logo.png")
    img4 = loadImage("buttonstart.png")
    img5 = loadImage("buttonstarthigh.png")

    instrImg = loadImage('instructie.jpeg')

    # Sets the default visual settings (fullscreen/font)
    fullScreen()
    backgroundImg = loadImage('startscherm1.jpg')
    backgroundImg.resize(width, height)
    regularFont = createFont('Felix Titling', 50)
    textFont(regularFont)
    textSize(200)
    fill(0)
    textAlign(CENTER, CENTER)
    background(backgroundImg)
    
    image(img2,280,10,720,576)
    image(img3,720,200,150,170)
    image(img4,420, 390, 500, 350)
   
   
def draw():    
    global d, currentScreen

    # Draws start screen
    if currentScreen == 'start':
        startmenu()
        
    # Draws timer screen
    elif currentScreen == 'timer':
        timerFunc()
            
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
    
    clock()
    
    
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
    
    
def timerFunc():
    global timer, d, currentScreen
    d = 0
    textSize(200)
    fill(255)   
    background(backgroundImg)
    text(timer, width/2, height/2)
    time.sleep(1)
    if timer == 1 or timer == 'De tijd is op!':
        timer = 'De tijd is op!'
    else:
        timer = timer - 1
    
def hoofdmenu():
    global font, font2, imgLogo, d
    d = 0
    fill(218,165,32)    
     
    background(backgroundImg)
        
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
    text("Handleiding",325,500)
    
    textAlign(CENTER)
    text("Stopwatch", 200, 650)
    

    
    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 309 and mouseY < 371 and d == 0:
        d = 1
        while key != 'p':
            instructie()
    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 459 and mouseY < 521:
        circle(20,20,20)
    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 609 and mouseY < 671: 
        circle(20,20,20)    
    
def startmenu():
    global img, img2, img3, img4, img5
    image(backgroundImg, 0, 0, width, height)
    image(img2,280,10,720,576)
    image(img3,720,200,150,170)
    image(img4,420, 390, 500, 350)
    
    if (mousePressed == True and mouseX > 500 and mouseX < 820 and mouseY > 500 and mouseY < 600):
        image(img5,420, 390, 500, 350)
    else:
        fill(255)   # Black
        loop()   

def clock():
    noSmooth()
    textSize(50)
    fill(255)
    textAlign(RIGHT)    
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    text(current_time, width-20, height-20)
    textAlign(CENTER)
    
    
def keyPressed():    
    global currentScreen, d, timer
    print(keyCode)
    if str(key) == 't':
        currentScreen = 'timer'
        timer = 10
    if str(key) == 'r':
        currentScreen = 'random'
    if str(key) == 'm':
        currentScreen = 'mainmenu'
    if str(key) == 's':
        currentScreen = 'start'
    
def mouseReleased():
    global d
    d = d - 1
