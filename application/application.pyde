import time
import functions

def setup():
    # Sets required global variables
    global currentScreen, timer, backgroundImg, regularFont, d, instrImg, img, Save, img2, img3, img4, img5
    currentScreen = 'start'
    timer = 10
    d = 0
    Save = False
    

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
    global d, currentScreen, Save, randomList, fillOrNoFill

    # Draws start screen
    if currentScreen == 'start':
        startmenu()
        
    if currentScreen == 'hoofdmenu':
        hoofdmenu()
    
    # Draws timer screen
    elif currentScreen == 'timer':
        background(backgroundImg)
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
    elif currentScreen == 'random' :
        instructie()
    
    clock()
    
    
def instructie():
    global d , instrImg, timer, Save, randomList, fillOrNoFill, instr
    if Save != True:
        textSize(50)
        d = d + 1
        l = [525, 150, 275 , 400]
        e = 4
        x = int(random(0, 4))
        f = x
        randomList = []
        fillOrNoFill= []
        while e > 0:
            randomList.append (width / 2 - 0)
            if f > 0:
                x = int(random(0, len(l)))
                randomList.append(l.pop(x))
                fillOrNoFill.append(0)
                f = f - 1
            else:
                fillOrNoFill.append(1)
                randomList.append (l.pop())
            e  = e - 1
        l = [525, 150, 275 , 400]
        e = 4
        x = int(random(0, 4))
        f = x
        while e > 0:
            randomList.append (width / 2 + 130)
            if f > 0:
                x = int(random(0, len(l)))
                randomList.append(l.pop(x))
                fillOrNoFill.append(0)
                f = f - 1
            else:
                fillOrNoFill.append(1)
                randomList.append (l.pop())
            e  = e - 1
        l = [525, 150, 275 , 400 ]
        e = 4
        x = int(random(0, 4))
        f = x
        while e > 0:
            randomList.append (width / 2 + 260)
            if f > 0:
                x = int(random(0, len(l)))
                randomList.append(l.pop(x))
                fillOrNoFill.append(0)
                f = f - 1
            else:
                fillOrNoFill.append(1)
                randomList.append (l.pop())
            e  = e - 1
        l = [525, 150, 275 , 400]
        e = 4
        x = int(random(0, 4))
        f = x
        while e > 0:
            randomList.append (width / 2 - 125)
            if f > 0:
                x = int(random(0, len(l)))
                randomList.append(l.pop(x))
                fillOrNoFill.append(0)
                f = f - 1
            else:
                fillOrNoFill.append(1)
                randomList.append (l.pop())
            e  = e - 1
        x = int(random(0, 4))
        instrlist = ['je mag geen links of rechts zeggen', 'je mag geen coordinaten gebruiken', 'je mag geen ja of nee zeggen','je mag geen omhoog of omlaag gebruiken']
        textSize(30)
        instr = instrlist.pop(x)
        Save = True
    background(backgroundImg)
    image(instrImg, (width // 2) -300 , 30)
    f = 0
    o = 0
    textSize(30)
    while f < 31:
        if o < 16:
            x = fillOrNoFill[o]
        o = o + 1
        if x == 0:
            fill(0)
        if x == 1:
            noFill()
        circle(randomList[f], randomList[f+1], 60)
        text(instr, width / 1.95 ,height / 1.3 )
        f += 2
    timerFunc()
    
        
    

    
def timerFunc():
    global timer, d, currentScreen
    textSize(200)
    fill(0)   
    time.sleep(1)
    if timer == 0 or timer == 'De tijd is op!':
        timer = 'De tijd is op!'
        background(backgroundImg)
        text(timer, width /2, height/2)
    else:
        text(timer, width /1.2, height/2)
        timer = timer - 1
    
def hoofdmenu():
    global font, font2, imgLogo, d, currentScreen
    currentScreen = 'hoofdmenu'
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
    
    textSize(100)
    fill(0,0,0)
    
    textAlign(CENTER)
    text("Hoofdmenu",width/2,120)
   
    textSize(43)
    fill(0,0,0)
    
    textAlign(LEFT)
    text("instructiekaarten",110,350)
    
    textSize(43)
    fill(0,0,0)
    
    textAlign(LEFT)
    text("Droomkaarten",110,500)
    
    textAlign(LEFT)
    text("Stopwatch", 110, 650)
    

    
    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 309 and mouseY < 371 and d == 0:
        d = 1
        currentScreen = 'random'
        background(backgroundImg)
    
    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 459 and mouseY < 521:
        circle(20,20,20)
    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 609 and mouseY < 671 and d == 0: 
        d = 1
        currentScreen = 'timer'
        background(backgroundImg)  
    
def startmenu():
    global img, img2, img3, img4, img5, currentScreen
    image(backgroundImg, 0, 0, width, height)
    image(img2,280,10,720,576)
    image(img3,720,200,150,170)
    image(img4,420, 390, 500, 350)
    
    if (mousePressed == True and mouseX > 500 and mouseX < 820 and mouseY > 500 and mouseY < 600):
        image(img5,420, 390, 500, 350)
        hoofdmenu()
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
    d = 0
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
    d = 0 
