from datetime import time, datetime
import time

def setup():
    # Sets required global variables
    global currentScreen, timerDifficulty, timerStart, secondsPassed, regularFont, d, playersList, allowedCharacters, currentPlayer, verwarring, addedCoins
    global backgroundImg, instrImg, droomImg, img, Save, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, punten

    playersList = [['', 'Antarctica', 0], ['', 'Europa', 0], ['', 'Noord-Amerika', 0], ['', 'Zuid-Amerika', 0], ['', u'Azi\u00EB', 0], ['', u'Australi\u00EB', 0], ['', 'Afrika', 0]]

    currentPlayer = 0
    allowedCharacters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    verwarring = False
    currentScreen = 'start'
    timerStart = datetime.now()
    timerDifficulty = 30
    addedCoins = False
    secondsPassed = 0
    d = 0
    Save = False

    # Startscherm afbeeldingen en highlight button
    img = loadImage("startscherm1.jpg")
    img2 = loadImage("starttekst.png")
    img3 = loadImage("logo.png")
    img4 = loadImage("buttonstart.png")
    img5 = loadImage("buttonstarthigh.png")
    
    img6 = loadImage("InstructieAchter.jpeg")
    img7 = loadImage("InstructieAchter2.jpeg")
    img8 = loadImage("continentkaartAchter.jpeg")
    img9 = loadImage("Babelspel.jpeg")

    #Loads stuf good or bad
    img10 = loadImage('TextBalkGoed.png')
    img11 = loadImage('TextBalkFout.png')
    punten = 0
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
    global d, currentScreen, Save, randomList, fillOrNoFill, verwarring, addedCoins
    
    if currentScreen != 'GoodOrBad':
        addedCoins = False
    
    # Draws start screen
    if currentScreen == 'start':
        startmenu()
    
    # Draws hoofdmenu    
    elif currentScreen == 'hoofdmenu':
        hoofdmenu()
        difficultyButtons()
    
    # Draws timer screen
    elif currentScreen == 'timer':
        background(backgroundImg)
        timerFunc(width*0.17)
            
    # Draws the cards screen
    elif currentScreen == 'card':
        text(currentScreen, width/2, height/2)
        #code
        
    # Draws the manual screen
    elif currentScreen == 'manual':
        text(currentScreen, width/2, height/2)
        #code
    
    elif currentScreen == 'inputNames':
        inputNames()
        
    # Displays back of an instructie card without verwarring
    elif currentScreen == 'instructieBack':
        verwarring = False
        instructieBack()
    
    # Displays back of an instructie card with verwarring   
    elif currentScreen == 'instructieBackV':
        verwarring = True
        instructieBackV()  
    
    # Draws instuctie card on screen with or without verwarring
    elif currentScreen == 'random' :
        instructie()
        
    #Displays back of an droom card 
    elif currentScreen == 'droomBack':
        droomBack()
        
    #Displays an droom card
    elif currentScreen == 'droomCards':
        droomCards()  
     
    #Displays back of babel card
    elif currentScreen == 'babelen':
        babelen()
        
    elif currentScreen == 'GoodOrBad':
        GoedOfFoutClick()
    
    
    # Draws button back to main menu where needed
    if False == (currentScreen == 'start' or currentScreen == 'hoofdmenu' or currentScreen == 'inputNames'):
        mainMenuButton()
    
    #Draws names from the players on the screen where needed
    if False == (currentScreen == 'inputNames' or currentScreen == 'start'):
        showNames()
        
    # Draws clock in bottom right on every screen
    clock()
    
def startmenu():
    global img, img2, img3, img4, img5, currentScreen, d
    image(backgroundImg, 0, 0, width, height)
    image(img2,570,80,720,576)
    image(img3,1020,300,150,170)
    image(img4,700, 450, 500, 350)
    
    if mouseX > 780 and mouseX < 1100 and mouseY > 560 and mouseY < 660:
        d = 1
        image(img5,700, 450, 500, 350)
        if mousePressed == True:
            currentScreen = 'inputNames'

def inputNames():
    global currentPlayer
    background(backgroundImg)
    rectMode(CENTER)
    fill(255)
    rect(width/2, height*0.55, width*0.35, height*0.075)
    
    textAlign(CENTER, CENTER)
    textSize(60)
    fill(0)
    text('Speler ' + str(currentPlayer + 1) + ' input je naam'+ ' (' + playersList[currentPlayer][1] + ')', width/2, height/2 * 0.8) 
    text(playersList[currentPlayer][0], width/2, height*0.54)
    mainMenuButtonNames()

