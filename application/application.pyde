from datetime import time, datetime
import time

def setup():
    # Sets required global variables
    global currentScreen, timerDifficulty, timerStart, secondsPassed, regularFont, d, playersList, allowedCharacters, currentPlayer, verwarring, addedCoins, Higlight, fillOrNoFill
    global backgroundImg, instrImg, droomImg, img, Save, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, punten, ground10, ground15, ground20, ground50, landkaart
    global Europe, NorthAmerika, SouthAmerika, Africa, Asia, Antartica, Australia, playersTurn, PlayerCount, gameWinner, gameOver, seccondPlayer, clicked
    playersList = [['', 'Antarctica', 500], ['', 'Europa', 0], ['', 'Zuid-Amerika', 0], ['', 'Noord-Amerika', 0], ['', u'Azi\u00EB', 0], ['', u'Australi\u00EB', 0], ['', 'Afrika', 0]]

    fillOrNoFill = ''
    gameOver = False
    currentPlayer = 0
    clicked = False
    allowedCharacters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    verwarring = False
    currentScreen = 'start'
    timerStart = datetime.now()
    timerDifficulty = 30
    addedCoins = False
    secondsPassed = 0
    d = 0
    Higlight = 0
    Save = False
    #looks which players turn it is
    seccondPlayer = ''
    PlayerCount = -1
    playersTurn = 0
    #makes empty list for every continen t
    Europe = [0,0,0,0,0,0,0,0,0]
    NorthAmerika = [0,0,0,0,0,0,0,0,0]
    SouthAmerika = [0,0,0,0,0,0,0,0,0]
    Africa = [0,0,0,0,0,0,0,0,0]
    Asia = [0,0,0,0,0,0,0,0,0]
    Antartica = [0,0,0,0,0,0,0,0,0]
    Australia = [0,0,0,0,0,0,0,0,0] 
    
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
    img10 = loadImage('TextBalkGoedGoed.png')
    img11 = loadImage('TextBalkFoutGoed.png')
    punten = 0
    # Loads static image for random card generation
    instrImg = loadImage('instructie.jpeg')
    
    # Loads static image for droom card function
    droomImg = loadImage('droom.jpeg')
    
    # Loads static images for buying contintents
    ground10 = loadImage('Grondstuk10.png')
    ground15 = loadImage('Grondstuk15.png')
    ground20 = loadImage('Grondstuk20.png')
    ground50 = loadImage('50.jpeg')
    landkaart = loadImage('landkaart2.png')
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
    global d, currentScreen, Save, randomList, fillOrNoFill, verwarring, addedCoins, clicked
    
    if False == (currentScreen == 'babelen' or currentScreen == 'GoodOrBad'):
        addedCoins = False
        clicked = False
        
    
    # Draws start screen
    if currentScreen == 'start':
        startmenu()
        difficultyButtons()
    # Draws hoofdmenu    
    elif currentScreen == 'hoofdmenu':
        hoofdmenu()
    
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
    elif currentScreen == 'backBabelen':
        backBabelen()
    
    #Displays back of babel card
    elif currentScreen == 'babelen':
        babelen()
        
    elif currentScreen == 'GoodOrBad':
        GoedOfFoutClick()
    
    elif currentScreen == 'worldMap':
        checkIfGameFinished()
        worldMap()
        
    elif currentScreen == 'gameFinished':
        gameFinished()
        
    # Draws button back to main menu where needed
    if False == (currentScreen == 'start' or currentScreen == 'hoofdmenu' or currentScreen == 'inputNames' or currentScreen == 'gameFinished'
                      or currentScreen == 'droomCards' or currentScreen == 'random' or currentScreen == 'GoodOrBad' or (currentScreen == 'babelen' and addedCoins == True)):
        mainMenuButton()
    
    #Draws names from the players on the screen where needed
    if False == (currentScreen == 'inputNames' or currentScreen == 'start' or currentScreen == 'gameFinished' or currentScreen == 'GoodOrBad' or (currentScreen == 'babelen' and addedCoins == True)):
        showNames()
        
        
    
    
    # Draws clock in bottom right on every screen
    clock()
    
def startmenu():
    global img, img2, img3, img4, img5, currentScreen, d, Higlight
    image(backgroundImg, 0, 0, width, height)
    image(img2,width*0.3,height*0.1,width*0.38,height*0.5)
    image(img3,width*0.53,height*0.28,width*0.08,height*0.15)
    image(img4,width*0.36, height*0.42, width*0.26, height*0.32)
    
    textAlign(CENTER)
    fill(255)
    textSize(70)
    text('Kies de moeilijkheidsgraad', width/2, height * 0.8)
    
    if mouseX > width*0.41 and mouseX < width*0.41 + width*0.16 and mouseY > height*0.529 and mouseY < height*0.529 + height*0.086:
        d = 1
        image(img5,width*0.36, height*0.42, width*0.26, height*0.32)
        if mousePressed == True and Higlight != 0:
            currentScreen = 'inputNames'

def inputNames():
    global currentPlayer
    background(backgroundImg)
    rectMode(CENTER)
    fill(255)
    rect(width/2, height*0.55, width*0.35, height*0.075)
    
    textAlign(CENTER, CENTER)
    textSize(65)
    fill(0)
    text('Naam speler ' + str(currentPlayer + 1) +  ' (' + playersList[currentPlayer][1] + ')', width/2, height/2 * 0.8) 
    text(playersList[currentPlayer][0], width/2, height*0.54)
    mainMenuButtonNames()

def mainMenuButtonNames():
    global currentScreen, Save, d, PlayerCount, currentPlayer
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
        if playersList[currentPlayer][0] != '':
            PlayerCount += 1
        d = 1
        currentScreen = 'hoofdmenu'
        Save = False    

# Draws the hoofdmenu
def hoofdmenu():
    global font, font2, imgLogo, d, currentScreen, timerStart, img6,img7, img8, img9, playersTurn, playersLists, PlayerCount, Save
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
        

    
    if mousePressed == True and mouseX > 29 and mouseX < 381 and mouseY > 249 and mouseY < 801 and d == 0: 
        d = 1
        Save = False
        currentScreen = 'instructieBackV'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 409 and mouseX < 761 and mouseY > 249 and mouseY < 801 and d == 0:
        d = 1
        Save = False
        currentScreen = 'instructieBack'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 789 and mouseX < 1141 and mouseY > 249 and mouseY < 801 and d == 0: 
        d = 1
        Save = False
        currentScreen = 'droomBack'
        timerStart = datetime.now()
        background(backgroundImg)
    if mousePressed == True and mouseX > 1169 and mouseX < 1521 and mouseY > 249 and mouseY < 801 and d == 0:
        d = 1
        Save = False
        currentScreen = 'backBabelen'
        timerStart = datetime.now()
        background(backgroundImg)

    rectMode(CORNER)
    fill(218,165,32)
    rect(width*0.015, height*0.80, width*0.38, height*0.07)
    fill(0)
    if mouseX > width*0.015 and mouseX < width*0.38 + width *0.015 and mouseY > height*0.8 and mouseY < height * 0.07 + height * 0.8:
        fill(218,165,32)
        stroke(255)
        rect(width*0.015, height*0.80, width*0.38, height*0.07)
        fill(255)
        stroke(0)
    text('Volgende speler ', width*0.03, height*0.85,)
    fill(0)
    circle(width*0.347, height*0.835, 50)
    if mousePressed == True and mouseX > width*0.015 and mouseX < width*0.38 + width *0.015 and mouseY > height*0.8 and mouseY < height * 0.07 + height * 0.8 and d == 0:
        if playersTurn < PlayerCount:
            playersTurn += 1
        else:
            playersTurn = 0   
        d = 1
        
    fill(218,165,32)
    rect(width*0.41, height*0.80, width*0.38, height*0.07)
    fill(0)
    if mouseX > width*0.41 and mouseX < width*0.38 + width *0.41 and mouseY > height*0.8 and mouseY < height * 0.07 + height * 0.8:
        fill(218,165,32)
        stroke(255)
        rect(width*0.41, height*0.80, width*0.38, height*0.07)
        fill(255)
        stroke(0)
    text('Wereldkaart ', width*0.42, height*0.85,)
    fill(0)
    circle(width*0.347, height*0.835, 50)
    if mousePressed == True and mouseX > width*0.41 and mouseX < width*0.38 + width *0.41 and mouseY > height*0.8 and mouseY < height * 0.07 + height * 0.8 and d == 0:
        d = 0
        currentScreen = 'worldMap'
        
