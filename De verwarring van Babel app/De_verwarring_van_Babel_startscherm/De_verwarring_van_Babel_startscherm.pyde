def setup():
    global img, img2, img3, img4, img5,backgroundImg
    size (1920,1080)
    img = loadImage("startscherm1.jpg")
    img2 = loadImage("starttekst.png")
    img3 = loadImage("logo.png")
    img4 = loadImage("buttonstart.png")
    img5 = loadImage("buttonstarthigh.png")
    
    fullScreen()
    backgroundImg = loadImage("startscherm1.jpg")
    backgroundImg.resize(width, height)

     
def draw():
  background(backgroundImg)

  image(img2,280,10,720,576)
  image(img3,720,200,150,170)
  image(img4,420, 390, 500, 350)

  if (mousePressed == True and mouseX > 500 and mouseX < 820 and mouseY > 500 and mouseY < 600):
        image(img5,420, 390, 500, 350)
        
        

            
        
        
  else:
        fill(255)   # Black
        loop()
        

  
    
