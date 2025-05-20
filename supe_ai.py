import pygame as gameone
import math
import random

# Initialize pygame
gameone.init()

# Set up frame rate control
clock = gameone.time.Clock()  # Clock object to track time and frame rate
fps = 60  # Set the desired frames per second

# Initialize game window
intcheck = True
myscreen = gameone.display.set_mode((1280, 720))  # Game screen resolution
gameloop = True  # Main game loop controller

# Load and set the game icon
icon = gameone.image.load("icon.png")
gameone.display.set_icon(icon)

# Set window caption
gameone.display.set_caption("JLA")

# Player stats and bullet variables
playerhp = 550
bulletx = 1280
bulletleftx = 720
bullety = 100
start = False
defeated = 0

# Round setup variables
enwaitframe = 4000
round = 1
round1 = True
round2 = False
round3 = False

animcount = 0  # Animation count for character's stance

# Music and sound setup
gameone.mixer.music.load("mainscoreloop.wav")
gameone.mixer.music.set_volume(0.5)
gameone.mixer.music.play(-1)

shootsound = gameone.mixer.Sound("laser.wav")
blast = gameone.mixer.Sound("explosion.wav")
blast.set_volume(1.0)

# Load all images and sprites
lazer = gameone.image.load("bullet.png").convert_alpha()
lazerleft = gameone.image.load("bulletleft.png").convert_alpha()

# Superman's standing animations
supstandleft1 = gameone.image.load("supestandleft.png").convert_alpha()
supstandleft2 = gameone.image.load("supstandanim2left.png")
supstandleft = supstandleft1

# Superman's right-facing animations
supstand1 = gameone.image.load("supestand.png").convert_alpha()
supstand = supstand1
supstand2 = gameone.image.load("supstandanim1.png").convert_alpha()
supstand3 = gameone.image.load("supstandanim2.png").convert_alpha()

# Load movement animations for Superman
supright = gameone.image.load("supesright.png").convert_alpha()
supleft = gameone.image.load("supesleft.png").convert_alpha()
supdown = gameone.image.load("supesdown.png").convert_alpha()
supdownleft = gameone.image.load("supesdownleft.png")
supup = gameone.image.load("supesup.png").convert_alpha()
supupleft = gameone.image.load("supesupleft.png").convert_alpha()
supshoot = gameone.image.load("supeshoot3.png").convert_alpha()
supfail = gameone.image.load("supeshoot.png").convert_alpha()
supfailleft = gameone.image.load("supeshootleft.png").convert_alpha()
supshootleft = gameone.image.load("supeshoot3left.png").convert_alpha()

# Enemy visuals
enem1look = gameone.image.load("enemy1.png").convert_alpha()
enem1lookright = gameone.image.load("enemy1right.png").convert_alpha()
enblast = gameone.image.load("pngegg.png").convert_alpha()

# Other assets
bg = gameone.image.load("back8ed.png").convert_alpha()
healthbar = gameone.image.load("healthbar.png").convert_alpha()

# Initial position variables
supx = 500
supy = 360
supcurpos = "supestand.png"
gameone.display.set_icon(icon)
gameone.display.set_caption("JLA")
# supes position
supx = 500
supy = 360
supstanddir = supstand
supsshootdir = "right"
supupdir = supup
supdowndir = supdown
supechangey = 0
supechannge = 0
supefaceic = gameone.image.load("supface.png").convert_alpha()
supe = supstand1  # Start with right standing sprite

# Enemy initialization
enem1 = []
enementered = []
enem1y = []
enem1x = []
enemmove = []
enemmovey = []
enhurt = []
enem1hp = []
enemisdead = []
envert = []
enemblast = []
enemblastx = []
enemblasty = []
number_of_enemies = 6

# Function to spawn enemies
def enemspawn(number, hp=3):
    global en1spawnid
    enementered.clear()
    en1spawnid = 0
    enemblast.clear()
    enemblasty.clear()
    enemblastx.clear()
    enem1.clear()
    enem1y.clear()
    enem1x.clear()
    enemmove.clear()
    enemmovey.clear()
    enhurt.clear()
    enem1hp.clear()
    enemisdead.clear()
    envert.clear()
    
    # Randomly initialize enemies
    for enemy in range(number):
        if enemy % 2 == 0:  # Even enemies move left
            enem1.append(enem1lookright)
            enem1x.append(1150)
            enhurt.append("enemy1hurtright.png")
            envert.append("up")
            enemmove.append(-0.8)
            enemmovey.append(0.8)
        else:  # Odd enemies move right
            enem1.append(enem1look)
            enem1x.append(20)
            enhurt.append("enemy1hurt.png")
            envert.append("down")
            enemmove.append(0.8)
            enemmovey.append(-0.8)
        enem1y.append(random.randint(50, 600))
        enem1hp.append(hp)
        enemisdead.append("False")
        enemblast.append(0)
        enemblastx.append(0)
        enemblasty.append(0)

