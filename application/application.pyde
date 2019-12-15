from datetime import time, datetime
import time
import functions

def setup():
    # Sets required global variables
    global currentScreen, timerDifficulty, timerStart, secondsPassed, backgroundImg, regularFont, d, instrImg, img, Save, img2, img3, img4, img5, img6, img7, img8, img9
    currentScreen = 'start'
    timerStart = datetime.now()
    timerDifficulty = 30
    secondsPassed = 0
    d = 0
    Save = False

    # Startscherm afbeeldingen en highlight button
    img = loadImage("startscherm1.jpg")
    img2 = loadImage("starttekst.png")
    img3 = loadImage("logo.png")
    img4 = loadImage("buttonstart.png")
    img5 = loadImage("buttonstarthigh.png")
    
    # Hoofdmenu afbeeldingen
    img6 = loadImage('InstructieAchter.jpeg')
    img7 = loadImage('InstructieAchter2.jpeg')
    img8 = loadImage('continentkaartAchter.jpeg')
    img9 = loadImage('Babelspel.jpeg')

    # Loads static image for random card generation
    instrImg = loadImage('instructie.jpeg')
    
    # Loads static image for droom card function
    droomImg = loadImage('droom.jpeg')
    
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

   
def draw():    
    global d, currentScreen, Save, randomList, fillOrNoFill, verwarring

    # Draws start screen
    if currentScreen == 'start':
        startmenu()
    
    # Draws hoofdmenu    
    if currentScreen == 'hoofdmenu':
        hoofdmenu()
        difficultyButtons()
    
    # Draws timer screen
    elif currentScreen == 'timer':
        background(backgroundImg)
        timerFunc(width/2)
            
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
        
    # Displays back of an instructie card without verwarring
    elif currentScreen == 'instructieBack':
        verwarring = False
        instructieBack()
        
     # Displays back of an instructie card with verwarring   
    elif currentScreen == 'instructieBackV':
        verwarring = True
        instructieBackV()   
    
    elif currentScreen == 'droomCards':
        droomCards()  
        
        
        
        
    # Draws clock in bottom right on every screen
    clock()
    
    # Draws button back to main menu where needed
    if False == (currentScreen == 'start' or currentScreen == 'hoofdmenu'):
        mainMenuButton()
    
# Generates a new random card and shows it on the screen    
def instructie():
    global d , instrImg, timerStart, Save, randomList, fillOrNoFill, instr, verwarring
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
        instrlist = ['je mag geen links of rechts zeggen', 'je mag geen coordinaten gebruiken', 'je mag geen ja of nee zeggen','je mag geen omhoog, omlaag, \n naar boven of beneden gebruiken']
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
        f += 2
        
    if verwarring == True:
        text(instr, width / 1.95 ,height / 1.3 )
    timerFunc(width/1.2)
    


