from datetime import time, datetime
import time


def setup():
    # Sets required global variables
    global current_screen, timer_difficulty, timer_start, seconds_passed, regular_font, d, player_list
    global allowed_characters, current_player, verwarring, added_coins, highlight, fill_or_no_fill
    global background_img, instructie_img, droom_img, start_img, wereldkaart_img, starttekst_img, startbutton_img
    global startbutton2_img, instructie_achterkant_img, instructie_achterkant2_img, continent_achterkant_img, logo_img
    global babelspel_img, goed_img, fout_img, punten, ground10_img, ground15_img, ground20_img, ground50_img
    global europa, noord_amerika, zuid_amerika, afrika, azie, antarctica, australie, player_turn, save
    global player_count, game_winner, game_over, second_player, clicked

    player_list = [['', 'Antarctica', 0], ['', 'Europa', 0], ['', 'Zuid-Amerika', 0], ['', 'Noord-Amerika', 0],
                   ['', u'Azi\u00EB', 0], ['', u'Australi\u00EB', 0], ['', 'Afrika', 0]]
    allowed_characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

    fill_or_no_fill = ''
    game_over = False
    current_player = 0
    clicked = False
    verwarring = False
    current_screen = 'start'
    timer_start = datetime.now()
    timer_difficulty = 30
    added_coins = False
    seconds_passed = 0
    d = 0
    highlight = 0
    punten = 0
    save = False

    # Houdt bij welke speler aan de beurt is
    second_player = ''
    player_count = -1
    player_turn = 0

    # Maakt lege list voor elk continent
    europa = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    noord_amerika = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zuid_amerika = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    afrika = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    azie = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    antarctica = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    australie = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Laadt meeste veelgebruikte afbeeldingen
    start_img = loadImage("startscherm1.jpg")
    starttekst_img = loadImage("starttekst.png")
    logo_img = loadImage("logo.png")
    startbutton_img = loadImage("buttonstart.png")
    startbutton2_img = loadImage("buttonstarthigh.png")

    instructie_achterkant_img = loadImage("InstructieAchter.jpeg")
    instructie_achterkant2_img = loadImage("InstructieAchter2.jpeg")
    continent_achterkant_img = loadImage("continentkaartAchter.jpeg")
    babelspel_img = loadImage("Babelspel.jpeg")

    goed_img = loadImage('TextBalkGoedGoedgoed.png')
    fout_img = loadImage('TextBalkFoutGoedgoed.png')

    instructie_img = loadImage('instructie.jpeg')
    droom_img = loadImage('droom.jpeg')

    # Laadt afbeeldingen wereldkaart
    ground10_img = loadImage('Grondstuk10.png')
    ground15_img = loadImage('Grondstuk15.png')
    ground20_img = loadImage('Grondstuk20.png')
    ground50_img = loadImage('50.jpeg')
    wereldkaart_img = loadImage('landkaart2.png')

    # Stelt de standaard visuele instelling in
    fullScreen()
    background_img = loadImage('startscherm1.jpg')
    background_img.resize(width, height)
    regular_font = createFont('Felix Titling', 50)
    textFont(regular_font)
    fill(0)
    textAlign(CENTER, CENTER)
    background(background_img)


# Tekent elke frame het scherm door verwijzing naar de juiste functies op basis van de variabele current_screen
def draw():
    global d, current_screen, save, random_list, fill_or_no_fill, verwarring, added_coins, clicked

    if not (current_screen == 'babelen' or current_screen == 'GoodOrBad'):
        added_coins = False
        clicked = False

    # Tekent startscherm
    if current_screen == 'start':
        startmenu()
        difficultyButtons()

    # Tekent hoofdmenuscherm
    elif current_screen == 'hoofdmenu':
        hoofdmenu()

    elif current_screen == 'inputNames':
        input_names()

    # Tekent niet omgedraaide instructiekaart
    elif current_screen == 'instructieBack':
        verwarring = False
        instructie_back()

    # Tekent niet omgedraaide instructiekaart met verwarring
    elif current_screen == 'instructieBackV':
        verwarring = True
        instructie_back_v()

    # Tekent instructiekaart
    elif current_screen == 'random':
        instructie()

    # Tekent niet omgedraaide droomkaart
    elif current_screen == 'droomBack':
        continent_back()

    # Tekent omgedraaide droomkaart
    elif current_screen == 'droomCards':
        droom_cards()

    # Tekent niet omgedraaide babelkaart
    elif current_screen == 'backBabelen':
        babelen_back()

    # Tekent omgedraaide babelkaart
    elif current_screen == 'babelen':
        babelen()

    # Tekent goed/fout afgerond scherm
    elif current_screen == 'GoodOrBad':
        goed_of_fout_click()

    # Tekent wereldkaart
    elif current_screen == 'worldMap':
        check_if_game_is_finished()
        wereldkaart()

    # Tekent eindscherm
    elif current_screen == 'gameFinished':
        game_finished()

    # Tekent menuknop op aantal schermen
    if not (current_screen == 'start' or current_screen == 'hoofdmenu' or current_screen == 'inputNames' or
            current_screen == 'gameFinished' or current_screen == 'droomCards' or current_screen == 'random' or
            current_screen == 'GoodOrBad' or (current_screen == 'babelen' and added_coins)):
        main_menu_button()

    # Tekent scorebord op aantal schermen
    if not (current_screen == 'inputNames' or current_screen == 'start' or current_screen == 'gameFinished' or
            current_screen == 'GoodOrBad' or (current_screen == 'babelen' and added_coins)):
        show_names()

    # Tekent klok op alle schermen
    clock()


# Tekent startscherm
def startmenu():
    global start_img, starttekst_img, logo_img, startbutton_img, startbutton2_img, current_screen, d, highlight
    image(background_img, 0, 0, width, height)
    image(starttekst_img, width * 0.3, height * 0.1, width * 0.38, height * 0.5)
    image(logo_img, width * 0.53, height * 0.28, width * 0.08, height * 0.15)
    image(startbutton_img, width * 0.36, height * 0.42, width * 0.26, height * 0.32)

    textAlign(CENTER)
    fill(255)
    textSize(70)
    text('Kies de moeilijkheidsgraad', width / 2, height * 0.8)

    # Geeft startknop functionaliteit
    if width * 0.41 < mouseX < width * 0.57 and height * 0.529 < mouseY < height * 0.615:
        d = 1
        image(startbutton2_img, width * 0.36, height * 0.42, width * 0.26, height * 0.32)
        if mousePressed and highlight != 0:
            current_screen = 'inputNames'


# Tekent en geeft functionaliteit aan scherm namen invullen
def input_names():
    global current_player
    background(background_img)
    rectMode(CENTER)
    fill(255)
    rect(width * 0.5, height * 0.55, width * 0.35, height * 0.075)

    textAlign(CENTER, CENTER)
    textSize(65)
    fill(0)
    text("Vul de namen van de spelers in en gebruik \n'enter' om naar de volgende speler te gaan", width * 0.5,
         height * 0.2)
    text('Naam speler ' + str(current_player + 1) + ' (' + player_list[current_player][1] + ')', width * 0.5,
         height * 0.4)
    text(player_list[current_player][0], width * 0.5, height * 0.54)
    main_menu_button_names()


# Tekent en geeft functionaliteit aan menuknop inputnames scherm
def main_menu_button_names():
    global current_screen, save, d, player_count, current_player
    button_coord_x = width * 0.375
    button_coord_y = height * 0.65
    button_size_x = 0.25 * width
    button_size_y = 0.05 * height
    rectMode(CORNER)
    if player_list[2][0] != '':
        fill(218, 165, 32)
    else:
        fill(200)
    stroke(0, 25, 0)
    rect(button_coord_x, button_coord_y, button_size_x, button_size_y)

    textAlign(CENTER, CENTER)
    fill(0)
    textSize(button_size_y * 0.6)
    text('Klaar', width * 0.5, (button_coord_y * 2 + button_size_y) / 2 - textDescent())
    if (mousePressed and (button_coord_x < mouseX < button_coord_x + button_size_x) and (
            button_coord_y < mouseY < button_coord_y + button_size_y) and player_list[2][0] != ''):
        if player_list[current_player][0] != '':
            player_count += 1
        d = 1
        current_screen = 'hoofdmenu'
        save = False


