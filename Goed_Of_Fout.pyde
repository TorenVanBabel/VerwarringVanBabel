
import random

def setup():
    global img,backgroundImg,b,img2,img3,punten
    size(800,800)
    img = loadImage('startscherm1.jpg')
    img2 = loadImage('TextBalkGoed.png')
    img3 = loadImage('TextBalkFout.png')
    punten = 0
    
    
    fullScreen()
    backgroundImg= loadImage('startscherm1.jpg')
    backgroundImg.resize(width,height)
    background(backgroundImg)
    regularFont = createFont('Felix Titling', 70)
    textFont(regularFont)
    b = 0

    
    
def draw():
    global goed,fout,img2,img3

    #rectMode(CENTER)
    # fill(0,255,0)
    #goed=rect((380),550,400,200)
    #fill(255,0,0)
    #fout=rect((1150),550,400,200)
    image(img2,330,500,500,300)
    image(img3,1100,510,500,290)
    GoedOfFoutClick()

    
    PuntenOpSoming()
    
    
def GoedOfFoutClick():
    global goed,fout
    #goed=((280),600,400,200)
    #fout=((1050),600,400,200)
    fill(0)
    stroke(100,100,100)
    textAlign(CENTER)
    textSize(80)
    if mousePressed == True and mouseX > 380 and mouseX < 780 and mouseY >550 and mouseY<750:
        text('Yes!\nJe krijgt een munt',width/2,100)
    elif mousePressed == True and mouseX > 1050 and mouseX < 1450 and mouseY > 550 and mouseY <750:
        text('Jammer volgende Ronde beter',width/2,900)
    else:
        pass
        
        
        
def PuntenOpSoming():
    global b,goed,fout,punten,rc1
    fill(200)
    l = ['5','10','15','20','25','50']
    b = (random.choice(l))
    textSize(40)
    text(str(punten),1700,100,100,100)
    
    if mousePressed == True and mouseX > 380 and mouseX < 780 and mouseY >550 and mouseY<750:
        print('good')
        #text('Yes!\nJe krijgt een munt',width/2,100)
        punten = int(punten) + int(b)
        fill(200,150,0)
        rect(1600,100,300,110)
        print (b)
        fill(0)
        text(b+'+',1750,180)
        print(punten)
        
        
        
        
        