def mainMenuButtonNames():
    global currentScreen, Save, d
    buttonCoordX = width*0.375
    buttonCoordY = height/2*1.3
    buttonSizeX = 0.25*width
    buttonSizeY = 0.05*height
    rectMode(CORNER)
    if playersList[2][0] != '':
        fill(218,165,32)
    else:
        fill(200)
    stroke(0,25,0)
    rect(buttonCoordX, buttonCoordY, buttonSizeX, buttonSizeY)
    
    
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(buttonSizeY*0.6)
    text('Klaar', width/2, (buttonCoordY*2+buttonSizeY)/2-textDescent()) 
    if (mousePressed == True and (buttonCoordX < mouseX < buttonCoordX+buttonSizeX) and (buttonCoordY < mouseY < buttonCoordY+buttonSizeY) and playersList[2][0] != ''):
        d = 1
        currentScreen = 'hoofdmenu'
        Save = False    

# Draws the hoofdmenu
def hoofdmenu():
    global font, font2, imgLogo, d, currentScreen, timerStart, img6,img7, img8, img9
    currentScreen = 'hoofdmenu'
    background(backgroundImg)
        
    fill(218,165,32)
    stroke(0,25,0)
    rectMode(CENTER)
    

    textSize(60)

    

    fill(0,0,0)
    
    textAlign(CENTER)
    text("Klik op de kleur van het vakje waar je op staat",width/2,220)


    image(img6,30,250,350,550)
    image(img7,410,250,350,550)
    image(img8,790,250,350,550)
    image(img9,1170,250,350,550)
   
    textSize(43)
    fill(0,0,0)
    textAlign(LEFT)
        
    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 309 and mouseY < 371 and d == 0:
        d = 1
        currentScreen = 'random'
        timerStart = datetime.now()
        background(backgroundImg)
    

    if mousePressed == True and mouseX > 105 and mouseX < 575 and mouseY > 459 and mouseY < 521:
        circle(20,20,20)
    if mousePressed == True and mouseX > 29 and mouseX < 381 and mouseY > 249 and mouseY < 801 and d == 0: 
        d = 1
        currentScreen = 'instructieBackV'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 409 and mouseX < 761 and mouseY > 249 and mouseY < 801 and d == 0:
        d = 1
        currentScreen = 'instructieBack'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 789 and mouseX < 1141 and mouseY > 249 and mouseY < 801 and d == 0: 
        d = 1
        currentScreen = 'droomBack'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 1169 and mouseX < 1521 and mouseY > 249 and mouseY < 801 and d == 0:
        d = 1
        currentScreen = 'babelen'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True:
        d = 1
    

def showNames():
    textSize(30)
    fill(0)
    textAlign(LEFT, TOP)
    text('Spelers:', width * 0.82, height * 0.25)
    text('Munten:', width * 0.92, height * 0.25)
    for x in range(0,7):
        if playersList[x][0] != '':
            text(playersList[x][0],width * 0.82, (height * x * 0.04) + (height * 0.3))
            text(str(playersList[x][2]), width * 0.92, (height * x * 0.04) + (height * 0.3))    


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
        
def GoedOfFoutClick():
    global goed,fout,img10,img11, b, punten,d, backgroundImg, Save, addedCoins
    background(backgroundImg)
    image(img10,330,500,500,300)
    image(img11,1100,510,500,290)
    fill(0)
    stroke(100,100,100)
    textAlign(CENTER)
    textSize(80)
    l = ['5','10','15','20','25','50']
    textSize(40)
    text(str(punten),1700,100,100,100)
    if Save == True:
        print('good')
        text('Yes!\nJe krijgt een munt',width/ 2,100)
        if addedCoins == False:
            playersList[currentPlayer][2] = int(playersList[currentPlayer][2]) + int(b)
            addedCoins = True
        fill(220,150,0)
        rect(1600,100,300,110)
        print (b)
        fill(0)
        text(b+'+',1750,180)
        print(playersList[currentPlayer][2])
    elif mousePressed == True and mouseX > 380 and mouseX < 780 and mouseY > 550 and mouseY < 750 and d == 0:
        d = 1
        b = int(random(0,5))
        b = l[b]
        fill(200)
        print('good')
        text('Yes!\nJe krijgt een munt',width/ 2,100)
        if addedCoins == False:
            playersList[currentPlayer][2] = int(playersList[currentPlayer][2]) + int(b)
            addedCoins = True
        fill(220,150,0)
        rect(1600,100,300,110)
        print (b)
        fill(0)
        text(b+'+',1750,180)
        print(punten)
        Save = True
        
        
    elif mousePressed == True and mouseX > 1050 and  mouseX  < 1450 and mouseY  > 550 and mouseY < 750 and d == 0:
        d = 1
        text('Jammer volgende Ronde beter',width/2,900)
    else:
        pass        
        

