import pygame as gameone
import math
import random
gameone.init()
intcheck = True
myscreen = gameone.display.set_mode((1280, 720))
gameloop = True
icon = gameone.image.load("icon.png")
gameone.display.set_icon(icon)
gameone.display.set_caption("JLA")

# Set up frame rate control
clock = gameone.time.Clock()  # Clock object to track time and frame rate
fps = 200  # Set the desired frames per second
# from pyvidplayer import Video
# sup1intro = Video("supe1intro.mp4")
# sup1intro.set_size((1280, 720))
# while intcheck is True:
#     sup1intro.draw(myscreen, (0, 0))
#     gameone.display.update()
#     for events in gameone.event.get():
#         if events.type == gameone.KEYDOWN:
#             if events.key == gameone.K_RETURN:
#                 sup1intro.close()
#                 intcheck = False
#                 break
#         if events.type == gameone.QUIT:
#             sup1intro.close()
#             intcheck = False
#             gameloop = False
#             gameone.quit()
playerhp = 550
bulletx = 1280
bulletleftx = 720
en1spawnid = 0
bullety = 100
start = False
defeated = 0
#rounds
enwaitframe = 4000
round = 1
round1 = True
round2 = False
round3 = False
animcount = 0
#end
#sounds and music
gameone.mixer.music.load("mainscoreloop.wav")
gameone.mixer.music.set_volume(0.5)
gameone.mixer.music.play(-1)
shootsound = gameone.mixer.Sound("laser.wav")
blast = gameone.mixer.Sound("explosion.wav")
blast.set_volume(1.0)
#victory = gameone.mixer.Sound()
#end
#  all supeerman sprites
lazer = gameone.image.load("bullet.png").convert_alpha()
lazerleft = gameone.image.load("bulletleft.png").convert_alpha()
# stand left anims
supstandleft1 = gameone.image.load("supestandleft.png").convert_alpha()
supstandleft2 = gameone.image.load("supstandanim2left.png")
supstandleft = supstandleft1
# stand right anims
supstand1 = gameone.image.load("supestand.png").convert_alpha()
supstand = supstand1
supstand2 = gameone.image.load("supstandanim1.png").convert_alpha()
supstand3 = gameone.image.load("supstandanim2.png").convert_alpha()
#end
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
enem1look = gameone.image.load("enemy1.png").convert_alpha()
enem1lookright = gameone.image.load("enemy1right.png").convert_alpha()
enblast = gameone.image.load("pngegg.png").convert_alpha()
# end
dircur = "supestand.png"
countshoot = 0
uplim = 100
rightlim = 1150
leftlim = 0
downlim = 530
scount = 0
vec = gameone.math.Vector2
# loading images
bg = gameone.image.load("backnightopt.jpg").convert_alpha()
healthbar = gameone.image.load("healthbar.png").convert_alpha()
# Superman code
stanfleftanims = [supstandleft1, supstandleft2]
supe = supstand
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
# Shazam code

# shaz = gameone.image.load("shazstandleft.png")

# Enemy code
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
    for enemy in range(number):
        if enemy % 2 == 0:
            enem1.append(enem1lookright)
            enem1x.append(1150)
            enhurt.append("enemy1hurtright.png")
            envert.append("up")
            enemmove.append(-0.8)
            enemmovey.append(0.8)
        else:
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


# supe bullet
supbullet = lazer
state = "hold"
# shaz position
shazx = 1100
shazy = 340
standanims = [supstand1, supstand2, supstand3]
"""
shazstanddir = gameone.image.load("shazstandleft.png")
shazupdir = gameone.image.load("shazupleft.png")
shazdowndir = gameone.image.load("shazdownleft.png")
shazchangey = 0
shazchange = 0
"""


def distance(x1, x2, y1, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))