# Tekent hoofdmenu
def hoofdmenu():
    global font, font2, imgLogo, d, current_screen, timer_start, instructie_achterkant_img, instructie_achterkant2_img
    global continent_achterkant_img, babelspel_img, player_turn, player_count, save
    current_screen = 'hoofdmenu'
    background(background_img)

    fill(218, 165, 32)
    stroke(0, 25, 0)
    rectMode(CENTER)

    textSize(60)
    fill(0)
    textAlign(CENTER)
    text("Klik op de kleur van het vakje waar je op staat", width * 0.5, 220)

    # Plaatst kaarten op scherm
    image(instructie_achterkant_img, 30, 250, 350, 550)
    image(instructie_achterkant2_img, 410, 250, 350, 550)
    image(continent_achterkant_img, 790, 250, 350, 550)
    image(babelspel_img, 1170, 250, 350, 550)

    # Maakt kaarten klikbaar
    if mousePressed and 29 < mouseX < 381 and 249 < mouseY < 801 and d == 0:
        d = 1
        save = False
        current_screen = 'instructieBackV'
        timer_start = datetime.now()
        background(background_img)
    if mousePressed and 409 < mouseX < 761 and 249 < mouseY < 801 and d == 0:
        d = 1
        save = False
        current_screen = 'instructieBack'
        timer_start = datetime.now()
        background(background_img)
    if mousePressed and 789 < mouseX < 1141 and 249 < mouseY < 801 and d == 0:
        d = 1
        save = False
        current_screen = 'droomBack'
        timer_start = datetime.now()
        background(background_img)
    if mousePressed and 1169 < mouseX < 1521 and 249 < mouseY < 801 and d == 0:
        d = 1
        save = False
        current_screen = 'backBabelen'
        timer_start = datetime.now()
        background(background_img)

    # Tekent volgende speler knop
    rectMode(CORNER)
    fill(218, 165, 32)
    rect(width * 0.015, height * 0.80, width * 0.38, height * 0.07)
    fill(0)
    if width * 0.015 < mouseX < width * 0.395 and height * 0.8 < mouseY < height * 0.87:
        fill(218, 165, 32)
        stroke(255)
        rect(width * 0.015, height * 0.80, width * 0.38, height * 0.07)
        fill(255)
        stroke(0)

    textSize(43)
    textAlign(LEFT)
    text('Volgende speler ', width * 0.03, height * 0.85, )
    fill(0)
    circle(width * 0.347, height * 0.835, 50)

    # Geeft volgende speler knop functionaliteit
    if mousePressed and width * 0.015 < mouseX < width * 0.395 and height * 0.8 < mouseY < height * 0.87 and d == 0:
        if player_turn < player_count:
            player_turn += 1
        else:
            player_turn = 0
        d = 1

    # Tekent wereldkaart knop
    fill(218, 165, 32)
    rect(width * 0.41, height * 0.80, width * 0.38, height * 0.07)
    fill(0)
    if width * 0.41 < mouseX < width * 0.79 and height * 0.8 < mouseY < height * 0.87:
        fill(218, 165, 32)
        stroke(255)
        rect(width * 0.41, height * 0.80, width * 0.38, height * 0.07)
        fill(255)
        stroke(0)
    text('Wereldkaart ', width * 0.42, height * 0.85, )
    fill(0)
    circle(width * 0.347, height * 0.835, 50)

    # Geeft wereldkaart knop functionaliteit
    if mousePressed and width * 0.41 < mouseX < width * 0.79 and height * 0.8 < mouseY < height * 0.87 and d == 0:
        d = 0
        current_screen = 'worldMap'


# Tekent scoreboard
def show_names():
    global player_turn
    rectMode(CORNER)
    fill(218, 165, 32)
    stroke(0, 25, 0)
    rect(width * 0.81, height * 0.25, width * 0.185, height * 0.35)
    textSize(30)
    fill(0)
    textAlign(LEFT, TOP)
    text('Spelers:', width * 0.82, height * 0.25)
    text('Munten:', width * 0.92, height * 0.25)
    for x in range(0, 7):
        if player_list[x][0] != '':
            if player_turn == x:
                fill(255)
            text(player_list[x][0], width * 0.82, (height * x * 0.04) + (height * 0.3))
            text(str(player_list[x][2]), width * 0.93, (height * x * 0.04) + (height * 0.3))
            fill(0)


# Tekent en geeft functionaliteit aan menu knop
def main_menu_button():
    global current_screen, save
    button_coord_x = width * 0.85
    button_coord_y = 50
    button_size_x = 0.1 * width
    button_size_y = 0.05 * height
    rectMode(CORNER)
    fill(218, 165, 32)
    stroke(0, 25, 0)
    rect(button_coord_x, button_coord_y, button_size_x, button_size_y)
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(button_size_y * 0.6)
    text('Menu', (button_coord_x * 2 + button_size_x) / 2, (button_coord_y * 2 - textDescent() + button_size_y) / 2)
    if (mousePressed and (button_coord_x < mouseX < button_coord_x + button_size_x) and (
            button_coord_y < mouseY < button_coord_y + button_size_y)):
        current_screen = 'hoofdmenu'
        save = False


# Tekent afgerond/niet afgerond scherm
def goed_of_fout_click():
    global goed_img, fout_img, b, b1, punten, d, background_img, save, added_coins, current_screen, player_turn
    global player_count, l, second_player

    background(background_img)
    if not save:
        image(goed_img, width * 0.16, height * 0.4, width * 0.25, height * 0.2)
        image(fout_img, width * 0.6, height * 0.4, width * 0.25, height * 0.2)
    fill(0)
    stroke(0)
    textAlign(CENTER)
    textSize(80)
    l = ['5', '10', '15', '20', '25', '50']
    textSize(40)
    if save:
        fill(218, 165, 32)
        rectMode(CENTER)
        rect(width / 2, height * 0.8, width * 0.20, height * 0.08)

        fill(255)
        textSize(50)
        textAlign(CENTER, CENTER)
        fill(0)
        text('Menu', width * 0.5, height * 0.79)

        fill(255)
        text(player_list[player_turn][0] + ' je krijgt een munt van ' + str(b) + '\nJe hebt nu ' + str(
            player_list[player_turn][2]) + ' munten', width / 2, height * 0.2)
        text(player_list[second_player][0] + ' je krijgt een munt van ' + str(b1) + '\nJe hebt nu ' + str(
            player_list[second_player][2]) + ' munten', width / 2, height * 0.4)
        text('Leg een bouwblokje neer op het bord', width / 2, height * 0.6)

        if mousePressed and width * 0.4 < mouseX < width * 0.6 and height * 0.76 < mouseY < height * 0.84 and d == 0:
            current_screen = 'hoofdmenu'

    elif mousePressed and width * 0.161 < mouseX < width * 0.407 and height * 0.404 < mouseY < height * 0.598 and \
            d == 0:
        b = int(random(0, 6))
        b1 = int(random(0, 6))
        b = l[b]
        b1 = l[b1]
        save = True
        if added_coins == False:
            player_list[second_player][2] = int(player_list[second_player][2]) + int(b1)
            player_list[player_turn][2] = int(player_list[player_turn][2]) + int(b)
            added_coins = True

    elif mousePressed == True and width * 0.6 < mouseX < width * 0.85 and height * 0.4 < mouseY < height * 0.6 and \
            d == 0 and save == False:
        d = 1
        current_screen = 'hoofdmenu'

    if current_screen == 'hoofdmenu':
        second_player = ''
        if player_turn < player_count:
            player_turn += 1
        else:
            player_turn = 0
        d = 1


# Tekent en geeft functionaliteit aan moeilijkheidsknoppen startscherm
def difficultyButtons():
    global current_screen, timer_difficulty, highlight
    rectMode(CORNER)
    fill(218, 165, 32)
    stroke(0, 25, 0)
    rect(width * 0.2, height * 0.85, width * 0.1, height * 0.05)
    rect(width * 0.45, height * 0.85, width * 0.1, height * 0.05)
    rect(width * 0.7, height * 0.85, width * 0.1, height * 0.05)
    textAlign(CENTER, CENTER)
    fill(0)
    textSize(height * 0.05 * 0.6)
    text('Makkelijk', (width * 0.2 * 2 + width * 0.1) / 2, (height * 0.85 * 2 - textDescent() + height * 0.05) / 2)
    text('Normaal', (width * 0.45 * 2 + width * 0.1) / 2, (height * 0.85 * 2 - textDescent() + height * 0.05) / 2)
    text('Moeilijk', (width * 0.7 * 2 + width * 0.1) / 2, (height * 0.85 * 2 - textDescent() + height * 0.05) / 2)
    if highlight == 1:
        fill(218, 165, 32)
        stroke(255)
        rect(width * 0.2, height * 0.85, width * 0.1, height * 0.05)
        textAlign(CENTER, CENTER)
        fill(255)
        textSize(height * 0.05 * 0.6)
        text('Makkelijk', (width * 0.2 * 2 + width * 0.1) / 2, (height * 0.85 * 2 - textDescent() + height * 0.05) / 2)
        fill(218, 165, 32)
        stroke(0, 25, 0)
    if highlight == 2:
        fill(218, 165, 32)
        stroke(255)
        rect(width * 0.45, height * 0.85, width * 0.1, height * 0.05)
        textAlign(CENTER, CENTER)
        fill(255)
        textSize(height * 0.05 * 0.6)
        text('Normaal', (width * 0.45 * 2 + width * 0.1) / 2, (height * 0.85 * 2 - textDescent() + height * 0.05) / 2)
        fill(218, 165, 32)
        stroke(0, 25, 0)
    if highlight == 3:
        fill(218, 165, 32)
        stroke(255)
        rect(width * 0.7, height * 0.85, width * 0.1, height * 0.05)
        textAlign(CENTER, CENTER)
        fill(255)
        textSize(height * 0.05 * 0.6)
        text('Moeilijk', (width * 0.7 * 2 + width * 0.1) / 2, (height * 0.85 * 2 - textDescent() + height * 0.05) / 2)
        fill(218, 165, 32)
        stroke(0, 25, 0)

    if mousePressed and width * 0.2 < mouseX < width * 0.3 and height * 0.85 < mouseY < height * 0.9:
        timer_difficulty = 40
        highlight = 1
    if mousePressed and width * 0.45 < mouseX < width * 0.55 and height * 0.85 < mouseY < height * 0.9:
        timer_difficulty = 30
        highlight = 2
    if mousePressed and width * 0.7 < mouseX < width * 0.8 and height * 0.85 < mouseY < height * 0.9:
        timer_difficulty = 20
        highlight = 3