# Bullet and shooting setup
supbullet = lazer
state = "hold"  # Bullet state, 'hold' means no shooting

# Function to calculate distance
def distance(x1, x2, y1, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

# Main game loop
while gameloop is True:
    myscreen.fill("#b53636")  # Background color
    myscreen.blit(bg, (0, 0))  # Blit background image
    myscreen.blit(supe, (supx, supy))  # Draw Superman

    # Rounds and enemy spawn logic
    if round > 3:
        enwaitframe = 3000
    if round > 6:
        enwaitframe = 2000
    if round > 9:
        enwaitframe = 500

    if round1 is True:
        enemspawn(2)  # Spawn 2 enemies in round 1
        number_of_enemies = 2
        enleft = 2
        round1 = False
    elif round2 is True:
        enemspawn(4)  # Spawn 4 enemies in round 2
        number_of_enemies = 4
        enleft = 4
        round2 = False
    elif round3 is True:
        enemspawn(6)  # Spawn 6 enemies in round 3
        number_of_enemies = 6
        enleft = 6
        round3 = False

    # Enemy drawing
    for enspawn in range(number_of_enemies):
        if enemisdead[enspawn] == "True":
            continue
        if en1spawnid % enwaitframe == 0:
            enementered.append(en1spawnid / enwaitframe)
        en1spawnid += 1
        if enspawn in enementered:
            myscreen.blit(enem1[enspawn], (enem1x[enspawn], enem1y[enspawn]))  # Draw enemies

    # Display health bar and player face icon
    myscreen.blit(healthbar, (92, 0))
    gameone.draw.rect(myscreen, '#ba2814', (110, 20, 550, 50))  # Full health bar background
    gameone.draw.rect(myscreen, '#0d731f', (110, 20, playerhp, 50))  # Current health bar

    # Event handling
    for i in gameone.event.get():
        if i.type == gameone.QUIT:
            gameloop = False  # Quit game

        # Keypress actions for movement and shooting
        if i.type == gameone.KEYDOWN:
            if i.key == gameone.K_RIGHT:
                supe = supright  # Move right
                supcurpos = "supesright.png"
                supechannge = 2
            if i.key == gameone.K_LEFT:
                supe = supleft  # Move left
                supcurpos = "supesleft.png"
                supechannge = -2
            if i.key == gameone.K_DOWN:
                supe = supdown  # Move down
                supechangey = 2
            if i.key == gameone.K_UP:
                supe = supup  # Move up
                supechangey = -2
            if i.key == gameone.K_SPACE:
                shootsound.play()  # Play shooting sound
                # Handle bullet creation and state
                if state == "hold":
                    bulletleftx = supx
                    bulletx = supx
                    bullety = supy
                    buldir = "right" if supe == supright else "left"  # Determine bullet direction
                    state = 'shoot'  # Change bullet state to 'shoot'

        # Stop movement when keys are released
        if i.type == gameone.KEYUP:
            supechannge = 0
            supechangey = 0

    # Update player position
    supx += supechannge
    supy += supechangey

    # Ensure player stays within screen bounds
    if supx <= 0:
        supx = 0
    elif supx >= 1150:
        supx = 1150
    if supy <= 100:
        supy = 100
    elif supy >= 530:
        supy = 530

    # Handle bullet movement
    if state == 'shoot':
        if buldir == "right":
            supbullet = lazer
            myscreen.blit(lazer, (bulletx + 80, bullety + 10))
            bulletx += 7
            if bulletx >= 1280:
                state = "hold"  # Reset bullet if it goes off screen
        elif buldir == "left":
            supbullet = lazerleft
            myscreen.blit(lazerleft, (bulletx, bullety + 10))
            bulletx -= 7
            if bulletx <= 0:
                state = "hold"  # Reset bullet if it goes off screen

    # Update the display
    gameone.display.update()

    # Control the frame rate
    clock.tick(fps)  # Keeps the frame rate consistent at 60 FPS

# Quit the game when the loop ends
gameone.quit()