def difficultyButtons():
    global currentScreen, timerDifficulty
    rectMode(CORNER)
    fill(218,165,32)
    stroke(0,25,0)
    rect(width*0.2, height*0.85, width*0.1, height*0.05)
    rect(width*0.45, height*0.85, width*0.1, height*0.05)
    rect(width*0.7, height*0.85, width*0.1, height*0.05)
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(height*0.05*0.6)
    text('Makkelijk', (width*0.2*2+width*0.1)/2, (height*0.85*2-textDescent()+height*0.05)/2)
    text('Normaal', (width*0.45*2+width*0.1)/2, (height*0.85*2-textDescent()+height*0.05)/2)
    text('Moeilijk', (width*0.7*2+width*0.1)/2, (height*0.85*2-textDescent()+height*0.05)/2) 
    if (mousePressed == True and (width*0.2 < mouseX < width*0.3) and (height*0.85 < mouseY < height*0.9)):
        timerDifficulty = 40
    if (mousePressed == True and (width*0.45 < mouseX < width*0.55) and (height*0.85 < mouseY < height*0.9)):
        timerDifficulty = 30
    if (mousePressed == True and (width*0.7 < mouseX < width*0.8) and (height*0.85 < mouseY < height*0.9)):
        timerDifficulty = 2

    
def instructieBackV():
    global img6, currentScreen, d, timerStart
    if mousePressed == True and d == 0:
        background(backgroundImg)
        timerStart = datetime.now()
        currentScreen = 'random'
    else:
        background(backgroundImg)
        image(img6, (width // 2) -300 , 30)


def instructieBack():
    global img7, currentScreen, d, timerStart
    if mousePressed == True and d == 0:
        background(backgroundImg)
        timerStart = datetime.now()
        currentScreen = 'random'
        
    else:
        background(backgroundImg)
        image(img7, (width // 2) -300 , 30)
        
def droomBack():
    global img8, currentScreen, d, timerStart, Save 
    if mousePressed == True and d == 0:
        background(backgroundImg)
        timerStart = datetime.now()
        Save = False
        currentScreen = 'droomCards'
    else:
        background(backgroundImg)
        image(img8, (width // 2) -300 , 30)

def babelen():
    global img9, currentScreen, d
    background(backgroundImg)
    image(img9, (width // 2) -300 , 30)
    
# Generates a new random card and shows it on the screen    
def instructie():
    global d , instrImg, timerStart, Save, randomList, fillOrNoFill, instr, verwarring
    if Save != True:
        textSize(50)
        d = d + 1
        l = [525, 150, 275 , 400]
        e = 4
        x = int(random(0, 5))
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
        x = int(random(0, 5))
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
        x = int(random(0, 5))
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
        x = int(random(0, 5))
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
        fill(0)
        
    timerFunc(width*0.17)
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
        textAlign(LEFT, CENTER)
        text(instr, width / 2.75 ,height / 1.4 )
    timerFunc(width*0.17)        

def droomCards():
    global droomImg, d, Save, droom
    fill(0)
    textAlign(CENTER, CENTER)
    background(backgroundImg)
    image(droomImg, (width // 2) -300 , 30)

    if Save == False:
        x = int(random(0, 4))
        droomList = ['Aarde','Aarde','Aarde','Aarde']
        textSize(60)
        droom = droomList.pop(x)
        Save = True
    if Save == True:
        text(droom, width / 1.9 ,height / 2 )
        timerFunc(width*0.17)


# Draws a timer on the screen that counts down to 0
def timerFunc(placement):
    global timerStart, timePassed, d, currentScreen, timerDifficulty, Save
    textSize(200)
    fill(255)
    textAlign(CENTER, CENTER)
    timePassed = (datetime.now() - timerStart).seconds
    if timePassed > timerDifficulty or timePassed == 'De tijd is op!':
        timePassed = 'De tijd is op!'
        background(backgroundImg)
        Save = False
        currentScreen = 'GoodOrBad'
    else:
        text(timerDifficulty - timePassed, placement, height/2)


def clock():
    noSmooth()
    textSize(50)
    fill(255)
    textAlign(RIGHT, BOTTOM)    
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    text(current_time, width-20, height-20)
    

def keyReleased():
    global currentPlayer, playerList, currentScreen
    if currentScreen == 'inputNames':
        if key in allowedCharacters and len(playersList[currentPlayer][0]) <= 10:
            playersList[currentPlayer][0] += key
        elif key == BACKSPACE:                        
            playersList[currentPlayer][0] = playersList[currentPlayer][0][:-1]
        elif key == ENTER and playersList[currentPlayer][0] != '':
            if currentPlayer == 6:
                currentScreen = 'hoofdmenu'
            else:
                currentPlayer += 1
            
def keyPressed():    
    global currentScreen, d, timerStart
    d = 0
    print(keyCode)

    
def mouseReleased():
    global d, currentScreen
    d = 0 
    if (currentScreen == 'inputNames' and (width*0.375 < mouseX < width*0.625) and (height/2*1.3 < mouseY < height/2*1.3+0.05*height) and playersList[2][0] != ''):
        currentScreen = 'hoofdmenu'