# Tekent en geeft functionaliteit aan instructiekaart achterkant met verwarring
def instructie_back_v():
    global instructie_achterkant_img, current_screen, d, timer_start, player_count, second_player, player_turn

    if mousePressed and width * 0.34 < mouseX < width * 0.685 and height * 0.03 < mouseY < height * 0.95 \
            and second_player != '' and d == 0:
        background(background_img)
        timer_start = datetime.now()
        current_screen = 'random'
    else:
        kies_je_medespeler(instructie_achterkant_img)


# tekent en geeft functionaliteit aan instructiekaart achterkant zonder verwarring
def instructie_back():
    global instructie_achterkant2_img, current_screen, d, timer_start, player_count, second_player, player_turn

    if mousePressed and width * 0.34 < mouseX < width * 0.685 and height * 0.03 < mouseY < height * 0.95 and \
            second_player != '' and d == 0:
        background(background_img)
        timer_start = datetime.now()
        current_screen = 'random'

    else:
        kies_je_medespeler(instructie_achterkant2_img)


# Tekent en geeft functionaliteit aan continentkaart achterkant
def continent_back():
    global continent_achterkant_img, current_screen, d, timer_start, save, player_count, second_player, player_turn
    draw_medespeler_tekst()

    if mousePressed and width * 0.34 < mouseX < width * 0.685 and height * 0.03 < mouseY < height * 0.95 \
            and second_player != '' and d == 0:
        d = 1
        background(background_img)
        timer_start = datetime.now()
        save = False
        current_screen = 'droomCards'
    else:
        kies_je_medespeler(continent_achterkant_img)