def droom():
    global droomImage, d
    background(backgroundImg)
    image(instrImg, (width // 2) -300 , 30)
    timerFunc(width/1.2)





# Draws a timer on the screen that counts down to 0
def timerFunc(placement):
    global timerStart, timePassed, d, currentScreen, timerDifficulty
    textSize(200)
    fill(0)
    timePassed = (datetime.now() - timerStart).seconds
    if timePassed > timerDifficulty or timePassed == 'De tijd is op!':
        timePassed = 'De tijd is op!'
        background(backgroundImg)
        text(timePassed, width /2, height/2)
    else:
        text(timerDifficulty - timePassed, placement, height/2)

    
# Draws the hoofdmenu
def hoofdmenu():
    global font, imgLogo, d, currentScreen, timerStart, img6, img7, img8, img9
    currentScreen = 'hoofdmenu'
    background(backgroundImg)

    textSize(100)
    fill(0,0,0)
    
    textAlign(CENTER)
    text("Hoofdmenu",width/2,120)
        
    image(img6,140,250,350,550)
    image(img7,550,250,350,550)
    image(img8,960,250,350,550)
    image(img9,1370,250,350,550)
   


    
    if mousePressed == True and mouseX > 139 and mouseX < 491 and mouseY > 249 and mouseY < 801 and d == 0:
        d = 1
        currentScreen = 'instructieBackV'
        timerStart = datetime.now()
        background(backgroundImg)
    
    if mousePressed == True and mouseX > 549 and mouseX < 901 and mouseY > 249 and mouseY < 801 and d == 0:
        d = 1
        currentScreen = 'instructieBack'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 959 and mouseX < 1311 and mouseY > 249 and mouseY < 801 and d == 0: 
        d = 1
        currentScreen = 'droomCards'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 1369 and mouseX < 1721 and mouseY > 249 and mouseY < 801 and d == 0:
        circle(20,20,20)
    
def startmenu():
    global img, img2, img3, img4, img5, currentScreen, d
    image(backgroundImg, 0, 0, width, height)
    image(img2,280,10,720,576)
    image(img3,720,200,150,170)
    image(img4,420, 390, 500, 350)
    
    if mouseX > 500 and mouseX < 820 and mouseY > 500 and mouseY < 600 :
        image(img5,420, 390, 500, 350)
    if (mousePressed == True and mouseX > 500 and mouseX < 820 and mouseY > 500 and mouseY < 600 and d == 0):
        d = 1
        hoofdmenu()
    else:
        fill(255)   # Black

def clock():
    noSmooth()
    textSize(50)
    fill(255)
    textAlign(RIGHT, BOTTOM)    
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    text(current_time, width-20, height-20)
    
    
def keyPressed():    
    global currentScreen, d, timerStart
    d = 0
    print(keyCode)
    if str(key) == 't':
        currentScreen = 'timer'
        timerStart = datetime.now()
    if str(key) == 'r':
        currentScreen = 'random'
        timerStart = datetime.now()
    if str(key) == 'm':
        currentScreen = 'hoofdmenu'
    if str(key) == 's':
        currentScreen = 'start'
    
def mouseReleased():
    global d
    d = 0 
    
    
def mainMenuButton():
    global currentScreen, Save
    buttonCoordX = 50
    buttonCoordY = 50
    buttonSizeX = 0.1*width
    buttonSizeY = 0.05*height
    rectMode(CORNER)
    fill(218,165,32)
    stroke(0,25,0)
    rect(buttonCoordX, buttonCoordY, buttonSizeX, buttonSizeY)
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(buttonSizeY*0.6)
    text('Menu', (buttonCoordX*2+buttonSizeX)/2, (buttonCoordY*2-textDescent()+buttonSizeY)/2) 
    if (mousePressed == True and (buttonCoordX < mouseX < buttonCoordX+buttonSizeX) and (buttonCoordY < mouseY < buttonCoordY+buttonSizeY)):
        currentScreen = 'hoofdmenu'
        Save = False
        

def difficultyButtons():
    global currentScreen, timerDifficulty
    rectMode(CORNER)
    fill(218,165,32)
    stroke(0,25,0)
    rect(width*0.2, height*0.75, width*0.1, height*0.05)
    rect(width*0.45, height*0.75, width*0.1, height*0.05)
    rect(width*0.7, height*0.75, width*0.1, height*0.05)
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(height*0.05*0.6)
    text('Makkelijk', (width*0.2*2+width*0.1)/2, (height*0.75*2-textDescent()+height*0.05)/2)
    text('Normaal', (width*0.45*2+width*0.1)/2, (height*0.75*2-textDescent()+height*0.05)/2)
    text('Moeilijk', (width*0.7*2+width*0.1)/2, (height*0.75*2-textDescent()+height*0.05)/2) 
    if (mousePressed == True and (width*0.2 < mouseX < width*0.3) and (height*0.75 < mouseY < height*0.8)):
        timerDifficulty = 40
    if (mousePressed == True and (width*0.45 < mouseX < width*0.55) and (height*0.75 < mouseY < height*0.8)):
        timerDifficulty = 30
    if (mousePressed == True and (width*0.7 < mouseX < width*0.8) and (height*0.75 < mouseY < height*0.8)):
        timerDifficulty = 20
        
def instructieBackV():
    global img6, currentScreen, d
    if mousePressed == True and d == 0:
        background(backgroundImg)
        currentScreen = 'random'
    else:
        background(backgroundImg)
        image(img6, (width // 2) -300 , 30)

def instructieBack():
    global img7, currentScreen, d
    if mousePressed == True and d == 0:
        background(backgroundImg)
        currentScreen = 'random'
    else:
        background(backgroundImg)
        image(img7, (width // 2) -300 , 30)
        
def droomCards():
    global img8, currentScreen, d
    if mousePressed == True and d == 0:
        background(backgroundImg)
        currentScreen = 'droomCards'
    else:
        background(backgroundImg)
        image(img8, (width // 2) -300 , 30)
    
        