def showNames():
    global playersTurn
    rectMode(CORNER)
    fill(218,165,32)
    stroke(0,25,0)
    rect(width*0.81, height*0.25, width*0.185, height*0.35)
    textSize(30)
    fill(0)
    textAlign(LEFT, TOP)
    text('Spelers:', width * 0.82, height * 0.25)
    text('Munten:', width * 0.92, height * 0.25)
    for x in range(0,7):
        if playersList[x][0] != '':
            if playersTurn == x:
                fill(255)
            text(playersList[x][0],width * 0.82, (height * x * 0.04) + (height * 0.3))
            text(str(playersList[x][2]), width * 0.93, (height * x * 0.04) + (height * 0.3))    
            fill(0)

def mainMenuButton():
    global currentScreen, Save
    buttonCoordX = width *0.85
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
    global goed,fout,img10,img11, b, b1, punten,d, backgroundImg, Save, addedCoins, currentScreen, playersTurn, PlayerCount, l, seccondPlayer
    background(backgroundImg)
    if Save != True:
        image(img10,width*0.17,height*0.3,width*0.25,height*0.6)
        image(img11,width*0.55,height*0.3,width*0.25,height*0.6)
    fill(0)
    stroke(0)
    textAlign(CENTER)
    textSize(80)
    l = ['5','10','15','20','25','50']
    textSize(40)
    if Save == True:

        fill(220,150,0)
        rectMode(CORNER)
        rect(width*0.43,height*0.79,width*0.15,height*0.041)
        rect(650,50,600, 250)
        rect(650,450,600, 250)
        fill(0)
        text('Menu', width/2, height*0.83)
        text(playersList[playersTurn][0] + '\nJe krijgt een munt van ' + str(b) +'\nJe hebt nu ' + str(playersList[playersTurn][2]) + ' munten',width/ 2,100)
        text(playersList[seccondPlayer][0] + '\nJe krijgt een munt van ' + str(b1)+'\nJe hebt nu ' + str(playersList[seccondPlayer][2]) +' munten',width/ 2,500)

    
        
        if mousePressed == True and mouseX > width*0.43 and mouseX < width*0.43 + width*0.15 and mouseY > height*0.79 and mouseY < height*0.79 + height*0.041:
            currentScreen = 'hoofdmenu'

        
        
    elif mousePressed == True and mouseX > 380 and mouseX < 780 and mouseY > 550 and mouseY < 750 and d == 0:
        b = int(random(0,6))
        b1 = int(random(0,6))
        b = l[b]
        b1 = l[b1]
        Save = True
        if addedCoins == False:
            playersList[seccondPlayer][2] = int(playersList[seccondPlayer][2]) + int(b1)
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) + int(b)
            addedCoins = True






        
        
    elif mousePressed == True and mouseX > 1050 and  mouseX  < 1450 and mouseY  > 550 and mouseY < 750 and d == 0 and Save == False:
        d = 1
        currentScreen = 'hoofdmenu'

    if currentScreen == 'hoofdmenu':
        seccondPlayer = ''
        if playersTurn < PlayerCount:
            playersTurn += 1
        else:
            playersTurn = 0   
        d = 1   
        

   
 

def difficultyButtons():
    global currentScreen, timerDifficulty, Higlight
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
    if Higlight == 1:
        fill(218,165,32)
        stroke(255)
        rect(width*0.2, height*0.85, width*0.1, height*0.05)
        textAlign(CENTER, CENTER)
        fill(255)
        textSize(height*0.05*0.6)
        text('Makkelijk', (width*0.2*2+width*0.1)/2, (height*0.85*2-textDescent()+height*0.05)/2)
        fill(218,165,32)
        stroke(0,25,0)
    if Higlight == 2:
        fill(218,165,32)
        stroke(255)
        rect(width*0.45, height*0.85, width*0.1, height*0.05)
        textAlign(CENTER, CENTER)
        fill(255)
        textSize(height*0.05*0.6)
        text('Normaal', (width*0.45*2+width*0.1)/2, (height*0.85*2-textDescent()+height*0.05)/2)
        fill(218,165,32)
        stroke(0,25,0)
    if Higlight == 3:
        fill(218,165,32)
        stroke(255)
        rect(width*0.7, height*0.85, width*0.1, height*0.05)
        textAlign(CENTER, CENTER)
        fill(255)
        textSize(height*0.05*0.6)
        text('Moeilijk', (width*0.7*2+width*0.1)/2, (height*0.85*2-textDescent()+height*0.05)/2) 
        fill(218,165,32)
        stroke(0,25,0)



    if (mousePressed == True and (width*0.2 < mouseX < width*0.3) and (height*0.85 < mouseY < height*0.9)):
        timerDifficulty = 40
        Higlight = 1
    if (mousePressed == True and (width*0.45 < mouseX < width*0.55) and (height*0.85 < mouseY < height*0.9)):
        timerDifficulty = 30
        Higlight = 2
    if (mousePressed == True and (width*0.7 < mouseX < width*0.8) and (height*0.85 < mouseY < height*0.9)):
        timerDifficulty = 2
        Higlight = 3

    