# Tekent en geeft functionaliteit aan babelen kaart achterkant
def babelen_back():
    global babelspel_img, current_screen, d, second_player
    background(background_img)
    image(babelspel_img, (width // 2) - 300, 30)
    if mousePressed and width * 0.34 < mouseX < width * 0.685 and height * 0.03 < mouseY < height * 0.95 and d == 0:
        d = 1
        current_screen = 'babelen'


# Tekent en geeft functionaliteit aan winnaar babelen kiezen
def babelen():
    global continent_achterkant_img, current_screen, d, timer_start, save, player_count, second_player, player_turn
    global save, clicked, added_coins, coins, d
    if not clicked:
        if second_player != '':
            second_player = ''
            save = False

        elif d == 0:
            if second_player == player_turn:
                second_player = ''
            background(background_img)
            fill(218, 165, 32)
            rect(width * 0.3, height * 0.290, width * 0.4, height * 0.056)
            fill(255)
            textAlign(CENTER, CENTER)
            textSize(55)
            text('Kies de Speler die gewonnen heeft', width / 2, height * 0.2)
            fill(0)

            if width * 0.3 < mouseX < width * 0.7 and height * 0.290 < mouseY < height * 0.345 or second_player == 0:
                fill(218, 165, 32)
                stroke(255)
                rect(width * 0.3, height * 0.290, width * 0.4, height * 0.056)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.290 < mouseY < height * 0.345 \
                    and d == 0 or second_player == 0:
                second_player = 0
                clicked = True

            fill(218, 165, 32)
            rect(width * 0.3, height * 0.360, width * 0.4, height * 0.056)
            fill(0)
            if width * 0.3 < mouseX < width * 0.7 and height * 0.360 < mouseY < height * 0.402 or second_player == 1:
                fill(218, 165, 32)
                stroke(255)
                rect(width * 0.3, height * 0.360, width * 0.4, height * 0.056)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.360 < mouseY < height * 0.415 \
                    and d == 0 or second_player == 1:
                second_player = 1
                clicked = True

            fill(218, 165, 32)
            rect(width * 0.3, height * 0.430, width * 0.4, height * 0.056)
            fill(0)

            if width * 0.3 < mouseX < width * 0.7 and height * 0.430 < mouseY < height * 0.485 or second_player == 2:
                fill(218, 165, 32)
                stroke(255)
                rect(width * 0.3, height * 0.430, width * 0.4, height * 0.056)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.430 < mouseY < height * 0.486 \
                    and d == 0 or second_player == 2:
                second_player = 2
                clicked = True

            if player_count >= 3:
                fill(218, 165, 32)
                rect(width * 0.3, height * 0.500, width * 0.4, height * 0.056)
                fill(0)

                if width * 0.3 < mouseX < width * 0.7 and height * 0.500 < mouseY < height * 0.555 \
                        or second_player == 3:
                    fill(218, 165, 32)
                    stroke(255)
                    rect(width * 0.3, height * 0.500, width * 0.4, height * 0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.500 < mouseY < height * 0.555 \
                        and d == 0 or second_player == 3:
                    second_player = 3
                    clicked = True

            if player_count >= 4:
                fill(218, 165, 32)
                rect(width * 0.3, height * 0.570, width * 0.4, height * 0.0565)
                fill(0)

                if width * 0.3 < mouseX < width * 0.7 and height * 0.570 < mouseY < height * 0.625 \
                        or second_player == 4:
                    fill(218, 165, 32)
                    stroke(255)
                    rect(width * 0.3, height * 0.570, width * 0.4, height * 0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.570 < mouseY < height * 0.625 \
                        and d == 0 or second_player == 4:
                    second_player = 4
                    clicked = True

            if player_count >= 5:
                fill(218, 165, 32)
                rect(width * 0.3, height * 0.640, width * 0.4, height * 0.056)
                fill(0)

                if width * 0.3 < mouseX < width * 0.7 and height * 0.640 < mouseY < height * 0.695 \
                        or second_player == 5:
                    fill(218, 165, 32)
                    stroke(255)
                    rect(width * 0.3, height * 0.640, width * 0.4, height * 0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.640 < mouseY < height * 0.695 \
                        and d == 0 or second_player == 5:
                    second_player = 5
                    clicked = True

            if player_count >= 6:
                fill(218, 165, 32)
                rect(width * 0.3, height * 0.710, width * 0.4, height * 0.056)
                fill(0)
                if width * 0.3 < mouseX < width * 0.7 and height * 0.710 < mouseY < height * 0.765 \
                        or second_player == 6:
                    fill(218, 165, 32)
                    stroke(255)
                    rect(width * 0.3, height * 0.710, width * 0.4, height * 0.056)
                    fill(255)
                    stroke(0)
                fill(0)
                if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.710 < mouseY < height * 0.766 \
                        and d == 0 or second_player == 6:
                    second_player = 6
                    clicked = True

            global player_turn
            textSize(50)
            fill(0)
            textAlign(LEFT, TOP)
            for x in range(0, 7):
                if player_list[x][0] != '':
                    text(player_list[x][0], width * 0.33, (height * x * 0.0698) + (height * 0.291))

    if clicked:
        background(background_img)

        if not added_coins:
            possible_coins = [5, 10, 15, 20, 25, 50]
            coins = possible_coins[int(random(0, 6))]
            player_list[second_player][2] = player_list[second_player][2] + coins
            added_coins = True

        fill(218, 165, 32)
        rectMode(CENTER)
        rect(width / 2, height * 0.76, width * 0.20, height * 0.08)

        textSize(70)
        textAlign(CENTER, CENTER)
        fill(0)
        text('Menu', width / 2, height * 0.75)

        fill(255)
        text(player_list[second_player][0] + ' je krijgt een munt van ' + str(coins) + '\nJe hebt nu ' + str(
            player_list[second_player][2]) + ' munten', width / 2, height / 2)

        if mousePressed and width * 0.4 < mouseX < width * 0.6 and height * 0.72 < mouseY < height * 0.8 and d == 0:
            d = 1
            current_screen = 'hoofdmenu'


# Generates a new random card and shows it on the screen
def instructie():
    global d, instructie_img, timer_start, save, random_list, fill_or_no_fill, instr, verwarring
    if save != True:
        textSize(50)
        d = d + 1
        l = [525, 150, 275, 400]
        e = 4
        x = int(random(0, 5))
        f = x
        random_list = []
        fill_or_no_fill = []
        while e > 0:
            random_list.append(width / 2 - 0)
            if f > 0:
                x = int(random(0, len(l)))
                random_list.append(l.pop(x))
                fill_or_no_fill.append(0)
                f = f - 1
            else:
                fill_or_no_fill.append(1)
                random_list.append(l.pop())
            e = e - 1
        l = [525, 150, 275, 400]
        e = 4
        x = int(random(0, 5))
        f = x
        while e > 0:
            random_list.append(width / 2 + 130)
            if f > 0:
                x = int(random(0, len(l)))
                random_list.append(l.pop(x))
                fill_or_no_fill.append(0)
                f = f - 1
            else:
                fill_or_no_fill.append(1)
                random_list.append(l.pop())
            e = e - 1
        l = [525, 150, 275, 400]
        e = 4
        x = int(random(0, 5))
        f = x
        while e > 0:
            random_list.append(width / 2 + 260)
            if f > 0:
                x = int(random(0, len(l)))
                random_list.append(l.pop(x))
                fill_or_no_fill.append(0)
                f = f - 1
            else:
                fill_or_no_fill.append(1)
                random_list.append(l.pop())
            e = e - 1
        l = [525, 150, 275, 400]
        e = 4
        x = int(random(0, 5))
        f = x
        while e > 0:
            random_list.append(width / 2 - 125)
            if f > 0:
                x = int(random(0, len(l)))
                random_list.append(l.pop(x))
                fill_or_no_fill.append(0)
                f = f - 1
            else:
                fill_or_no_fill.append(1)
                random_list.append(l.pop())
            e = e - 1
        x = int(random(0, 4))
        instrlist = ["Gebruik niet de woorden 'links' \nen 'rechts'", u'Je mag geen co\u00F6rdinaten gebruiken',
                     "Gebruik niet de woorden 'omhoog',\n'omlaag', 'boven' of 'beneden'",
                     'gebruik geen getallen', "Gebruik Niet de woorden 'Wel'\n en 'Niet'",
                     "Gebruik niet de woorden 'goed'\nof 'fout'", "Gebruik niet de woorden 'onder'\n en 'boven'",
                     'Gebruik geen woorden', "Gebruik niet de woorden \n'ja' en 'nee'"]
        instr = instrlist.pop(int(random(0, len(instrlist))))
        save = True
        fill(0)

    background(background_img)
    image(instructie_img, (width // 2) - 300, 30)
    f = 0
    o = 0
    textSize(30)
    if len(fill_or_no_fill) > 14:
        while f < 31:
            if o < 16:
                x = fill_or_no_fill[o]
            o = o + 1
            if x == 0:
                fill(0)
            if x == 1:
                noFill()
            circle(random_list[f], random_list[f + 1], 60)
            f += 2

    if verwarring == True:
        textAlign(CENTER, CENTER)
        text(instr, width / 2 + width * 0.0199, height / 1.4)
    timer_func(width * 0.17)


def droom_cards():
    global droom_img, d, save, droom
    fill(0)
    textAlign(CENTER, CENTER)
    background(background_img)
    image(droom_img, (width // 2) - 300, 30)

    if save == False:
        droom_list = ['Aarde', 'Vuur', 'Water', 'Lucht', 'Bouwstenen', 'Constructie', 'Sloophamer', 'Opdrachten',
                     'Metselaar', 'Pikhouweel', 'Inspanning', 'Teamwork', 'Instorten', 'Hoogbouw',
                     'Laagbouw', 'Straffen', 'Vertaling', 'Wereldreis', 'Hoogtevrees', 'Onduidelijk', 'Begrijpen',
                     'Goddelijk', 'Verhalen', 'Mythe', 'Oudheid', 'Legende', 'Zuid-Amerika',
                     'Noord-Amerika', 'Europa', u'Azi\u00EB', u'Australi\u00EB', 'Antarctica', 'Afrika', 'Continent',
                     'Toendra', 'Woestijn', 'IJs', 'Zonneschijn', 'Maneschijn', 'Letters', 'Woorden']
        x = int(random(0, len(droom_list) - 1))
        droom = droom_list.pop(x)
        save = True
    if save == True:
        textSize(60)
        text(droom, width * 0.52, height / 2)
        timer_func(width * 0.17)


# Draws a timer on the screen that counts down to 0
def timer_func(placement):
    global timer_start, time_passed, d, current_screen, timer_difficulty, save
    textSize(200)
    fill(255)
    textAlign(CENTER, CENTER)

    time_passed = (datetime.now() - timer_start).seconds
    if time_passed > timer_difficulty or time_passed == 'De tijd is op!':
        time_passed = 'De tijd is op!'
        background(background_img)
        save = False
        current_screen = 'GoodOrBad'
    else:
        text(timer_difficulty - time_passed, placement, height / 2)
    rectMode(CENTER)
    fill(218, 165, 32)
    rect(placement, height * 0.65, width * 0.12, height * 0.045)
    textAlign(CENTER, CENTER)
    textSize(25)
    fill(0)
    text('Klaar', placement, height * 0.645)
    if mousePressed == True and placement - width * 0.06 < mouseX < placement + width * 0.06 and height * 0.65 - height * 0.0225 < mouseY < height * 0.65 + height * 0.0225:
        timer_start = datetime.max


# Verwijst naar juiste continent voor functionaliteit wereldkaart
def wereldkaart():
    global player_turn, game_over, current_screen
    if game_over:
        current_screen = 'gameFinished'
    if player_turn == 0:
        antartica()
    if player_turn == 1:
        europe()
    if player_turn == 2:
        south_america()
    if player_turn == 3:
        north_america()
    if player_turn == 4:
        asia()
    if player_turn == 5:
        australia()
    if player_turn == 6:
        africa()


# Tekent wereldkaart voor speler Europa
def europe():
    global ground10_img, ground15_img, ground20_img, ground50_img, wereldkaart_img, europa, player_turn, PlayersList
    background(background_img)
    image(wereldkaart_img, -12, -8, width * 0.82, height)
    if mousePressed == True and width * 0.28 < mouseX < width * 0.28 + 29 \
            and height * 0.33 < mouseY < height * 0.33 + 29 or europa[0] == 1:
        if europa[0] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            europa.pop(0)
            europa.insert(0, 1)
        if europa[0] != 1:
            image(ground20_img, width * 0.28, height * 0.33)

    else:
        image(ground20_img, width * 0.28, height * 0.33)

    if mousePressed == True and width * 0.30 < mouseX < width * 0.30 + 29 and height * 0.3 < mouseY < height * 0.3 + 29 \
            or europa[1] == 1:
        if europa[1] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            europa.pop(1)
            europa.insert(1, 1)
        if europa[1] != 1:
            image(ground20_img, width * 0.30, height * 0.3)
    else:
        image(ground20_img, width * 0.30, height * 0.3)

    if mousePressed == True and width * 0.32 < mouseX < width * 0.32 + 29 \
            and height * 0.20 < mouseY < height * 0.20 + 29 or europa[2] == 1:
        if europa[2] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            europa.pop(2)
            europa.insert(2, 1)
        if europa[2] != 1:
            image(ground15_img, width * 0.32, height * 0.20)
    else:
        image(ground15_img, width * 0.32, height * 0.20)

    if mousePressed == True and width * 0.33 < mouseX < width * 0.33 + 29 and height * 0.28 < mouseY < height * 0.28 + 29 or \
            europa[3] == 1:
        if europa[3] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            europa.pop(3)
            europa.insert(3, 1)
        if europa[3] != 1:
            image(ground20_img, width * 0.33, height * 0.28)
    else:
        image(ground20_img, width * 0.33, height * 0.28)

    if mousePressed == True and width * 0.35 < mouseX < width * 0.35 + 29 and height * 0.35 < mouseY < height * 0.35 + 29 or \
            europa[4] == 1:
        if europa[4] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            europa.pop(4)
            europa.insert(4, 1)
        if europa[4] != 1:
            image(ground20_img, width * 0.35, height * 0.35)
    else:
        image(ground20_img, width * 0.35, height * 0.35)

    if mousePressed == True and width * 0.36 < mouseX < width * 0.36 + 29 and height * 0.3 < mouseY < height * 0.3 + 29 or \
            europa[5] == 1:
        if europa[5] == 0 and (int(player_list[player_turn][2]) - int(50)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(50)
            europa.pop(5)
            europa.insert(5, 1)
        if europa[5] != 1:
            image(ground50_img, width * 0.36, height * 0.3)
    else:
        image(ground50_img, width * 0.36, height * 0.3)

    if mousePressed == True and width * 0.37 < mouseX < width * 0.37 + 29 and height * 0.18 < mouseY < height * 0.18 + 29 or \
            europa[6] == 1:
        if europa[6] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            europa.pop(6)
            europa.insert(6, 1)
        if europa[6] != 1:
            image(ground20_img, width * 0.37, height * 0.18)
    else:
        image(ground20_img, width * 0.37, height * 0.18)

    if mousePressed == True and width * 0.38 < mouseX < width * 0.38 + 29 and height * 0.25 < mouseY < height * 0.25 + 29 or \
            europa[7] == 1:
        if europa[7] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            europa.pop(7)
            europa.insert(7, 1)
        if europa[7] != 1:
            image(ground15_img, width * 0.38, height * 0.25)
    else:
        image(ground15_img, width * 0.38, height * 0.25)

    if mousePressed == True and width * 0.41 < mouseX < width * 0.41 + 29 and height * 0.2 < mouseY < height * 0.2 + 29 or \
            europa[8] == 1:
        if europa[8] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            europa.pop(8)
            europa.insert(8, 1)
        if europa[8] != 1:
            image(ground20_img, width * 0.41, height * 0.2)
    else:
        image(ground20_img, width * 0.41, height * 0.2)


# Tekent wereldkaart voor speler Azië
def asia():
    global BackgroundImg, ground10_img, ground15_img, ground20_img, ground50_img, wereldkaart_img, azie
    background(background_img)
    image(wereldkaart_img, -12, -8, width * 0.82, height)
    # Asia
    if mousePressed == True and width * 0.46 < mouseX < width * 0.46 + 29 and height * 0.33 < mouseY < height * 0.33 + 29 or \
            azie[0] == 1:
        if azie[0] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            azie.pop(0)
            azie.insert(0, 1)
        if azie[0] != 1:
            image(ground20_img, width * 0.46, height * 0.33)
    else:
        image(ground20_img, width * 0.46, height * 0.33)

    if mousePressed == True and width * 0.50 < mouseX < width * 0.50 + 29 and height * 0.3 < mouseY < height * 0.3 + 29 or \
            azie[1] == 1:
        if azie[1] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            azie.pop(1)
            azie.insert(1, 1)
        if azie[1] != 1:
            image(ground20_img, width * 0.50, height * 0.3)
    else:
        image(ground20_img, width * 0.50, height * 0.3)

    if mousePressed == True and width * 0.49 < mouseX < width * 0.49 + 29 and height * 0.20 < mouseY < height * 0.20 + 29 or \
            azie[2] == 1:
        if azie[2] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            azie.pop(2)
            azie.insert(2, 1)
        if azie[2] != 1:
            image(ground15_img, width * 0.49, height * 0.20)

    else:
        image(ground15_img, width * 0.49, height * 0.20)

    if mousePressed == True and width * 0.54 < mouseX < width * 0.54 + 29 and height * 0.28 < mouseY < height * 0.28 + 29 or \
            azie[3] == 1:
        if azie[3] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            azie.pop(3)
            azie.insert(3, 1)
        if azie[3] != 1:
            image(ground20_img, width * 0.54, height * 0.28)

    else:
        image(ground20_img, width * 0.54, height * 0.28)

    if mousePressed == True and width * 0.41 < mouseX < width * 0.41 + 29 and height * 0.43 < mouseY < height * 0.43 + 29 or \
            azie[4] == 1:
        if azie[4] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            azie.pop(4)
            azie.insert(4, 1)
        if azie[4] != 1:
            image(ground20_img, width * 0.41, height * 0.43)
    else:
        image(ground20_img, width * 0.41, height * 0.43)

    if mousePressed == True and width * 0.51 < mouseX < width * 0.51 + 29 and height * 0.42 < mouseY < height * 0.42 + 29 or \
            azie[5] == 1:
        if azie[5] == 0 and (int(player_list[player_turn][2]) - int(50)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(50)
            azie.pop(5)
            azie.insert(5, 1)
        if azie[5] != 1:
            image(ground50_img, width * 0.51, height * 0.42)
    else:
        image(ground50_img, width * 0.51, height * 0.42)

    if mousePressed == True and width * 0.56 < mouseX < width * 0.56 + 29 and height * 0.22 < mouseY < height * 0.22 + 29 or \
            azie[6] == 1:
        if azie[6] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            azie.pop(6)
            azie.insert(6, 1)
        if azie[6] != 1:
            image(ground20_img, width * 0.56, height * 0.22)
    else:
        image(ground20_img, width * 0.56, height * 0.22)

    if mousePressed == True and width * 0.47 < mouseX < width * 0.47 + 29 and height * 0.4 < mouseY < height * 0.4 + 29 or \
            azie[7] == 1:
        if azie[7] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            azie.pop(7)
            azie.insert(7, 1)
        if azie[7] != 1:
            image(ground15_img, width * 0.47, height * 0.4)
    else:
        image(ground15_img, width * 0.47, height * 0.4)

    if mousePressed == True and width * 0.44 < mouseX < width * 0.44 + 29 and height * 0.28 < mouseY < height * 0.28 + 29 or \
            azie[8] == 1:
        if azie[8] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            azie.pop(8)
            azie.insert(8, 1)
        if azie[8] != 1:
            image(ground20_img, width * 0.44, height * 0.28)
    else:
        image(ground20_img, width * 0.44, height * 0.28)


# Tekent wereldkaart voor speler Zuid-Amerika
def south_america():
    global BackgroundImg, ground10_img, ground15_img, ground20_img, ground50_img, wereldkaart_img, zuid_amerika
    background(background_img)
    image(wereldkaart_img, -12, -8, width * 0.82, height)
    # zuid-Amerika
    if mousePressed == True and width * 0.17 < mouseX < width * 0.17 + 29 and height * 0.73 < mouseY < height * 0.73 + 29 or \
            zuid_amerika[0] == 1:
        if zuid_amerika[0] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            zuid_amerika.pop(0)
            zuid_amerika.insert(0, 1)
        if zuid_amerika[0] != 1:
            image(ground20_img, width * 0.17, height * 0.73)
    else:
        image(ground20_img, width * 0.17, height * 0.73)

    if mousePressed == True and width * 0.17 < mouseX < width * 0.17 + 29 and height * 0.6 < mouseY < height * 0.6 + 29 or \
            zuid_amerika[1] == 1:
        if zuid_amerika[1] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            zuid_amerika.pop(1)
            zuid_amerika.insert(1, 1)
        if zuid_amerika[1] != 1:
            image(ground20_img, width * 0.17, height * 0.6)
    else:
        image(ground20_img, width * 0.17, height * 0.6)

    if mousePressed == True and width * 0.12 < mouseX < width * 0.12 + 29 and height * 0.63 < mouseY < height * 0.63 + 29 or \
            zuid_amerika[2] == 1:
        if zuid_amerika[2] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            zuid_amerika.pop(2)
            zuid_amerika.insert(2, 1)
        if zuid_amerika[2] != 1:
            image(ground20_img, width * 0.12, height * 0.63)
    else:
        image(ground20_img, width * 0.12, height * 0.63)

    if mousePressed == True and width * 0.15 < mouseX < width * 0.15 + 29 and height * 0.86 < mouseY < height * 0.86 + 29 or \
            zuid_amerika[3] == 1:
        if zuid_amerika[3] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            zuid_amerika.pop(3)
            zuid_amerika.insert(3, 1)
        if zuid_amerika[3] != 1:
            image(ground15_img, width * 0.15, height * 0.86)
    else:
        image(ground15_img, width * 0.15, height * 0.86)

    if mousePressed == True and width * 0.16 < mouseX < width * 0.16 + 29 and height * 0.65 < mouseY < height * 0.65 + 29 or \
            zuid_amerika[4] == 1:
        if zuid_amerika[4] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            zuid_amerika.pop(4)
            zuid_amerika.insert(4, 1)
        if zuid_amerika[4] != 1:
            image(ground20_img, width * 0.16, height * 0.65)
    else:
        image(ground20_img, width * 0.16, height * 0.65)

    if mousePressed == True and width * 0.14 < mouseX < width * 0.14 + 29 and height * 0.75 < mouseY < height * 0.75 + 29 or \
            zuid_amerika[5] == 1:
        if zuid_amerika[5] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            zuid_amerika.pop(5)
            zuid_amerika.insert(5, 1)
        if zuid_amerika[5] != 1:
            image(ground20_img, width * 0.14, height * 0.75)
    else:
        image(ground20_img, width * 0.14, height * 0.75)

    if mousePressed == True and width * 0.2 < mouseX < width * 0.2 + 29 and height * 0.64 < mouseY < height * 0.64 + 29 or \
            zuid_amerika[6] == 1:
        if zuid_amerika[6] == 0 and (int(player_list[player_turn][2]) - int(50)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(50)
            zuid_amerika.pop(6)
            zuid_amerika.insert(6, 1)
        if zuid_amerika[6] != 1:
            image(ground50_img, width * 0.20, height * 0.64)
    else:
        image(ground50_img, width * 0.20, height * 0.64)

    if mousePressed == True and width * 0.16 < mouseX < width * 0.16 + 29 and height * 0.78 < mouseY < height * 0.78 + 29 or \
            zuid_amerika[7] == 1:
        if zuid_amerika[7] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            zuid_amerika.pop(7)
            zuid_amerika.insert(7, 1)
        if zuid_amerika[7] != 1:
            image(ground20_img, width * 0.16, height * 0.78)
    else:
        image(ground20_img, width * 0.16, height * 0.78)

    if mousePressed == True and width * 0.13 < mouseX < width * 0.13 + 29 and height * 0.56 < mouseY < height * 0.56 + 29 or \
            zuid_amerika[8] == 1:
        if zuid_amerika[8] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            zuid_amerika.pop(8)
            zuid_amerika.insert(8, 1)
        if zuid_amerika[8] != 1:
            image(ground15_img, width * 0.13, height * 0.56)
    else:
        image(ground15_img, width * 0.13, height * 0.56)


def africa():
    global BackgroundImg, ground10_img, ground15_img, ground20_img, ground50_img, wereldkaart_img, afrika
    background(background_img)
    image(wereldkaart_img, -12, -8, width * 0.82, height)
    # Africa
    if mousePressed == True and width * 0.39 < mouseX < width * 0.39 + 29 and height * 0.71 < mouseY < height * 0.71 + 29 or \
            afrika[0] == 1:
        if afrika[0] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            afrika.pop(0)
            afrika.insert(0, 1)
        if afrika[0] != 1:
            image(ground20_img, width * 0.39, height * 0.71)
    else:
        image(ground20_img, width * 0.39, height * 0.71)

    if mousePressed == True and width * 0.4 < mouseX < width * 0.4 + 29 and height * 0.6 < mouseY < height * 0.6 + 29 or \
            afrika[1] == 1:
        if afrika[1] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            afrika.pop(1)
            afrika.insert(1, 1)
        if afrika[1] != 1:
            image(ground20_img, width * 0.4, height * 0.6)

    else:
        image(ground20_img, width * 0.4, height * 0.6)

    if mousePressed == True and width * 0.3 < mouseX < width * 0.3 + 29 and height * 0.42 < mouseY < height * 0.42 + 29 or \
            afrika[2] == 1:
        if afrika[2] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            afrika.pop(2)
            afrika.insert(2, 1)
        if afrika[2] != 1:
            image(ground15_img, width * 0.3, height * 0.42)
    else:
        image(ground15_img, width * 0.3, height * 0.42)

    if mousePressed == True and width * 0.37 < mouseX < width * 0.37 + 29 and height * 0.39 < mouseY < height * 0.39 + 29 or \
            afrika[3] == 1:
        if afrika[3] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            afrika.pop(3)
            afrika.insert(3, 1)
        if afrika[3] != 1:
            image(ground20_img, width * 0.37, height * 0.39)
    else:
        image(ground20_img, width * 0.37, height * 0.39)

    if mousePressed == True and width * 0.36 < mouseX < width * 0.36 + 29 and height * 0.75 < mouseY < height * 0.75 + 29 or \
            afrika[4] == 1:
        if afrika[4] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            afrika.pop(4)
            afrika.insert(4, 1)
        if afrika[4] != 1:
            image(ground20_img, width * 0.36, height * 0.75)
    else:
        image(ground20_img, width * 0.36, height * 0.75)

    if mousePressed == True and width * 0.28 < mouseX < width * 0.28 + 29 and height * 0.5 < mouseY < height * 0.5 + 29 or \
            afrika[5] == 1:
        if afrika[5] == 0 and (int(player_list[player_turn][2]) - int(50)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(50)
            afrika.pop(5)
            afrika.insert(5, 1)
        if afrika[5] != 1:
            image(ground50_img, width * 0.28, height * 0.50)
    else:
        image(ground50_img, width * 0.28, height * 0.50)

    if mousePressed == True and width * 0.35 < mouseX < width * 0.35 + 29 and height * 0.58 < mouseY < height * 0.58 + 29 or \
            afrika[6] == 1:
        if afrika[6] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            afrika.pop(6)
            afrika.insert(6, 1)
        if afrika[6] != 1:
            image(ground20_img, width * 0.35, height * 0.58)
    else:
        image(ground20_img, width * 0.35, height * 0.58)

    if mousePressed == True and width * 0.42 < mouseX < width * 0.42 + 29 and height * 0.53 < mouseY < height * 0.53 + 29 or \
            afrika[7] == 1:
        if afrika[7] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            afrika.pop(7)
            afrika.insert(7, 1)
        if afrika[7] != 1:
            image(ground15_img, width * 0.42, height * 0.53)
    else:
        image(ground15_img, width * 0.42, height * 0.53)

    if mousePressed == True and width * 0.38 < mouseX < width * 0.38 + 29 and height * 0.49 < mouseY < height * 0.49 + 29 or \
            afrika[8] == 1:
        if afrika[8] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            afrika.pop(8)
            afrika.insert(8, 1)
        if afrika[8] != 1:
            image(ground20_img, width * 0.38, height * 0.49)
    else:
        image(ground20_img, width * 0.38, height * 0.49)


# Tekent wereldkaart voor speler Noord-Amerika
def north_america():
    global BackgroundImg, ground10_img, ground15_img, ground20_img, ground50_img, wereldkaart_img, noord_amerika
    background(background_img)
    image(wereldkaart_img, -12, -8, width * 0.82, height)
    # North-Amerika
    if mousePressed == True and width * 0.1 < mouseX < width * 0.1 + 29 and height * 0.33 < mouseY < height * 0.33 + 29 or \
            noord_amerika[0] == 1:
        if noord_amerika[0] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            noord_amerika.pop(0)
            noord_amerika.insert(0, 1)
        if noord_amerika[0] != 1:
            image(ground20_img, width * 0.1, height * 0.33)
    else:
        image(ground20_img, width * 0.1, height * 0.33)

    if mousePressed == True and width * 0.08 < mouseX < width * 0.08 + 29 and height * 0.37 < mouseY < height * 0.37 + 29 or \
            noord_amerika[1] == 1:
        if noord_amerika[1] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            noord_amerika.pop(1)
            noord_amerika.insert(1, 1)
        if noord_amerika[1] != 1:
            image(ground20_img, width * 0.08, height * 0.37)
    else:
        image(ground20_img, width * 0.08, height * 0.37)

    if mousePressed == True and width * 0.08 < mouseX < width * 0.08 + 29 and height * 0.26 < mouseY < height * 0.26 + 29 or \
            noord_amerika[2] == 1:
        if noord_amerika[2] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            noord_amerika.pop(2)
            noord_amerika.insert(2, 1)
        if noord_amerika[2] != 1:
            image(ground15_img, width * 0.08, height * 0.26)
    else:
        image(ground15_img, width * 0.08, height * 0.26)

    if mousePressed == True and width * 0.19 < mouseX < width * 0.19 + 29 and height * 0.25 < mouseY < height * 0.25 + 29 or \
            noord_amerika[3] == 1:
        if noord_amerika[3] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            noord_amerika.pop(3)
            noord_amerika.insert(3, 1)
        if noord_amerika[3] != 1:
            image(ground20_img, width * 0.19, height * 0.25)
    else:
        image(ground20_img, width * 0.19, height * 0.25)

    if mousePressed == True and width * 0.14 < mouseX < width * 0.14 + 29 and height * 0.35 < mouseY < height * 0.35 + 29 or \
            noord_amerika[4] == 1:
        if noord_amerika[4] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            noord_amerika.pop(4)
            noord_amerika.insert(4, 1)
        if noord_amerika[4] != 1:
            image(ground20_img, width * 0.14, height * 0.35)
    else:
        image(ground20_img, width * 0.14, height * 0.35)

    if mousePressed == True and mouseX > width * 0.2 and mouseX < width * 0.2 + 29 and mouseY > height * 0.14 and mouseY < height * 0.14 + 29 or \
            noord_amerika[5] == 1:
        if noord_amerika[5] == 0 and (int(player_list[player_turn][2]) - int(50)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(50)
            noord_amerika.pop(5)
            noord_amerika.insert(5, 1)
        if noord_amerika[5] != 1:
            image(ground50_img, width * 0.20, height * 0.14)
    else:
        image(ground50_img, width * 0.20, height * 0.14)

    if mousePressed == True and width * 0.16 < mouseX < width * 0.16 + 29 and height * 0.18 < mouseY < height * 0.18 + 29 or \
            noord_amerika[6] == 1:
        if noord_amerika[6] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            noord_amerika.pop(6)
            noord_amerika.insert(6, 1)
        if noord_amerika[6] != 1:
            image(ground20_img, width * 0.16, height * 0.18)
    else:
        image(ground20_img, width * 0.16, height * 0.18)

    if mousePressed == True and width * 0.09 < mouseX < width * 0.09 + 29 and height * 0.44 < mouseY < height * 0.44 + 29 or \
            noord_amerika[7] == 1:
        if noord_amerika[7] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            noord_amerika.pop(7)
            noord_amerika.insert(7, 1)
        if noord_amerika[7] != 1:
            image(ground15_img, width * 0.09, height * 0.44)
    else:
        image(ground15_img, width * 0.09, height * 0.44)

    if mousePressed == True and width * 0.06 < mouseX < width * 0.06 + 29 and height * 0.17 < mouseY < height * 0.17 + 29 or \
            noord_amerika[8] == 1:
        if noord_amerika[8] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            noord_amerika.pop(8)
            noord_amerika.insert(8, 1)
        if noord_amerika[8] != 1:
            image(ground20_img, width * 0.06, height * 0.17)
    else:
        image(ground20_img, width * 0.06, height * 0.17)


def antartica():
    global BackgroundImg, ground10_img, ground15_img, ground20_img, ground50_img, wereldkaart_img, antarctica
    background(background_img)
    image(wereldkaart_img, -12, -8, width * 0.82, height)
    # antartica
    if mousePressed == True and width * 0.39 < mouseX < width * 0.39 + 29 and height * 0.81 < mouseY < height * 0.81 + 29 or \
            antarctica[0] == 1:
        if antarctica[0] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            antarctica.pop(0)
            antarctica.insert(0, 1)
        if antarctica[0] != 1:
            image(ground20_img, width * 0.39, height * 0.81)
    else:
        image(ground20_img, width * 0.39, height * 0.81)

    if mousePressed == True and width * 0.49 < mouseX < width * 0.49 + 29 and height * 0.78 < mouseY < height * 0.78 + 29 or \
            antarctica[1] == 1:
        if antarctica[1] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            antarctica.pop(1)
            antarctica.insert(1, 1)
        if antarctica[1] != 1:
            image(ground20_img, width * 0.49, height * 0.78)
    else:
        image(ground20_img, width * 0.49, height * 0.78)

    if mousePressed == True and width * 0.27 < mouseX < width * 0.27 + 29 and height * 0.83 < mouseY < height * 0.83 + 29 or \
            antarctica[2] == 1:
        if antarctica[2] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            antarctica.pop(2)
            antarctica.insert(2, 1)
        if antarctica[2] != 1:
            image(ground15_img, width * 0.27, height * 0.83)
    else:
        image(ground15_img, width * 0.27, height * 0.83)

    if mousePressed == True and width * 0.22 < mouseX < width * 0.22 + 29 and height * 0.89 < mouseY < height * 0.89 + 29 or \
            antarctica[3] == 1:
        if antarctica[3] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            antarctica.pop(3)
            antarctica.insert(3, 1)
        if antarctica[3] != 1:
            image(ground20_img, width * 0.22, height * 0.89)
    else:
        image(ground20_img, width * 0.22, height * 0.89)

    if mousePressed == True and width * 0.36 < mouseX < width * 0.36 + 29 and height * 0.85 < mouseY < height * 0.85 + 29 or \
            antarctica[4] == 1:
        if antarctica[4] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            antarctica.pop(4)
            antarctica.insert(4, 1)
        if antarctica[4] != 1:
            image(ground20_img, width * 0.36, height * 0.85)
    else:
        image(ground20_img, width * 0.36, height * 0.85)

    if mousePressed == True and width * 0.64 < mouseX < width * 0.64 + 29 and height * 0.8 < mouseY < height * 0.8 + 29 or \
            antarctica[5] == 1:
        if antarctica[5] == 0 and (int(player_list[player_turn][2]) - int(50)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(50)
            antarctica.pop(5)
            antarctica.insert(5, 1)
        if antarctica[5] != 1:
            image(ground50_img, width * 0.64, height * 0.80)
    else:
        image(ground50_img, width * 0.64, height * 0.80)

    if mousePressed == True and width * 0.6 < mouseX < width * 0.6 + 29 and height * 0.9 < mouseY < height * 0.9 + 29 or \
            antarctica[6] == 1:
        if antarctica[6] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            antarctica.pop(6)
            antarctica.insert(6, 1)
        if antarctica[6] != 1:
            image(ground20_img, width * 0.60, height * 0.9)
    else:
        image(ground20_img, width * 0.60, height * 0.9)

    if mousePressed == True and width * 0.54 < mouseX < width * 0.54 + 29 and height * 0.86 < mouseY < height * 0.86 + 29 or \
            antarctica[7] == 1:
        if antarctica[7] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            antarctica.pop(7)
            antarctica.insert(7, 1)
        if antarctica[7] != 1:
            image(ground20_img, width * 0.54, height * 0.86)
    else:
        image(ground15_img, width * 0.54, height * 0.86)

    if mousePressed == True and width * 0.45 < mouseX < width * 0.45 + 29 and height * 0.89 < mouseY < height * 0.89 + 29 or \
            antarctica[8] == 1:
        if antarctica[8] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            antarctica.pop(8)
            antarctica.insert(8, 1)
        if antarctica[8] != 1:
            image(ground20_img, width * 0.45, height * 0.89)
    else:
        image(ground20_img, width * 0.45, height * 0.89)


def australia():
    global BackgroundImg, ground10_img, ground15_img, ground20_img, ground50_img, wereldkaart_img, australie
    background(background_img)
    image(wereldkaart_img, -12, -8, width * 0.82, height)
    # Australie
    if mousePressed == True and width * 0.63 < mouseX < width * 0.63 + 29 and height * 0.7 < mouseY < height * 0.7 + 29 or \
            australie[0] == 1:
        if australie[0] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            australie.pop(0)
            australie.insert(0, 1)
        if australie[0] != 1:
            image(ground20_img, width * 0.63, height * 0.7)
    else:
        image(ground20_img, width * 0.63, height * 0.7)

    if mousePressed == True and width * 0.61 < mouseX < width * 0.61 + 29 and height * 0.67 < mouseY < height * 0.67 + 29 or \
            australie[1] == 1:
        if australie[1] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            australie.pop(1)
            australie.insert(1, 1)
        if australie[1] != 1:
            image(ground20_img, width * 0.61, height * 0.67)
    else:
        image(ground20_img, width * 0.61, height * 0.67)

    if mousePressed == True and width * 0.68 < mouseX < width * 0.68 + 29 and height * 0.57 < mouseY < height * 0.57 + 29 or \
            australie[2] == 1:
        if australie[2] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            australie.pop(2)
            australie.insert(2, 1)
        if australie[2] != 1:
            image(ground15_img, width * 0.68, height * 0.57)
    else:
        image(ground15_img, width * 0.68, height * 0.57)

    if mousePressed == True and width * 0.64 < mouseX < width * 0.64 + 29 and height * 0.64 < mouseY < height * 0.64 + 29 or \
            australie[3] == 1:
        if australie[3] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            australie.pop(3)
            australie.insert(3, 1)
        if australie[3] != 1:
            image(ground20_img, width * 0.64, height * 0.64)
    else:
        image(ground20_img, width * 0.64, height * 0.64)

    if mousePressed == True and width * 0.72 < mouseX < width * 0.72 + 29 and height * 0.72 < mouseY < height * 0.72 + 29 or \
            australie[4] == 1:
        if australie[4] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            australie.pop(4)
            australie.insert(4, 1)
        if australie[4] != 1:
            image(ground20_img, width * 0.72, height * 0.72)
    else:
        image(ground20_img, width * 0.72, height * 0.72)

    if mousePressed == True and width * 0.72 < mouseX < width * 0.72 + 29 and height * 0.6 < mouseY < height * 0.6 + 29 or \
            australie[5] == 1:
        if australie[5] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(50)
            australie.pop(5)
            australie.insert(5, 1)
        if australie[5] != 1:
            image(ground50_img, width * 0.72, height * 0.6)
    else:
        image(ground50_img, width * 0.72, height * 0.6)

    if mousePressed == True and width * 0.69 < mouseX < width * 0.69 + 29 and height * 0.64 < mouseY < height * 0.64 + 29 or \
            australie[6] == 1:
        if australie[6] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            australie.pop(6)
            australie.insert(6, 1)
        if australie[6] != 1:
            image(ground20_img, width * 0.69, height * 0.64)
    else:
        image(ground20_img, width * 0.69, height * 0.64)

    if mousePressed == True and width * 0.69 < mouseX < width * 0.69 + 29 and height * 0.74 < mouseY < height * 0.74 + 29 or \
            australie[7] == 1:
        if australie[7] == 0 and (int(player_list[player_turn][2]) - int(15)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(15)
            australie.pop(7)
            australie.insert(7, 1)
        if australie[7] != 1:
            image(ground15_img, width * 0.69, height * 0.74)
    else:
        image(ground15_img, width * 0.69, height * 0.74)

    if mousePressed == True and width * 0.7 < mouseX < width * 0.7 + 29 and height * 0.68 < mouseY < height * 0.68 + 29 or \
            australie[8] == 1:
        if australie[8] == 0 and (int(player_list[player_turn][2]) - int(20)) >= 0:
            player_list[player_turn][2] = int(player_list[player_turn][2]) - int(20)
            australie.pop(8)
            australie.insert(8, 1)
        if australie[8] != 1:
            image(ground20_img, width * 0.7, height * 0.68)
    else:
        image(ground20_img, width * 0.7, height * 0.68)


# Checkt of een speler alle land van zijn continent heeft gekocht en verwijst hierna door naar eindscherm
def check_if_game_is_finished():
    global europa, noord_amerika, zuid_amerika, afrika, azie, antarctica, australie, game_winner, game_over
    global current_screen

    if antarctica == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        game_winner = 0
        game_over = True
        current_screen = 'gameFinished'
    elif europa == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        game_winner = 1
        game_over = True
        current_screen = 'gameFinished'
    elif zuid_amerika == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        game_winner = 2
        game_over = True
        current_screen = 'gameFinished'
    elif noord_amerika == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        game_winner = 3
        game_over = True
        current_screen = 'gameFinished'
    elif azie == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        game_winner = 4
        game_over = True
        current_screen = 'gameFinished'
    elif australie == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        game_winner = 5
        game_over = True
        current_screen = 'gameFinished'
    elif afrika == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
        game_winner = 6
        game_over = True
        current_screen = 'gameFinished'


# Tekent en geeft functionaliteit aan het eindscherm
def game_finished():
    global game_winner, player_list
    background(background_img)
    textAlign(CENTER, CENTER)
    textSize(70)
    fill(255)
    text(player_list[game_winner][0] + ' (' + player_list[game_winner][1] + ') \n'
         + 'heeft de Verwarring van Babel gewonnen!', width / 2, height / 2)
    fill(218, 165, 32)
    rectMode(CENTER)
    rect(width / 2, height * 0.8, width * 0.35, height * 0.13)

    textAlign(CENTER, CENTER)
    fill(0)
    textSize(60)
    text('Speel opnieuw!', width / 2, height * 0.8)
    if mousePressed and width * 0.3 < mouseX < width * 0.7 and height * 0.725 < mouseY < height * 0.875:
        setup()


# Tekent huidige tijd op scherm
def clock():
    noSmooth()
    textSize(50)
    fill(255)
    textAlign(RIGHT, BOTTOM)
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    text(current_time, width - 20, height - 20)


# Tekent bij achterkant kaarten het 'kies je medespeler' gedeelte en geeft hier functionaliteit aan de knoppen
def kies_je_medespeler(img):
    global second_player, d, player_turn
    if second_player == player_turn:
        second_player = ''

    background(background_img)
    image(img, (width // 2) - 300, 30)
    fill(218, 165, 32)
    rect(width * 0.03, height * 0.302, width * 0.2, height * 0.038)
    fill(0)
    if player_turn == 0:
        fill(200)
        stroke(0)
        rect(width * 0.03, height * 0.302, width * 0.2, height * 0.038)
        fill(255)
        stroke(0)
        fill(0)
    else:
        if width * 0.03 < mouseX < width * 0.23 and height * 0.302 < mouseY < height * 0.339 or second_player == 0:
            fill(218, 165, 32)
            stroke(255)
            rect(width * 0.03, height * 0.302, width * 0.2, height * 0.038)
            fill(255)
            stroke(0)
        fill(0)
        if mousePressed and width * 0.03 < mouseX < width * 0.23 and height * 0.302 < mouseY < height * 0.339 \
                and d == 0 or second_player == 0:
            second_player = 0
            d = 0

    fill(218, 165, 32)
    rect(width * 0.03, height * 0.352, width * 0.2, height * 0.038)
    fill(0)
    if player_turn == 1:
        fill(200)
        stroke(0)
        rect(width * 0.03, height * 0.352, width * 0.2, height * 0.038)
        fill(255)
        stroke(0)
        fill(0)
    else:
        if width * 0.03 < mouseX < width * 0.23 and height * 0.352 < mouseY < height * 0.389 or second_player == 1:
            fill(218, 165, 32)
            stroke(255)
            rect(width * 0.03, height * 0.352, width * 0.2, height * 0.038)
            fill(255)
            stroke(0)
        fill(0)
        if mousePressed and width * 0.03 < mouseX < width * 0.23 and height * 0.352 < mouseY < height * 0.371 \
                and d == 0 or second_player == 1:
            second_player = 1
            d = 0

    fill(218, 165, 32)
    rect(width * 0.03, height * 0.402, width * 0.2, height * 0.038)
    fill(0)
    if player_turn == 2:
        fill(200)
        stroke(0)
        rect(width * 0.03, height * 0.402, width * 0.2, height * 0.038)
        fill(255)
        stroke(0)
        fill(0)
    else:
        if width * 0.03 < mouseX < width * 0.23 and height * 0.402 < mouseY < height * 0.439 or second_player == 2:
            fill(218, 165, 32)
            stroke(255)
            rect(width * 0.03, height * 0.402, width * 0.2, height * 0.038)
            fill(255)
            stroke(0)
        fill(0)
        if mousePressed and width * 0.03 < mouseX < width * 0.23 and height * 0.402 < mouseY < height * 0.439 \
                and d == 0 or second_player == 2:
            second_player = 2
            d = 0

    if player_count >= 3:
        fill(218, 165, 32)
        rect(width * 0.03, height * 0.452, width * 0.2, height * 0.038)
        fill(0)
    if player_turn == 3:
        fill(200)
        stroke(0)
        rect(width * 0.03, height * 0.452, width * 0.2, height * 0.038)
        fill(255)
        stroke(0)
        fill(0)
    else:
        if width * 0.03 < mouseX < width * 0.23 and height * 0.452 < mouseY < height * 0.489 \
                or second_player == 3:
            fill(218, 165, 32)
            stroke(255)
            rect(width * 0.03, height * 0.452, width * 0.2, height * 0.038)
            fill(255)
            stroke(0)
            fill(0)
        if mousePressed and width * 0.03 < mouseX < width * 0.23 and height * 0.452 < mouseY < height * 0.489 \
                and d == 0 or second_player == 3:
            second_player = 3
            d = 0

    if player_count >= 4:
        fill(218, 165, 32)
        rect(width * 0.03, height * 0.502, width * 0.2, height * 0.038)
        fill(0)
        if player_turn == 4:
            fill(200)
            stroke(0)
            rect(width * 0.03, height * 0.502, width * 0.2, height * 0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if width * 0.03 < mouseX < width * 0.23 and height * 0.502 < mouseY < height * 0.539 \
                    or second_player == 4:
                fill(218, 165, 32)
                stroke(255)
                rect(width * 0.03, height * 0.502, width * 0.2, height * 0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed and width * 0.03 < mouseX < width * 0.23 and height * 0.502 < mouseY < height * 0.539 \
                    and d == 0 or second_player == 4:
                second_player = 4
                d = 0

    if player_count >= 5:
        fill(218, 165, 32)
        rect(width * 0.03, height * 0.552, width * 0.2, height * 0.038)
        fill(0)
        if player_turn == 5:
            fill(200)
            stroke(0)
            rect(width * 0.03, height * 0.552, width * 0.2, height * 0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if width * 0.03 < mouseX < width * 0.23 and height * 0.552 < mouseY < height * 0.58 \
                    or second_player == 5:
                fill(218, 165, 32)
                stroke(255)
                rect(width * 0.03, height * 0.552, width * 0.2, height * 0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed and width * 0.03 < mouseX < width * 0.23 and height * 0.552 < mouseY < height * 0.59 \
                    and d == 0 or second_player == 5:
                second_player = 5
                d = 0

    if player_count >= 6:
        fill(218, 165, 32)
        rect(width * 0.03, height * 0.602, width * 0.2, height * 0.038)
        fill(0)
        if player_turn == 6:
            fill(200)
            stroke(0)
            rect(width * 0.03, height * 0.602, width * 0.2, height * 0.038)
            fill(255)
            stroke(0)
            fill(0)
        else:
            if width * 0.03 < mouseX < width * 0.2 + width * 0.03 and height * 0.600 < mouseY < height * 0.037 + height * 0.602 or second_player == 6:
                fill(218, 165, 32)
                stroke(255)
                rect(width * 0.03, height * 0.602, width * 0.2, height * 0.038)
                fill(255)
                stroke(0)
            fill(0)
            if mousePressed and width * 0.03 < mouseX < width * 0.23 and height * 0.602 < mouseY < height * 0.639 \
                    and d == 0 or second_player == 6:
                second_player = 6
                d = 0

    global player_turn
    fill(0)
    rectMode(CORNER)
    fill(218, 165, 32)
    stroke(0, 25, 0)
    rect(width * 0.81, height * 0.25, width * 0.185, height * 0.35)
    textSize(30)
    fill(0)
    textAlign(LEFT, TOP)
    for x in range(0, 7):
        if player_list[x][0] != '':
            text(player_list[x][0], width * 0.05, (height * x * 0.05) + (height * 0.305))

    draw_medespeler_tekst()


# Tekent tekst 'kies je medespeler' bij achterkant kaarten
def draw_medespeler_tekst():
    fill(255)
    textSize(40)
    textAlign(LEFT, TOP)
    text('Kies je medespeler', width * 0.03, height * 0.22)


def keyReleased():
    global current_player, current_screen, player_count
    if current_screen == 'inputNames':
        if key in allowed_characters and len(player_list[current_player][0]) <= 8:
            player_list[current_player][0] += key
        elif key == BACKSPACE:
            player_list[current_player][0] = player_list[current_player][0][:-1]
        elif key == ENTER and player_list[current_player][0] != '':
            player_count += 1
            if current_player == 6:
                current_screen = 'hoofdmenu'
            else:
                current_player += 1


# Zorgt voor betere overgang bij klikken op knoppen
def mouseReleased():
    global d, current_screen
    d = 0
    if current_screen == 'inputNames' and width * 0.375 < mouseX < width * 0.625 \
            and height * 0.65 < mouseY < height * 0.65 + 0.05 * height and player_list[2][0] != '':
        current_screen = 'hoofdmenu'