while gameloop is True:
    myscreen.fill("#b53636")
    myscreen.blit(bg, (0, 0))
    myscreen.blit(supe, (supx, supy))
    if round > 3:
        enwaitframe = 3000
    if round > 6:
        enwaitframe = 2000
    if round > 9:
        enwaitframe = 500
    if round1 is True:
        enemspawn(2)
        number_of_enemies = 2
        enleft = 2
        round1 = False
    elif round2 is True:
        enemspawn(4)
        number_of_enemies = 4
        enleft = 4
        round2 = False
    elif round3 is True:
        enemspawn(6)
        number_of_enemies = 6
        enleft = 6
        round3 = False
    for enspawn in range(number_of_enemies):
        if enemisdead[enspawn] == "True":
            continue
        if en1spawnid % enwaitframe == 0:
            enementered.append(en1spawnid/enwaitframe)
        en1spawnid += 1
        if enspawn in enementered:
            myscreen.blit(enem1[enspawn], (enem1x[enspawn], enem1y[enspawn]))
    myscreen.blit(supefaceic, (0, 0))
    myscreen.blit(healthbar, (92, 0))
    gameone.draw.rect(myscreen, '#ba2814', (110, 20, 550, 50))
    gameone.draw.rect(myscreen, '#0d731f', (110, 20, playerhp, 50))
    # myscreen.blit(shaz, (shazx, shazy))
    for i in gameone.event.get():
        if i.type == gameone.QUIT:
            gameloop = False

        if i.type == gameone.KEYDOWN:
            if i.key == gameone.K_RIGHT:
                supupdir = supup
                supdowndir = supdown
                supe = supright
                supcurpos = "supesright.png"
                supsshootdir = "right"
                supechannge = 2
            if i.key == gameone.K_LEFT:
                supupdir = supupleft
                supdowndir = supdownleft
                supe = supleft
                supcurpos = "supesleft.png"
                supechannge = -2
                supsshootdir = "left"
            if i.key == gameone.K_DOWN:
                supe = supdowndir
                if supsshootdir == "right":
                    supcurpos = "supesdown.png"
                elif supsshootdir == "left":
                    supcurpos = "supesdownleft.png"
                supechangey = 2
            if i.key == gameone.K_UP:
                supe = supupdir
                if supsshootdir == "right":
                    supcurpos = "supesup.png"
                elif supsshootdir == "left":
                    supcurpos = "supesupleft.png"
                supechangey = -2
            if i.key == gameone.K_SPACE:
                shootsound.play()
                """
                if number_of_enemies >= 4:
                    for scheck in range(number_of_enemies):
                        if enhurt[scheck] == "enemy1hurt.png":
                            enemmove[scheck] = 1.5
                            enem1x[scheck] += enemmove[scheck]
                        else:
                            enemmove[scheck] = -1.5
                            enem1x[scheck] += enemmove[scheck]
                        if envert[scheck] == "up":
                            enemmovey[scheck] = -1.5
                            enem1y[scheck] += enemmovey[scheck]
                        else:
                            enemmovey[scheck] = 1.5
                            enem1y[scheck] += enemmovey[scheck]
                """
                if state == "hold":
                    bulletleftx = supx
                    bulletx = supx
                    bullety = supy
                    buldir = supsshootdir
                    if supsshootdir == "right":
                        supe = supshoot
                        supcurpos = "supeshoot3.png"
                    else:
                        supe = supshootleft
                        supcurpos = "supeshoot3left.png"
                else:
                    if supsshootdir == "right":
                        supe = supfail
                        supcurpos = "supeshoot.png"
                    else:
                        supe = supfailleft
                        supcurpos = "supeshootleft.png"
                state = 'shoot'

            """
            if i.key == gameone.K_d:
                shazupdir = gameone.image.load("shazup.png")
                shazdowndir = gameone.image.load("shazdown.png")
                shaz = gameone.image.load("shazright.png")
                shazchange = 2
            if i.key == gameone.K_a:
                shazupdir = gameone.image.load("shazupleft.png")
                shazdowndir = gameone.image.load("shazdownleft.png")
                shaz = gameone.image.load("shazleft.png")
                shazchange = -2
            if i.key == gameone.K_s:
                shaz = shazdowndir
                shazchangey = 2
            if i.key == gameone.K_w:
                shaz = shazupdir
                shazchangey = -2
                """

        if i.type == gameone.KEYUP:
            supechannge = 0
            supechangey = 0
            shazchange = 0
            shazchangey = 0
            """
            if i.key == gameone.K_a:
                shazstanddir = gameone.image.load("shazstandleft.png")
            if i.key == gameone.K_d:
                shazstanddir = gameone.image.load("shazstand.png")
            shaz = shazstanddir
            """
            if i.key == gameone.K_LEFT:
                supstanddir = supstandleft
                dircur = "supestandleft.png"
            if i.key == gameone.K_RIGHT:
                supstanddir = supstand
                dircur = "supestand.png"
            if i.key == gameone.K_SPACE:
                """
                if number_of_enemies >= 4:
                    for scheck in range(number_of_enemies):
                        if enhurt[scheck] == "enemy1hurt.png":
                            enemmove[scheck] = 0.8
                            enem1x[scheck] += enemmove[scheck]
                        else:
                            enemmove[scheck] = -0.8
                            enem1x[scheck] += enemmove[scheck]
                        if envert[scheck] == "up":
                            enemmovey[scheck] = -0.8
                            enem1y[scheck] += enemmovey[scheck]
                        else:
                            enemmovey[scheck] = 0.8
                            enem1y[scheck] += enemmovey[scheck]
                    """
            supe = supstanddir
            supcurpos = dircur
    supx += supechannge
    supy += supechangey
    # shazy += shazchangey
    # shazx += shazchange

    for moven in range(number_of_enemies):
        if enemisdead[moven] == "True":
            if enemblast[moven] == 500:
                enemblast[moven] = 0
            elif enemblast[moven] > 0:
                myscreen.blit(enblast, (enemblastx[moven], enemblasty[moven]))
                enemblast[moven] += 1
            continue
        if moven in enementered:
            enem1x[moven] += enemmove[moven]
            enem1y[moven] += enemmovey[moven]

    for endamm in range(number_of_enemies):
        if enemisdead[endamm] == "True":
            continue
        if endamm in enementered:
            if distance(enem1x[endamm], supx, enem1y[endamm] + 50, supy) <= 80 or distance(enem1x[endamm], supx,
                                                                                         enem1y[endamm] + 50,
                                                                                         supy) <= 80:
                hurt = 1
                playerhp -= 0.5
                if supsshootdir == "left":
                    supe = gameone.image.load("supehurtleft.png").convert_alpha()
                else:
                    supe = gameone.image.load("supehurt.png").convert_alpha()

    if state == "shoot":
        if bulletleftx <= 0 or bulletx >= 1280:
            state = "hold"
        for endam in range(number_of_enemies):
            if enemisdead[endam] == "True":
                continue
            if endam in enementered:
                if distance(enem1x[endam], bulletleftx, enem1y[endam] + 50, bullety) <= 80 or distance(enem1x[endam],
                                                                                                       bulletx,
                                                                                                       enem1y[endam] + 50,
                                                                                                       bullety) <= 80:
                    state = 'hold'
                    enem1[endam] = gameone.image.load(enhurt[endam]).convert_alpha()
                    bulletx = 1280
                    bullety = 720
                    bulletleftx = supx
                    enem1hp[endam] -= 1
                    if enem1hp[endam] <= 0:
                        if enemisdead[endam] == "False":
                            blast.play()
                            enemblast[endam] = 1
                            enemblastx[endam] = enem1x[endam]
                            enemblasty[endam] = enem1y[endam]
                        enemisdead[endam] = "True"
                        enleft -= 1
                        enem1x[endam] = 1280
                        enem1y[endam] = 720
                else:
                    if enhurt[endam] == "enemy1hurt.png":
                        enem1[endam] = enem1look
                    else:
                        enem1[endam] = enem1lookright
        if buldir == "left":
            myscreen.blit(lazerleft, (bulletleftx, bullety + 10))
            bulletleftx -= 7
        else:
            myscreen.blit(lazer, (bulletx + 80, bullety + 10))
            bulletx += 7
    if enleft == 0:
        encheck = False
        for enwait in range(number_of_enemies):
            if enemblast[enwait] == 0:
                encheck = True
            else:
                encheck = False
                break
        if encheck is True:
            round += 1
            if round == 2:
                round2 = True
            elif round % 3 == 0:
                round3 = True
            else:
                round2 = True
    if supx <= leftlim:
        supx = leftlim
    elif supx >= rightlim:
        supx = rightlim
    if supy <= uplim:
        supy = uplim
    elif supy >= downlim:
        supy = downlim

    if shazx <= 0:
        shazx = 0
    elif shazx >= 1150:
        shazx = 1150
    if shazy <= 0:
        shazy = 0
    elif shazy >= 530:
        shazy = 530

    for enco in range(number_of_enemies):
        if enemisdead[enco] == "True":
            continue
        if enem1x[enco] <= leftlim:
            enem1[enco] = enem1look
            enemmove[enco] = 0.8
            enhurt[enco] = "enemy1hurt.png"
            enem1x[enco] += enemmove[enco]
        elif enem1x[enco] >= rightlim:
            enem1[enco] = enem1lookright
            enhurt[enco] = "enemy1hurtright.png"
            enemmove[enco] = -0.8
            enem1x[enco] += enemmove[enco]
        if enem1y[enco] <= uplim:
            envert[enco] = "down"
            enemmovey[enco] = 0.8
            enem1y[enco] += enemmovey[enco]
        elif enem1y[enco] >= downlim + 100:
            envert[enco] = "up"
            enemmovey[enco] = -0.8
            enem1y[enco] += enemmovey[enco]
            # stand animation
        if animcount <= 240:
            animcount += 1
        else:
            animcount = 0
        for i in standanims:
            if supe == i:
                if animcount <= 120:
                    supe = supstand1
                #elif animcount <= 100:
                 #   supe = supstand2
                else:
                    supe = supstand3
        for j in stanfleftanims:
            if supe == j:
                if animcount <= 120:
                    supe = supstandleft1
                #elif animcount <= 100:
                 #   supe = supstand2
                else:
                    supe = supstandleft2
    gameone.display.update()
    clock.tick(fps) 