def instructieBackV():
    global img6, currentScreen, d, timerStart, PlayerCount, seccondPlayer, playersTurn
    
    if mousePressed == True and mouseX > width * 0.34 and mouseX < width * 0.685 and mouseY > height * 0.03 and mouseY < height * 0.95 and seccondPlayer != '' and d == 0:
        background(backgroundImg)
        timerStart = datetime.now()
        currentScreen = 'random'
    else:
        if seccondPlayer == playersTurn:
            seccondPlayer = ''
        background(backgroundImg)
        image(img6, (width // 2) -300 , 30)
        fill(218,165,32)
        rect(width*0.03, height*0.302, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 0:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.302, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.302 and mouseY < height * 0.037 + height * 0.302 or seccondPlayer == 0:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.302, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.302 and mouseY < height * 0.037 + height * 0.302 and d == 0 or seccondPlayer == 0:
                seccondPlayer = 0
                d = 0
        
        
        fill(218,165,32)
        rect(width*0.03, height*0.352, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 1:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.352, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.352 and mouseY < height * 0.037 + height * 0.352 or seccondPlayer == 1:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.352, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.352 and mouseY < height * 0.037 + height * 0.341 and d == 0 or seccondPlayer == 1:
                seccondPlayer = 1
                d = 0
        
        fill(218,165,32)
        rect(width*0.03, height*0.402,width*0.2, height*0.038)
        fill(0)
        if playersTurn == 2:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.402, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.402 and mouseY < height * 0.037 + height * 0.402 or seccondPlayer == 2:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.402, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.402 and mouseY < height * 0.037 + height * 0.402 and d == 0 or seccondPlayer == 2:
                seccondPlayer = 2
                d = 0
        
        if PlayerCount >= 3:
            fill(218,165,32)
            rect(width*0.03, height*0.452, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 3:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.452, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.452 and mouseY < height * 0.037 + height * 0.452 or seccondPlayer == 3:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.452, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.452 and mouseY < height * 0.037 + height * 0.452 and d == 0 or seccondPlayer == 3:
                    seccondPlayer = 3
                    d = 0
            
        if PlayerCount >= 4:    
            fill(218,165,32)
            rect(width*0.03, height*0.502, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 4:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.502, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.502 and mouseY < height * 0.037 + height * 0.502 or seccondPlayer == 4:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.502, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.502 and mouseY < height * 0.037 + height * 0.502 and d == 0 or seccondPlayer == 4:
                    seccondPlayer = 4
                    d = 0
                
        if PlayerCount >= 5:    
            fill(218,165,32)
            rect(width*0.03, height*0.552, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 5:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.552, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.552 and mouseY < height * 0.038+ height * 0.552 or seccondPlayer == 5:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.552, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.552 and mouseY < height * 0.038 + height * 0.552 and d == 0 or seccondPlayer == 5:
                    seccondPlayer = 5
                    d = 0
            
        if PlayerCount >= 6:    
            fill(218,165,32)
            rect(width*0.03, height*0.602, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 6:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.602, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.600 and mouseY < height * 0.037 + height * 0.602 or seccondPlayer == 6:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.602, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.602 and mouseY < height * 0.037 + height * 0.602 and d == 0 or seccondPlayer == 6:
                    seccondPlayer = 6
                    d = 0
            
        
        global playersTurn
        fill(0)
        rectMode(CORNER)
        fill(218,165,32)
        stroke(0,25,0)
        rect(width*0.81, height*0.25, width*0.185, height*0.35)
        textSize(30)
        fill(0)
        textAlign(LEFT, TOP)
        for x in range(0,7):
            if playersList[x][0] != '':
                text(playersList[x][0],width * 0.05, (height * x * 0.05) + (height * 0.305))   
                
    drawMedespelerTekst() 



def instructieBack():
    global img7, currentScreen, d, timerStart, PlayerCount, seccondPlayer, playersTurn
        
    if mousePressed == True and mouseX > width * 0.34 and mouseX < width * 0.685 and mouseY > height * 0.03 and mouseY < height * 0.95 and seccondPlayer != '' and d == 0:
        background(backgroundImg)
        timerStart = datetime.now()
        currentScreen = 'random'
    
    else:
        if seccondPlayer == playersTurn:
            seccondPlayer = ''
        background(backgroundImg)
        image(img7, (width // 2) -300 , 30)
        fill(218,165,32)
        rect(width*0.03, height*0.302, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 0:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.302, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.302 and mouseY < height * 0.037 + height * 0.302 or seccondPlayer == 0:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.302, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.302 and mouseY < height * 0.037 + height * 0.302 and d == 0 or seccondPlayer == 0:
                seccondPlayer = 0
                
        
        
        fill(218,165,32)
        rect(width*0.03, height*0.352, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 1:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.352, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.352 and mouseY < height * 0.037 + height * 0.352 or seccondPlayer == 1:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.352, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.352 and mouseY < height * 0.037 + height * 0.352 and d == 0 or seccondPlayer == 1:
                seccondPlayer = 1
                
        
        fill(218,165,32)
        rect(width*0.03, height*0.402, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 2:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.402, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.402 and mouseY < height * 0.037 + height * 0.402 or seccondPlayer == 2:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.402, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.402 and mouseY < height * 0.037 + height * 0.402 and d == 0 or seccondPlayer == 2:
                seccondPlayer = 2
                
        
        if PlayerCount >= 3:
            fill(218,165,32)
            rect(width*0.03, height*0.452, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 3:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.452, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.452 and mouseY < height * 0.037 + height * 0.452 or seccondPlayer == 3:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.452, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.452 and mouseY < height * 0.037 + height * 0.452 and d == 0 or seccondPlayer == 3:
                    seccondPlayer = 3
                
            
        if PlayerCount >= 4:    
            fill(218,165,32)
            rect(width*0.03, height*0.502, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 4:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.502, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.502 and mouseY < height * 0.037 + height * 0.502 or seccondPlayer == 4:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.502, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.502 and mouseY < height * 0.037 + height * 0.502 and d == 0 or seccondPlayer == 4:
                    seccondPlayer = 4
                
                
        if PlayerCount >= 5:    
            fill(218,165,32)
            rect(width*0.03, height*0.552, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 5:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.552, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.552 and mouseY < height * 0.038+ height * 0.552 or seccondPlayer == 5:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.552, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.552 and mouseY < height * 0.038 + height * 0.552 and d == 0 or seccondPlayer == 5:
                    seccondPlayer = 5
                
            
        if PlayerCount >= 6:    
            fill(218,165,32)
            rect(width*0.03, height*0.602, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 6:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.602, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.600 and mouseY < height * 0.037 + height * 0.602 or seccondPlayer == 6:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.602, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.602 and mouseY < height * 0.037 + height * 0.602 and d == 0 or seccondPlayer == 6:
                    seccondPlayer = 6
                
            
        
        global playersTurn
        fill(0)
        rectMode(CORNER)
        fill(218,165,32)
        stroke(0,25,0)
        rect(width*0.81, height*0.25, width*0.185, height*0.35)
        textSize(30)
        fill(0)
        textAlign(LEFT, TOP)
        for x in range(0,7):
            if playersList[x][0] != '':
                text(playersList[x][0],width * 0.05, (height * x * 0.050) + (height * 0.305)) 
                
        drawMedespelerTekst()   

        
def droomBack():
    global img8, currentScreen, d, timerStart, Save, PlayerCount, seccondPlayer, playersTurn
    drawMedespelerTekst()
    
    if mousePressed == True and mouseX > width * 0.34 and mouseX < width * 0.685 and mouseY > height * 0.03 and mouseY < height * 0.95 and seccondPlayer != '' and d == 0:
        d = 1
        background(backgroundImg)
        timerStart = datetime.now()
        Save = False
        currentScreen = 'droomCards'
    else:
        if seccondPlayer == playersTurn:
            seccondPlayer = ''
        background(backgroundImg)
        image(img8, (width // 2) -300 , 30)
        fill(218,165,32)
        rect(width*0.03, height*0.302, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 0:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.302, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.302 and mouseY < height * 0.037 + height * 0.302 or seccondPlayer == 0:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.302, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.302 and mouseY < height * 0.037 + height * 0.302 and d == 0 or seccondPlayer == 0:
                seccondPlayer = 0
                
        
        
        fill(218,165,32)
        rect(width*0.03, height*0.352, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 1:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.352, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.352 and mouseY < height * 0.037 + height * 0.352 or seccondPlayer == 1:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.352, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.352 and mouseY < height * 0.037 + height * 0.352 and d == 0 or seccondPlayer == 1:
                seccondPlayer = 1
                
        
        fill(218,165,32)
        rect(width*0.03, height*0.402, width*0.2, height*0.038)
        fill(0)
        if playersTurn == 2:
            fill(200)
            stroke(0)
            rect(width*0.03, height*0.402, width*0.2, height*0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.402 and mouseY < height * 0.037 + height * 0.402 or seccondPlayer == 2:
                fill(218,165,32)
                stroke(255)
                rect(width*0.03, height*0.402, width*0.2, height*0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.402 and mouseY < height * 0.037 + height * 0.402 and d == 0 or seccondPlayer == 2:
                seccondPlayer = 2
                
        
        if PlayerCount >= 3:
            fill(218,165,32)
            rect(width*0.03, height*0.452, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 3:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.452, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.452 and mouseY < height * 0.037 + height * 0.452 or seccondPlayer == 3:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.452, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.452 and mouseY < height * 0.037 + height * 0.452 and d == 0 or seccondPlayer == 3:
                    seccondPlayer = 3
                    
            
        if PlayerCount >= 4:    
            fill(218,165,32)
            rect(width*0.03, height*0.502, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 4:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.502, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.502 and mouseY < height * 0.037 + height * 0.502 or seccondPlayer == 4:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.502, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.502 and mouseY < height * 0.037 + height * 0.502 and d == 0 or seccondPlayer == 4:
                    seccondPlayer = 4
                    
                
        if PlayerCount >= 5:    
            fill(218,165,32)
            rect(width*0.03, height*0.552, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 5:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.552, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.552 and mouseY < height * 0.038+ height * 0.552 or seccondPlayer == 5:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.552, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.552 and mouseY < height * 0.038 + height * 0.552 and d == 0 or seccondPlayer == 5:
                    seccondPlayer = 5
                    
            
        if PlayerCount >= 6:    
            fill(218,165,32)
            rect(width*0.03, height*0.602, width*0.2, height*0.038)
            fill(0)
            if playersTurn == 6:
                fill(200)
                stroke(0)
                rect(width*0.03, height*0.602, width*0.2, height*0.038)
                fill(255)
                stroke(0)
                fill(0)
            else:
                if mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.600 and mouseY < height * 0.037 + height * 0.602 or seccondPlayer == 6:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.03, height*0.602, width*0.2, height*0.038)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.03 and mouseX < width*0.2 + width *0.03 and mouseY > height*0.602 and mouseY < height * 0.037 + height * 0.602 and d == 0 or seccondPlayer == 6:
                    seccondPlayer = 6
                
            
        
        global playersTurn
        fill(0)
        rectMode(CORNER)
        fill(218,165,32)
        stroke(0,25,0)
        rect(width*0.81, height*0.25, width*0.185, height*0.35)
        textSize(30)
        fill(0)
        textAlign(LEFT, TOP)
        for x in range(0,7):
            if playersList[x][0] != '':
                text(playersList[x][0],width * 0.05, (height * x * 0.050) + (height * 0.305))    
                
    drawMedespelerTekst()


def backBabelen():
    global img9, currentScreen, d, seccondPlayer
    background(backgroundImg)
    image(img9, (width // 2) -300 , 30)
    if mousePressed == True and mouseX > width * 0.34 and mouseX < width * 0.685 and mouseY > height * 0.03 and mouseY < height * 0.95 and d == 0:
        d = 1
        currentScreen = 'babelen'

def babelen():
    global img8, currentScreen, d, timerStart, Save, PlayerCount, seccondPlayer, playersTurn, Save, clicked, addedCoins, coins, d    
    if clicked == False:
        if seccondPlayer != '':
            seccondPlayer = ''
            Save = False
        elif d == 0:
        
            if seccondPlayer == playersTurn:
                seccondPlayer = ''
            background(backgroundImg)
            fill(218,165,32)
            rect(width*0.3, height*0.290, width*0.4, height*0.056)
            fill(255)
            textAlign (CENTER, CENTER)
            textSize(55)
            text('Kies de Speler die gewonnen heeft', width / 2, height * 0.2)
            fill(0)
    
            if mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.290 and mouseY < height * 0.055 + height * 0.290 or seccondPlayer == 0:
                fill(218,165,32)
                stroke(255)
                rect(width*0.3, height*0.290, width*0.4, height*0.056)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.290 and mouseY < height * 0.055 + height * 0.290 and d == 0 or seccondPlayer == 0:
                seccondPlayer = 0
                clicked = True                
            
            
            fill(218,165,32)
            rect(width*0.3, height*0.360, width*0.4, height*0.056)
            fill(0)
            if mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.360 and mouseY < height * 0.055 + height * 0.347 or seccondPlayer == 1:
                fill(218,165,32)
                stroke(255)
                rect(width*0.3, height*0.360, width*0.4, height*0.056)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.360 and mouseY < height * 0.055 + height * 0.360 and d == 0 or seccondPlayer == 1:
                seccondPlayer = 1
                clicked = True
                
            
            fill(218,165,32)
            rect(width*0.3, height*0.430, width*0.4, height*0.056)
            fill(0)
        
            if mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.430 and mouseY < height * 0.055 + height * 0.430 or seccondPlayer == 2:
                fill(218,165,32)
                stroke(255)
                rect(width*0.3, height*0.430, width*0.4, height*0.056)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed == True and mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.430 and mouseY < height * 0.056 + height * 0.430 and d == 0 or seccondPlayer == 2:
                seccondPlayer = 2
                clicked = True
                
        
            if PlayerCount >= 3:
                fill(218,165,32)
                rect(width*0.3, height*0.500, width*0.4, height*0.056)
                fill(0)
    
                if mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.500 and mouseY < height * 0.055 + height * 0.500 or seccondPlayer == 3:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.3, height*0.500, width*0.4, height*0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.500 and mouseY < height * 0.055 + height * 0.500 and d == 0 or seccondPlayer == 3:
                    seccondPlayer = 3
                    clicked = True
                    
            
            if PlayerCount >= 4:    
                fill(218,165,32)
                rect(width*0.3, height*0.570 ,width*0.4, height*0.0565)
                fill(0)


                if mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.570 and mouseY < height * 0.055 + height * 0.570 or seccondPlayer == 4:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.3, height*0.570, width*0.4, height*0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.570 and mouseY < height * 0.055 + height * 0.570 and d == 0 or seccondPlayer == 4:
                    seccondPlayer = 4
                    clicked = True    
                    
            if PlayerCount >= 5:    
                fill(218,165,32)
                rect(width*0.3, height*0.640, width*0.4, height*0.056)
                fill(0)
    
                if mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.640 and mouseY < height * 0.055+ height * 0.640 or seccondPlayer == 5:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.3, height*0.640, width*0.4, height*0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.640 and mouseY < height * 0.055 + height * 0.640 and d == 0 or seccondPlayer == 5:
                    seccondPlayer = 5
                    clicked = True    
            
            if PlayerCount >= 6:    
                fill(218,165,32)
                rect(width*0.3, height*0.710, width*0.4, height*0.056)
                fill(0)
                if mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.710 and mouseY < height * 0.055 + height * 0.710 or seccondPlayer == 6:
                    fill(218,165,32)
                    stroke(255)
                    rect(width*0.3, height*0.710, width*0.4, height*0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed == True and mouseX > width*0.3 and mouseX < width*0.4 + width *0.3 and mouseY > height*0.710 and mouseY < height * 0.056 + height * 0.710 and d == 0 or seccondPlayer == 6:
                    seccondPlayer = 6
                    clicked = True
                    
            

            global playersTurn
            textSize(50)
            fill(0)
            textAlign(LEFT, TOP)
            for x in range(0,7):
                if playersList[x][0] != '':
                    text(playersList[x][0],width * 0.33 , (height * x * 0.0698) + (height * 0.291)) 
                    
                
    if clicked == True:
        background(backgroundImg)
        
        if addedCoins == False:
            possibleCoins = [5,10,15,20,25,50]
            coins = possibleCoins[int(random(0, 6))]
            playersList[seccondPlayer][2] = playersList[seccondPlayer][2] + coins
            addedCoins = True
            
        fill(218,165,32)
        rectMode(CENTER)
        rect(width/2,height*0.76,width*0.20,height*0.08)
            
        fill(255)
        textSize(70)
        textAlign(CENTER, CENTER)
        fill(0)
        text('Menu', width/2, height*0.75)
        
        fill(0)
        text(playersList[seccondPlayer][0] + ' je krijgt een munt van ' + str(coins) + '\nJe hebt nu ' + str(playersList[seccondPlayer][2]) + ' munten', width/2, height/2)
        
        if mousePressed == True and width*0.4 < mouseX < width*0.6 and height*0.72 < mouseY < height*0.8 and d == 0:
            currentScreen = 'hoofdmenu'
 
    
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
        instrlist = ["Gebruik niet de woorden 'links' en 'rechts'", u'Je mag geen co\u00F6rdinaten gebruiken', "Gebruik niet de woorden 'omhoog',\n'omlaag', 'boven' of 'beneden'", 
                     'gebruik geen getallen', "Gebruik Niet de woorden 'Wel'\n en 'Niet'", "Gebruik niet de woorden 'goed'\nof 'fout'", "Gebruik niet de woorden 'onder'\n en 'boven'",
                     'Gebruik geen woorden', "Gebruik niet de woorden 'ja' en 'nee'"]
        instr = instrlist.pop(int(random(0, len(instrlist))))
        Save = True
        fill(0)
    
    
    background(backgroundImg)
    image(instrImg, (width // 2) -300 , 30)
    f = 0
    o = 0
    textSize(30)
    if len(fillOrNoFill) > 14:
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
        textAlign(CENTER, CENTER)
        text(instr, width/2+ width*0.0199 ,height / 1.4 )
    timerFunc(width*0.17)        

def droomCards():
    global droomImg, d, Save, droom
    fill(0)
    textAlign(CENTER, CENTER)
    background(backgroundImg)
    image(droomImg, (width // 2) -300 , 30)

    if Save == False:
        x = int(random(0, 4))
        droomList = ['Aarde','Vuur','Water','Lucht', 'Bouwstenen', 'Constructie', 'Sloophamer', 'Opdrachten', 'Metselaar', 'Pikhouweel', 'Inspanning', 'Teamwork', 'Instorten', 'Hoogbouw', 
                     'Laagbouw', 'Straffen', 'Vertaling', 'Wereldreis', 'Hoogtevrees', 'Onduidelijk', 'Begrijpen', 'Goddelijk', 'Verhalen', 'Mythe', 'Oudheid', 'Legende', 'Zuid-Amerika', 
                     'Noord-Amerika', 'Europa', u'Azi\u00EB', u'Australi\u00EB', 'Antarctica', 'Afrika', 'Continent', 'Toendra', 'Woestijn', 'IJs', 'Zonneschijn', 'Maneschijn', 'Letters', 'Woorden']
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
    rectMode(CENTER)
    fill(218,165,32)
    rect(placement, height*0.65, width*0.12, height*0.045)
    textAlign(CENTER, CENTER)
    textSize(25)
    fill(0)
    text('Klaar', placement, height*0.645)
    if mousePressed == True and placement-width*0.06 < mouseX < placement+width*0.06 and height*0.65-height*0.0225 < mouseY < height*0.65+height*0.0225:
        timerStart = datetime.max
    

def worldMap():
    global playersTurn, gameOver
    if gameOver == True:
        currentScreen = 'gameFinished'
    if playersTurn == 0:
        antartica()
    if playersTurn == 1:
        europe()                        
    if playersTurn == 2:
        southAmerika()              
    if playersTurn == 3:
        northAmerika() 
    if playersTurn == 4:
        asia()
    if playersTurn == 5:
        australia()
    if playersTurn == 6:
        africa()
    
def europe():
    global BackgroundImg, ground10, ground15, ground20, ground50, landkaart , Europe, playersTurn, PlayersList
    background(backgroundImg)
    image(landkaart, -12, -8, width*0.82, height)
    #Europe 
    if mousePressed == True and mouseX > width * 0.28 and mouseX < width * 0.28 + 29 and mouseY > height* 0.33 and mouseY < height* 0.33 + 29 or Europe[0] == 1:
        if Europe[0] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Europe.pop(0)
            Europe.insert(0, 1) 
        if  Europe[0] != 1:
            image(ground20, width * 0.28, height* 0.33)
            
    else:
        image(ground20, width * 0.28, height* 0.33)
    
    if mousePressed == True and mouseX > width * 0.30 and mouseX < width * 0.30 + 29 and mouseY > height * 0.3 and mouseY < height* 0.3 + 29 or Europe[1] == 1:
        if Europe[1] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Europe.pop(1)
            Europe.insert(1, 1) 
        if Europe[1] != 1:
            image(ground20, width * 0.30 , height* 0.3)
    else:
        image(ground20, width * 0.30 , height* 0.3)
    
    if mousePressed == True and mouseX >width * 0.32 and mouseX <width * 0.32 + 29 and mouseY > height* 0.20 and mouseY <height* 0.20 + 29 or Europe[2] == 1:
        if Europe[2] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Europe.pop(2)
            Europe.insert(2, 1) 
        if Europe[2] != 1:
            image(ground15, width * 0.32 , height* 0.20)
    else:
        image(ground15, width * 0.32 , height* 0.20)
    
    if mousePressed == True and mouseX >width * 0.33 and mouseX < width * 0.33 + 29 and mouseY > height* 0.28 and mouseY <height* 0.28 + 29 or Europe[3] == 1:
        if Europe[3] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Europe.pop(3)
            Europe.insert(3, 1) 
        if Europe[3] != 1:
            image(ground20, width * 0.33 , height* 0.28)
    else:
        image(ground20, width * 0.33 , height* 0.28)
    
    if mousePressed == True and mouseX >width * 0.35 and mouseX < width * 0.35 + 29 and mouseY > height* 0.35 and mouseY <height* 0.35 + 29 or Europe[4] == 1:
        if Europe[4] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Europe.pop(4)
            Europe.insert(4, 1) 
        if Europe[4] != 1:
            image(ground20, width * 0.35 , height* 0.35)
    else:
        image(ground20, width * 0.35 , height* 0.35)
    
    if mousePressed == True and mouseX >width * 0.36 and mouseX < width * 0.36 + 29 and mouseY > height* 0.3 and mouseY <height* 0.3 + 29 or Europe[5] == 1:
        if Europe[5] == 0 and (int(playersList[playersTurn][2]) - int(50)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(50)
            Europe.pop(5)
            Europe.insert(5, 1) 
        if Europe[5] != 1:
            image(ground50, width * 0.36 , height* 0.3)
    else:
        image(ground50, width * 0.36 , height* 0.3)
    
    if mousePressed == True and mouseX >width * 0.37 and mouseX < width * 0.37 + 29 and mouseY > height* 0.18 and mouseY <height* 0.18 + 29 or Europe[6] == 1:
        if Europe[6] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Europe.pop(6)
            Europe.insert(6, 1) 
        if Europe[6] != 1:
            image(ground20, width * 0.37 , height* 0.18)        
    else:
        image(ground20, width * 0.37 , height* 0.18)
    
    if mousePressed == True and mouseX >width * 0.38 and mouseX < width * 0.38 + 29 and mouseY > height* 0.25 and mouseY <height* 0.25 + 29 or Europe[7] == 1:
        if Europe[7] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Europe.pop(7)
            Europe.insert(7, 1) 
        if Europe[7] != 1:
            image(ground15, width * 0.38 , height* 0.25)
    else:
        image(ground15, width * 0.38 , height* 0.25)
    
    if mousePressed == True and mouseX >width * 0.41 and mouseX < width * 0.41 + 29 and mouseY > height* 0.2 and mouseY <height* 0.2 + 29 or Europe[8] == 1:
        if Europe[8] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Europe.pop(8)
            Europe.insert(8, 1)
        if Europe [8] != 1:
            image(ground20, width * 0.41 , height* 0.2)
    else:
        image(ground20, width * 0.41 , height* 0.2)
        
        

    
    
def asia():
    global BackgroundImg, ground10, ground15, ground20, ground50, landkaart , Asia
    background(backgroundImg)
    image(landkaart, -12, -8, width*0.82, height)
    #Asia
    if mousePressed == True and mouseX > width * 0.46 and mouseX < width * 0.46+ 29 and mouseY > height* 0.33 and mouseY < height* 0.33 + 29 or Asia[0] == 1:
        if Asia[0] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Asia.pop(0)
            Asia.insert(0, 1)
        if  Asia[0] != 1:
            image(ground20, width * 0.46, height* 0.33) 
    else:
         image(ground20, width * 0.46, height* 0.33)
    
    if mousePressed == True and mouseX > width * 0.50 and mouseX < width * 0.50 + 29 and mouseY > height * 0.3 and mouseY < height* 0.3 + 29 or Asia[1] == 1:
        if Asia[1] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Asia.pop(1)
            Asia.insert(1, 1) 
        if  Asia[1] != 1:
            image(ground20, width * 0.50, height* 0.3) 
    else:
        image(ground20, width * 0.50 , height* 0.3)
    
    if mousePressed == True and mouseX >width * 0.49 and mouseX <width * 0.49 + 29 and mouseY > height* 0.20 and mouseY <height* 0.20 + 29 or Asia[2] == 1:
        if Asia[2] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Asia.pop(2)
            Asia.insert(2, 1) 
        if  Asia[2] != 1:
            image(ground15, width * 0.49, height* 0.20) 
            
    else:
        image(ground15, width * 0.49 , height* 0.20)
    
    if mousePressed == True and mouseX >width * 0.54 and mouseX < width * 0.54 + 29 and mouseY > height* 0.28 and mouseY <height* 0.28 + 29 or Asia[3] == 1:
        if Asia[3] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Asia.pop(3)
            Asia.insert(3, 1) 
        if  Asia[3] != 1:
            image(ground20, width * 0.54, height* 0.28) 
            
    else:
        image(ground20, width * 0.54 , height* 0.28)
    
    if mousePressed == True and mouseX >width * 0.41 and mouseX < width * 0.41 + 29 and mouseY > height* 0.43 and mouseY <height* 0.43 + 29 or Asia[4] == 1:
        if Asia[4] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Asia.pop(4)
            Asia.insert(4, 1) 
        if  Asia[4] != 1:
            image(ground20, width * 0.41, height* 0.43) 
    else:    
        image(ground20, width * 0.41 , height* 0.43)

    if mousePressed == True and mouseX >width * 0.51 and mouseX < width * 0.51 + 29 and mouseY > height* 0.42 and mouseY <height* 0.42 + 29 or Asia[5] == 1:
        if Asia[5] == 0 and (int(playersList[playersTurn][2]) - int(50)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(50)
            Asia.pop(5)
            Asia.insert(5, 1) 
        if  Asia[5] != 1:
            image(ground50, width * 0.51, height* 0.42) 
    else:
        image(ground50, width * 0.51 , height* 0.42)
    
    if mousePressed == True and mouseX >width * 0.56 and mouseX < width * 0.56 + 29 and mouseY > height* 0.22 and mouseY <height* 0.22 + 29 or Asia[6] == 1:
        if Asia[6] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Asia.pop(6)
            Asia.insert(6, 1)
        if  Asia[6] != 1:
            image(ground20, width * 0.56, height* 0.22)  
    else:
        image(ground20, width * 0.56 , height* 0.22)
    
    if mousePressed == True and mouseX >width * 0.47 and mouseX < width * 0.47 + 29 and mouseY > height* 0.4 and mouseY <height* 0.4 + 29 or Asia[7] == 1:
        if Asia[7] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Asia.pop(7)
            Asia.insert(7, 1) 
        if  Asia[7] != 1:
            image(ground15, width * 0.47, height* 0.4)  
    else:
        image(ground15, width * 0.47 , height* 0.4)
    
    if mousePressed == True and mouseX >width * 0.44 and mouseX < width * 0.44 + 29 and mouseY > height* 0.28 and mouseY <height* 0.28 + 29 or Asia[8] == 1:
        if Asia[8] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Asia.pop(8)
            Asia.insert(8, 1) 
        if  Asia[8] != 1:
            image(ground20, width * 0.44, height* 0.28)  
    else:
        image(ground20, width * 0.44 , height* 0.28)
    
    
def southAmerika():
    global BackgroundImg, ground10, ground15, ground20, ground50, landkaart , SouthAmerika
    background(backgroundImg)
    image(landkaart, -12, -8, width*0.82, height)
    #zuid-Amerika
    if mousePressed == True and mouseX > width * 0.17  and mouseX < width * 0.17 + 29 and mouseY > height* 0.73 and mouseY < height* 0.73 + 29 or SouthAmerika[0] == 1:
        if SouthAmerika[0] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            SouthAmerika.pop(0)
            SouthAmerika.insert(0, 1) 
        if  SouthAmerika[0] != 1:
            image(ground20, width * 0.17, height* 0.73) 
    else:
          image(ground20, width * 0.17, height* 0.73)

    
    if mousePressed == True and mouseX > width * 0.17 and mouseX < width * 0.17 + 29 and mouseY > height * 0.6 and mouseY < height* 0.6 + 29 or SouthAmerika[1] == 1:
        if SouthAmerika[1] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            SouthAmerika.pop(1)
            SouthAmerika.insert(1, 1) 
        if  SouthAmerika[1] != 1:
            image(ground20, width * 0.17, height* 0.6)
    else:
        image(ground20, width * 0.17 , height* 0.6)


    if mousePressed == True and mouseX >width * 0.12 and mouseX <width * 0.12 + 29 and mouseY > height* 0.63 and mouseY <height* 0.63 + 29 or SouthAmerika[2] == 1:
        if SouthAmerika[2] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            SouthAmerika.pop(2)
            SouthAmerika.insert(2, 1)
        if  SouthAmerika[2] != 1:
            image(ground20, width * 0.12, height* 0.63) 
    else:
        image(ground20, width * 0.12 , height* 0.63)

    
    if mousePressed == True and mouseX >width * 0.15 and mouseX < width * 0.15 + 29 and mouseY > height* 0.86 and mouseY <height* 0.86 + 29 or SouthAmerika[3] == 1:
        if SouthAmerika[3] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            SouthAmerika.pop(3)
            SouthAmerika.insert(3, 1) 
        if  SouthAmerika[3] != 1:
            image(ground15, width * 0.15, height* 0.86)
    else:
        image(ground15, width * 0.15 , height* 0.86)

    
    
    if mousePressed == True and mouseX >width * 0.16  and mouseX < width * 0.16 + 29 and mouseY > height* 0.65 and mouseY <height* 0.65 + 29 or SouthAmerika[4] == 1:
        if SouthAmerika[4] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            SouthAmerika.pop(4)
            SouthAmerika.insert(4, 1) 
        if  SouthAmerika[4] != 1:
            image(ground20, width * 0.16, height* 0.65)
    else:    
        image(ground20, width * 0.16 , height* 0.65)


    if mousePressed == True and mouseX >width * 0.14 and mouseX < width * 0.14+ 29 and mouseY > height* 0.75 and mouseY <height* 0.75 + 29 or SouthAmerika[5] == 1:
        if SouthAmerika[5] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            SouthAmerika.pop(5)
            SouthAmerika.insert(5, 1) 
        if  SouthAmerika[5] != 1:
            image(ground20, width * 0.14, height* 0.75)
    else:
        image(ground20, width * 0.14 , height* 0.75)
    
    if mousePressed == True and mouseX >width * 0.2 and mouseX < width * 0.2 + 29 and mouseY > height* 0.64 and mouseY <height* 0.64 + 29 or SouthAmerika[6] == 1:
        if SouthAmerika[6] == 0 and (int(playersList[playersTurn][2]) - int(50)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(50)
            SouthAmerika.pop(6)
            SouthAmerika.insert(6, 1) 
        if  SouthAmerika[6] != 1:
            image(ground50, width * 0.20, height* 0.64)
    else:
        image(ground50, width * 0.20, height* 0.64)

    
    if mousePressed == True and mouseX >width * 0.16 and mouseX < width * 0.16 + 29 and mouseY > height* 0.78 and mouseY <height* 0.78 + 29 or SouthAmerika[7] == 1:
        if SouthAmerika[7] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            SouthAmerika.pop(7)
            SouthAmerika.insert(7, 1) 
        if  SouthAmerika[7] != 1:
            image(ground20, width * 0.16, height* 0.78)
    else:
        image(ground20, width * 0.16 , height* 0.78)
    
    
    if mousePressed == True and mouseX >width * 0.13 and mouseX < width * 0.13 + 29 and mouseY > height* 0.56 and mouseY <height* 0.56 + 29 or SouthAmerika[8] == 1:
        if SouthAmerika[8] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            SouthAmerika.pop(8)
            SouthAmerika.insert(8, 1) 
        if  SouthAmerika[8] != 1:
            image(ground15, width * 0.13, height* 0.56)
    else:
        image(ground15, width * 0.13 , height* 0.56)

    


    
    
def africa():
    global BackgroundImg, ground10, ground15, ground20, ground50, landkaart , Africa
    background(backgroundImg)
    image(landkaart, -12, -8, width*0.82, height)
    #Africa
    if mousePressed == True and mouseX > width * 0.39 and mouseX < width * 0.39 + 29 and mouseY > height* 0.71 and mouseY < height* 0.71 + 29 or Africa[0] == 1:
        if Africa[0] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Africa.pop(0)
            Africa.insert(0, 1) 
        if Africa[0] != 1:
            image(ground20, width * 0.39, height * 0.71)
    else:
        image(ground20, width * 0.39, height* 0.71)

    
    
    if mousePressed == True and mouseX > width * 0.4 and mouseX < width * 0.4 + 29 and mouseY > height * 0.6 and mouseY < height* 0.6 + 29 or Africa[1] == 1:
        if Africa[1] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Africa.pop(1)
            Africa.insert(1, 1)
        if Africa[1] != 1:
            image(ground20, width * 0.4, height * 0.6)
        
    else:
        image(ground20, width * 0.4 , height* 0.6)


    if mousePressed == True and mouseX >width * 0.3 and mouseX <width * 0.3 + 29 and mouseY > height* 0.42 and mouseY <height* 0.42 + 29 or Africa[2] == 1:
        if Africa[2] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Africa.pop(2)
            Africa.insert(2, 1) 
        if Africa[2] != 1:
            image(ground15, width * 0.3, height * 0.42)
    else:
        image(ground15, width * 0.3 , height* 0.42)

    
    if mousePressed == True and mouseX >width * 0.37 and mouseX < width * 0.37 + 29 and mouseY > height* 0.39 and mouseY <height* 0.39 + 29 or Africa[3] == 1:
        if Africa[3] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Africa.pop(3)
            Africa.insert(3, 1) 
        if Africa[3] != 1:
            image(ground20, width * 0.37, height * 0.39)
    else:
         image(ground20, width * 0.37 , height* 0.39)
    
    
    if mousePressed == True and mouseX >width * 0.36 and mouseX < width * 0.36 + 29 and mouseY > height* 0.75 and mouseY <height* 0.75 + 29 or Africa[4] == 1:
        if Africa[4] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Africa.pop(4)
            Africa.insert(4, 1)
        if Africa[4] != 1:
            image(ground20, width * 0.36, height * 0.75) 
    else:    
        image(ground20, width * 0.36 , height* 0.75)


    if mousePressed == True and mouseX >width * 0.28 and mouseX < width * 0.28 + 29 and mouseY > height* 0.5 and mouseY <height* 0.5 + 29 or Africa[5] == 1:
        if Africa[5] == 0 and (int(playersList[playersTurn][2]) - int(50)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(50)
            Africa.pop(5)
            Africa.insert(5, 1) 
        if Africa[5] != 1:
            image(ground50, width * 0.28, height * 0.50)
    else:
        image(ground50, width * 0.28, height* 0.50)
    
    if mousePressed == True and mouseX >width * 0.35 and mouseX < width * 0.35 + 29 and mouseY > height* 0.58 and mouseY <height* 0.58 + 29 or Africa[6] == 1:
        if Africa[6] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Africa.pop(6)
            Africa.insert(6, 1) 
        if Africa[6] != 1:
            image(ground20, width * 0.35, height * 0.58)
    else:
        image(ground20, width * 0.35 , height* 0.58)

    
    if mousePressed == True and mouseX >width * 0.42 and mouseX < width * 0.42 + 29 and mouseY > height* 0.53 and mouseY <height* 0.53 + 29 or Africa[7] == 1:
        if Africa[7] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Africa.pop(7)
            Africa.insert(7, 1) 
        if Africa[7] != 1:
            image(ground15, width * 0.42, height * 0.53)
    else:
        image(ground15, width * 0.42 , height* 0.53)

    
    if mousePressed == True and mouseX >width * 0.38 and mouseX < width * 0.38 + 29 and mouseY > height* 0.49 and mouseY <height* 0.49 + 29 or Africa[8] == 1:
        if Africa[8] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Africa.pop(8)
            Africa.insert(8, 1) 
        if Africa[8] != 1:
            image(ground20, width * 0.38, height * 0.49)
    else:
        image(ground20, width * 0.38 , height* 0.49)
    
    

    
    
def northAmerika():
    global BackgroundImg, ground10, ground15, ground20, ground50, landkaart , NorthAmerika
    background(backgroundImg)
    image(landkaart, -12, -8, width*0.82, height)
    #North-Amerika
    if mousePressed == True and mouseX > width * 0.1 and mouseX < width * 0.1 + 29 and mouseY > height* 0.33 and mouseY < height* 0.33 + 29 or NorthAmerika[0] == 1:
        if NorthAmerika[0] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            NorthAmerika.pop(0)
            NorthAmerika.insert(0, 1) 
        if NorthAmerika[0] != 1:
            image(ground20, width * 0.1, height * 0.33)
    else:
         image(ground20, width * 0.1, height* 0.33)
    
    
    if mousePressed == True and mouseX > width * 0.08 and mouseX < width * 0.08 + 29 and mouseY > height * 0.37 and mouseY < height* 0.37 + 29 or NorthAmerika[1] == 1:
        if NorthAmerika[1] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            NorthAmerika.pop(1)
            NorthAmerika.insert(1, 1) 
        if NorthAmerika[1] != 1:
            image(ground20, width * 0.08, height * 0.37)
    else:
        image(ground20, width * 0.08 , height* 0.37)

    if mousePressed == True and mouseX >width * 0.08 and mouseX <width * 0.08 + 29 and mouseY > height* 0.26 and mouseY <height* 0.26 + 29 or NorthAmerika[2] == 1:
        if NorthAmerika[2] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            NorthAmerika.pop(2)
            NorthAmerika.insert(2, 1) 
        if NorthAmerika[2] != 1:
            image(ground15, width * 0.08, height * 0.26)
    else:
        image(ground15, width * 0.08 , height* 0.26)

    
    if mousePressed == True and mouseX >width * 0.19 and mouseX < width * 0.19 + 29 and mouseY > height* 0.25 and mouseY <height* 0.25 + 29 or NorthAmerika[3] == 1:
        if NorthAmerika[3] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            NorthAmerika.pop(3)
            NorthAmerika.insert(3, 1) 
        if NorthAmerika[3] != 1:
            image(ground20, width * 0.19, height * 0.25)
    else:
        image(ground20, width * 0.19 , height* 0.25)
    
    
    if mousePressed == True and mouseX >width * 0.14 and mouseX < width * 0.14 + 29 and mouseY > height* 0.35 and mouseY <height* 0.35 + 29 or NorthAmerika[4] == 1:
        if NorthAmerika[4] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            NorthAmerika.pop(4)
            NorthAmerika.insert(4, 1) 
        if NorthAmerika[4] != 1:
            image(ground20, width * 0.14, height * 0.35)
    else:    
        image(ground20, width * 0.14 , height* 0.35)


    if mousePressed == True and mouseX >width * 0.2 and mouseX < width * 0.2 + 29 and mouseY > height* 0.14 and mouseY <height* 0.14 + 29 or NorthAmerika[5] == 1:
        if NorthAmerika[5] == 0 and (int(playersList[playersTurn][2]) - int(50)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(50)
            NorthAmerika.pop(5)
            NorthAmerika.insert(5, 1) 
        if NorthAmerika[5] != 1:
            image(ground50, width * 0.20, height * 0.14)
    else:
        image(ground50, width * 0.20, height* 0.14)
    
    if mousePressed == True and mouseX >width * 0.16 and mouseX < width * 0.16 + 29 and mouseY > height* 0.18 and mouseY <height* 0.18 + 29 or NorthAmerika[6] == 1:
        if NorthAmerika[6] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            NorthAmerika.pop(6)
            NorthAmerika.insert(6, 1) 
        if NorthAmerika[6] != 1:
            image(ground20, width * 0.16, height * 0.18)
    else:
        image(ground20, width * 0.16 , height* 0.18)
    
    if mousePressed == True and mouseX >width * 0.09 and mouseX < width * 0.09 + 29 and mouseY > height* 0.44 and mouseY <height* 0.44 + 29 or NorthAmerika[7] == 1:
        if NorthAmerika[7] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            NorthAmerika.pop(7)
            NorthAmerika.insert(7, 1) 
        if NorthAmerika[7] != 1:
            image(ground15, width * 0.09, height * 0.44)
    else:
        image(ground15, width * 0.09 , height* 0.44)
    
    if mousePressed == True and mouseX >width * 0.06 and mouseX < width * 0.06 + 29 and mouseY > height* 0.17 and mouseY <height* 0.17 + 29 or NorthAmerika[8] == 1:
        if NorthAmerika[8] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            NorthAmerika.pop(8)
            NorthAmerika.insert(8, 1) 
        if NorthAmerika[8] != 1:
            image(ground20, width * 0.06, height * 0.17)
    else:
        image(ground20, width * 0.06 , height* 0.17)
                                

    
    
def antartica():
    global BackgroundImg, ground10, ground15, ground20, ground50, landkaart , Antartica
    background(backgroundImg)
    image(landkaart, -12, -8, width*0.82, height)
    #antartica
    if mousePressed == True and mouseX > width * 0.39 and mouseX < width * 0.39 + 29 and mouseY > height* 0.81 and mouseY < height* 0.81 + 29 or Antartica[0] == 1:
        if Antartica[0] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Antartica.pop(0)
            Antartica.insert(0, 1) 
        if Antartica[0] != 1:
            image(ground20, width * 0.39, height * 0.81)
    else:
         image(ground20, width * 0.39, height* 0.81)
     
    
    if mousePressed == True and mouseX > width * 0.49 and mouseX < width * 0.49 + 29 and mouseY > height * 0.78 and mouseY < height* 0.78 + 29 or Antartica[1] == 1:
        if Antartica[1] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Antartica.pop(1)
            Antartica.insert(1, 1) 
        if Antartica[1] != 1:
            image(ground20, width * 0.49, height * 0.78)
    else:
        image(ground20, width * 0.49 , height* 0.78)

    if mousePressed == True and mouseX >width * 0.27 and mouseX <width * 0.27 + 29 and mouseY > height* 0.83 and mouseY <height* 0.83 + 29 or Antartica[2] == 1:
        if Antartica[2] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Antartica.pop(2)
            Antartica.insert(2, 1) 
        if Antartica[2] != 1:
            image(ground15, width * 0.27, height * 0.83)
    else:
        image(ground15, width * 0.27 , height* 0.83)
   

    
    if mousePressed == True and mouseX >width * 0.22 and mouseX < width * 0.22 + 29 and mouseY > height* 0.89 and mouseY <height* 0.89 + 29 or Antartica[3] == 1:
        if Antartica[3] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Antartica.pop(3)
            Antartica.insert(3, 1) 
        if Antartica[3] != 1:
            image(ground20, width * 0.22, height * 0.89)
    else:
        image(ground20, width * 0.22 , height* 0.89)

    
    
    if mousePressed == True and mouseX >width * 0.36 and mouseX < width * 0.36 + 29 and mouseY > height* 0.85 and mouseY <height* 0.85 + 29 or Antartica[4] == 1:
        if Antartica[4] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Antartica.pop(4)
            Antartica.insert(4, 1) 
        if Antartica[4] != 1:
            image(ground20, width * 0.36, height * 0.85)
    else:    
        image(ground20, width * 0.36 , height* 0.85)


    if mousePressed == True and mouseX >width * 0.64 and mouseX < width * 0.64 + 29 and mouseY > height* 0.8 and mouseY <height* 0.8 + 29 or Antartica[5] == 1:
        if Antartica[5] == 0 and (int(playersList[playersTurn][2]) - int(50)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(50)
            Antartica.pop(5)
            Antartica.insert(5, 1) 
        if Antartica[5] != 1:
            image(ground50, width * 0.64, height * 0.80)
    else:
        image(ground50, width * 0.64, height* 0.80)
    
    if mousePressed == True and mouseX >width * 0.6 and mouseX < width * 0.6 + 29 and mouseY > height* 0.9 and mouseY <height* 0.9 + 29 or Antartica[6] == 1:
        if Antartica[6] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Antartica.pop(6)
            Antartica.insert(6, 1) 
        if Antartica[6] != 1:
            image(ground20, width * 0.60, height * 0.9)
    else:
         image(ground20, width * 0.60 , height* 0.9)
 
    
    if mousePressed == True and mouseX >width * 0.54 and mouseX < width * 0.54 + 29 and mouseY > height* 0.86 and mouseY <height* 0.86 + 29 or Antartica[7] == 1:
        if Antartica[7] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Antartica.pop(7)
            Antartica.insert(7, 1) 
        if Antartica[7] != 1:
            image(ground20, width * 0.54, height * 0.86)
    else:
        image(ground15, width * 0.54 , height* 0.86)

    
    if mousePressed == True and mouseX >width * 0.45 and mouseX < width * 0.45 + 29 and mouseY > height* 0.89 and mouseY <height* 0.89+ 29 or Antartica[8] == 1:
        if Antartica[8] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Antartica.pop(8)
            Antartica.insert(8, 1) 
        if Antartica[8] != 1:
            image(ground20, width * 0.45, height * 0.89)
    else:
        image(ground20, width * 0.45 , height* 0.89)
  
    
    
    
    
def australia():
    global BackgroundImg, ground10, ground15, ground20, ground50, landkaart , Australia
    background(backgroundImg)
    image(landkaart, -12, -8, width*0.82, height)
    #Australie
    if mousePressed == True and mouseX > width * 0.63 and mouseX < width * 0.63 + 29 and mouseY > height* 0.7 and mouseY < height* 0.7 + 29 or Australia[0] == 1:
        if Australia[0] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Australia.pop(0)
            Australia.insert(0, 1) 
        if Australia[0] != 1:
            image(ground20, width * 0.63, height * 0.7)
    else:
        image(ground20, width * 0.63, height* 0.7)
    
    
    if mousePressed == True and mouseX > width * 0.61 and mouseX < width * 0.61 + 29 and mouseY > height * 0.67 and mouseY < height* 0.67 + 29 or Australia[1] == 1:
        if Australia[1] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Australia.pop(1)
            Australia.insert(1, 1) 
        if Australia[1] != 1:
            image(ground20, width * 0.61, height * 0.67)
    else:
        image(ground20, width * 0.61 , height* 0.67)

    if mousePressed == True and mouseX >width * 0.68 and mouseX <width * 0.68 + 29 and mouseY > height* 0.57 and mouseY <height* 0.57 + 29 or Australia[2] == 1:
        if Australia[2] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Australia.pop(2)
            Australia.insert(2, 1) 
        if Australia[2] != 1:
            image(ground15, width * 0.68, height * 0.57)
    else:
        image(ground15, width * 0.68 , height* 0.57)

    
    if mousePressed == True and mouseX >width * 0.64 and mouseX < width * 0.64 + 29 and mouseY > height* 0.64 and mouseY <height* 0.64 + 29 or Australia[3] == 1:
        if Australia[3] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Australia.pop(3)
            Australia.insert(3, 1) 
        if Australia[3] != 1:
            image(ground20, width * 0.64, height * 0.64)
    else:
        image(ground20, width * 0.64 , height* 0.64)

    
    
    if mousePressed == True and mouseX >width * 0.72 and mouseX < width * 0.72 + 29 and mouseY > height* 0.72 and mouseY <height* 0.72 + 29 or Australia[4] == 1:
        if Australia[4] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Australia.pop(4)
            Australia.insert(4, 1) 
        if Australia[4] != 1:
            image(ground20, width * 0.72, height * 0.72)
    else:    
        image(ground20, width * 0.72 , height* 0.72)


    if mousePressed == True and mouseX >width * 0.72 and mouseX < width * 0.72 + 29 and mouseY > height* 0.6 and mouseY <height* 0.6 + 29 or Australia[5] == 1:
        if Australia[5] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(50)
            Australia.pop(5)
            Australia.insert(5, 1) 
        if Australia[5] != 1:
            image(ground50, width * 0.72, height * 0.6)
    else:
        image(ground50, width * 0.72 , height* 0.6)
    
    if mousePressed == True and mouseX >width * 0.69 and mouseX < width * 0.69 + 29 and mouseY > height* 0.64 and mouseY <height* 0.64 + 29 or Australia[6] == 1:
        if Australia[6] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Australia.pop(6)
            Australia.insert(6, 1) 
        if Australia[6] != 1:
            image(ground20, width * 0.69, height * 0.64)
    else:
         image(ground20, width * 0.69 , height* 0.64)

 
    
    if mousePressed == True and mouseX >width * 0.69 and mouseX < width * 0.69 + 29 and mouseY > height* 0.74 and mouseY <height* 0.74 + 29 or Australia[7] == 1:
        if Australia[7] == 0 and (int(playersList[playersTurn][2]) - int(15)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(15)
            Australia.pop(7)
            Australia.insert(7, 1) 
        if Australia[7] != 1:
            image(ground15, width * 0.69, height * 0.74)
    else:
        image(ground15, width * 0.69 , height* 0.74)

    
    if mousePressed == True and mouseX >width * 0.7 and mouseX < width * 0.7 + 29 and mouseY > height* 0.68 and mouseY <height* 0.68+ 29 or Australia[8] == 1:
        if Australia[8] == 0 and (int(playersList[playersTurn][2]) - int(20)) >= 0:
            playersList[playersTurn][2] = int(playersList[playersTurn][2]) - int(20)
            Australia.pop(8)
            Australia.insert(8, 1) 
        if Australia[8] != 1:
            image(ground20, width * 0.7, height * 0.68)
    else:
        image(ground20, width * 0.7 , height* 0.68)



def checkIfGameFinished():
    global Europe, NorthAmerika, SouthAmerika, Africa, Asia, Antartica, Australia, gameWinner, gameOver, currentScreen
    if Antartica == [1,1,1,1,1,1,1,1,1]:
        gameWinner = 0
        gameOver = True
        currentScreen = 'gameFinished'
    elif Europe == [1,1,1,1,1,1,1,1,1]:
        gameWinner = 1
        gameOver = True
        currentScreen = 'gameFinished'
    elif SouthAmerika == [1,1,1,1,1,1,1,1,1]:
        gameWinner = 2
        gameOver = True
        currentScreen = 'gameFinished'
    elif NorthAmerika == [1,1,1,1,1,1,1,1,1]:
        gameWinner = 3
        gameOver = True
        currentScreen = 'gameFinished'
    elif Asia == [1,1,1,1,1,1,1,1,1]:
        gameWinner = 4
        gameOver = True
        currentScreen = 'gameFinished'
    elif Australia == [1,1,1,1,1,1,1,1,1]:
        gameWinner = 5
        gameOver = True 
        currentScreen = 'gameFinished'
    elif Africa == [1,1,1,1,1,1,1,1,1]:
        gameWinner = 6
        gameOver = True
        currentScreen = 'gameFinished'


def gameFinished():
    global gameWinner, playersList
    background(backgroundImg)
    textAlign(CENTER, CENTER)
    textSize(70)
    fill(255)
    text(playersList[gameWinner][0] + ' (' + playersList[gameWinner][1] + ') \n' + 'heeft de Verwarring van Babel gewonnen!', width/2, height/2)
    fill(218,165,32)
    rectMode(CENTER)
    rect(width/2, height*0.8, width * 0.35, height * 0.13)
    
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(60)
    text('Speel opnieuw!', width/2, height * 0.8) 
    if (mousePressed == True and (width * 0.3 < mouseX < width * 0.7) and (height * 0.725 < mouseY < height * 0.875)):
        setup()
    
    
def clock():
    noSmooth()
    textSize(50)
    fill(255)
    textAlign(RIGHT, BOTTOM)    
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    text(current_time, width-20, height-20)
    
def drawMedespelerTekst():
    fill(255)
    textSize(40)
    textAlign(LEFT, TOP)
    text('Kies je medespeler', width*0.03, height*0.22)
    

def keyReleased():
    global currentPlayer, playerList, currentScreen, PlayerCount
    if currentScreen == 'inputNames':
        if key in allowedCharacters and len(playersList[currentPlayer][0]) <= 8:
            playersList[currentPlayer][0] += key
        elif key == BACKSPACE:                        
            playersList[currentPlayer][0] = playersList[currentPlayer][0][:-1]
        elif key == ENTER and playersList[currentPlayer][0] != '':
            PlayerCount += 1
            if currentPlayer == 6:
                currentScreen = 'hoofdmenu'
            else:
                currentPlayer += 1
        
            
def keyPressed():    
    global currentScreen, d, timerStart
    d = 0
    print(keyCode) 
    if key == 'a' and currentScreen == 'instructieBack':
        mouseWidth = float(mouseX) / float(width)
        mouseHeight = float(mouseY) / float(height)
        print(str(mouseWidth), str(mouseHeight))
    
def mouseReleased():
    global d, currentScreen
    d = 0 
    if (currentScreen == 'inputNames' and (width*0.375 < mouseX < width*0.625) and (height/2*1.3 < mouseY < height/2*1.3+0.05*height) and playersList[2][0] != ''):
        currentScreen = 'hoofdmenu'
