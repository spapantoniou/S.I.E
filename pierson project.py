import pygame
import math
import random
from pygame import mixer
import os
from network import network
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
pygame.init()

#tkclass

#screen maker
screen_width = 1500
screen_height = 780
screen = pygame.display.set_mode((screen_width,screen_height))
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)
background1 = pygame.image.load('arena1.jpg')
background = pygame.image.load('space.png')
pause_img = pygame.image.load('pause.png').convert_alpha()
start_img = pygame.image.load('reset.png').convert_alpha()
gamestartimg = pygame.image.load('start1.png').convert_alpha()
quitimg = pygame.image.load('quit.png').convert_alpha()
resumeimg =pygame.image.load('resume.png').convert_alpha()
pauseimg = pygame.image.load('pause.png').convert_alpha()
characters = pygame.image.load('selection.png').convert_alpha()
nextimg= pygame.image.load('next.png').convert_alpha()
previousimg = pygame.image.load('previous.png').convert_alpha()
selectimg = pygame.image.load('select.png').convert_alpha()
bluelvlimg = pygame.image.load('bluelvl.png').convert_alpha()
graylvlimg = pygame.image.load('graylvl.png').convert_alpha()
lvlsimg = pygame.image.load('lvls.jpg').convert_alpha()
endlessimg = pygame.image.load('endless.jpg').convert_alpha()
nextlvlimg=pygame.image.load('nextlvl.png').convert_alpha()
menuimg=pygame.image.load('menu.png').convert_alpha()
purchaseimg=pygame.image.load('purchase.png').convert_alpha()
portal1img=pygame.image.load('portal.png').convert_alpha()
signinimg =pygame.image.load('sign.png').convert_alpha()
loginimg =pygame.image.load('sign.png').convert_alpha()
signimg =pygame.image.load('signin.png').convert_alpha()
logimg =pygame.image.load('login.png').convert_alpha()
#button class
class button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_width()
        self.image = pygame.transform.scale(image,(int(width * scale),int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        screen.blit(self.image,(self.rect.x,self.rect.y))
        pos = pygame.mouse.get_pos()
        if (self.rect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1 and self.clicked == False):
                self.clicked = True
                action = True
        if (pygame.mouse.get_pressed()[0]==0):
            self.clicked = False

        return action
font = pygame.font.Font('crazy.ttf',32)
reload_button = button(1100,10,start_img,0.8)
pause_button = button(1000,10,pause_img,0.3)
start_button = button(696,320,gamestartimg,0.25)
quit_button = button(700,530,quitimg,0.1)
resume_button = button(700,630,resumeimg,1)
pause_button = button(1050,30,pauseimg,0.3) 
character_button = button(700,420,characters,1)
next_button = button(350,300,nextimg,0.75)
previous_button = button(250,300,previousimg,1)
next2_button = button(550,300,nextimg,0.75)
previous2_button = button(450,300,previousimg,1)
select_button = button(300,400,selectimg,1)
select2_button = button(500,400,selectimg,1)
select3_button = button(700,400,selectimg,1)
bluelvl1_button = button(300,250,bluelvlimg,1)
graylvl1_button = button(300,250,graylvlimg,1)
bluelvl2_button = button(400,300,bluelvlimg,1)
graylvl2_button = button(400,300,graylvlimg,1)
bluelvl3_button = button(500,350,bluelvlimg,1)
graylvl3_button = button(500,350,graylvlimg,1)
bluelvl4_button = button(600,300,bluelvlimg,1)
graylvl4_button = button(600,300,graylvlimg,1)
lvls_button = button(690,400,lvlsimg,0.3)
endless_button = button(690,300,endlessimg,0.3)
nextlvl_button = button(800,500,nextlvlimg,1)
menu_button = button(600,500,menuimg,1)
purchase_button = button(300,400,purchaseimg,1)
purchase2_button = button(900,400,purchaseimg,1)
portal_button = button(900,10,portal1img,1)
signin_button = button(900,10,signinimg,1)
login_button = button(100,10,signinimg,1)
sign_button = button(700,300,signimg,2)
log_button = button(700,200,logimg,2)
#lvl
starimg=pygame.image.load('shootingstar.png')
#player
player2img = pygame.image.load('alien.png')
player1img = pygame.image.load('ship.png')
player3img = pygame.image.load('jet.png')
player2x = 100
player2y = 300
player2x_change = 10
player2y_change = 10
class player():
    def __init__(self,image,x,y,changex,changey):
        self.image = player2img
        self.x = player2x
        self.y = player2y
        self.changex = player2x_change
        self.changey = player2y_change
    def move(self,x,y):
        key = pygame.key.get_pressed()
        self.x+=self.changex
        self.y+=self.changey
        if (key[pygame.K_LEFT]== True):
              self.changex+=15
        elif (key[pygame.K_RIGHT]== True):
              self.changex-=15
        elif (key[pygame.K_UP]== True):
            self.changey+=15
        elif (key[pygame.K_DOWN]== True):
            self.changey-=15
        screen.blit(self.image,(player2x,player2y))
dash = 0
player2_player = player(player2img,100,300,10,10)
#player2 = player(100,300,player2img,1)
#player2.draw()
enemy2img = []
#bigLaser
blaserimg=pygame.image.load('blaser.jpg')
blaserx=0
blasery=0
blaserx_change=0
blasery_change=0
#nuke
nukeimg = pygame.image.load('bomb.png')
explosionimg = pygame.image.load('explosion.png')
nukex = 100
nukey = 300
nukex_change = 0
nukey_change = 10
nukeammo = 3
explosionx=100
explosiony=300
#granny
grannypng = pygame.image.load('grandma.png')
grannyx = 2000
grannyy  = 100
grannyx_change = -1
grannyy_change = -1
#enemy1
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 10
dubli = 0
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(1490,1500))
    enemyy.append(random.randint(0,780))
    enemyx_change.append(30)
    enemyy_change.append(12)
#shieldenemys
senemyimg = []
senemyx = []
senemyy = []
senemyx_change = []
senemyy_change = []
num_of_senemies = 10
senemylife_value =3 
for i in range(num_of_senemies):
    senemyimg.append(pygame.image.load('armor.png'))
    senemyx.append(random.randint(1490,1500))
    senemyy.append(random.randint(0,780))
    senemyx_change.append(30)
    senemyy_change.append(12)
#enemy2
enemy2img = pygame.image.load('enemy2.png')
enemy2x = random.randint(1300,1500)
enemy2y = random.randint(300,580)
enemy2y_change = 75
enemy2x_change = 25
#missiles
warning1img = pygame.image.load('warning1.png')
warning1x = 1400
warning1y = 100
warnme = 0
missileimg = []
missilex = []
missiley = []
missilex_change = []
num_of_missiles = 4
for i in range(num_of_missiles):
    missileimg.append(pygame.image.load('missile.png'))
    missilex.append(random.randint(13500,13700))
    missiley.append(random.randint(0,740))
    missilex_change.append(-20)
#boss asteroids
asteroidimg = []
asteroidx = []
asteroidy = []
asteroidx_change = []
asteroidy_change = []
num_of_asteroids = 12
for i in range(num_of_asteroids):
    asteroidimg.append(pygame.image.load('asteroid.png'))
    asteroidx.append(1200)
    asteroidy.append(random.randint(0,780))
    asteroidx_change.append(-10)
    asteroidy_change.append(12)
#boss
bossimg = pygame.image.load('boo.png')
theholeimg = pygame.image.load('blackhole.png')
heartimg = pygame.image.load('heart.png')
heartx = 1200
hearty = 300
heartx_change = -3
hearty_change = -3
hole_state = 'ready'
holex = 1200
holey = 300
holex_change = -5
bossx = 1200
bossy = 390
bossy_change = 50
boolife_value = 250
asmeter = 0
bossmeter =0
#danger
danger =0
dangerimg = pygame.image.load('warning.png')
#frenzie and death
frenzie2 = 0 
#cow bullet
cowimg = pygame.image.load('cow.png')
cowx = 700
cowy = 400
cowx_change = 30
cowy_change = 15
cow_state = 'ready'
board = 5
#powerups
#powerup1
powerupimg = pygame.image.load('stickman.png')
powerupx = 1500
powerupy = random.randint(100,640)
powerupx_change = 10
powerupy_change = 10
powerme = 0
cow2img = pygame.image.load('cow.png')
cow2x = 700
cow2y = 400
cow2x_change = 30
cow2y_change = 15
cow2_state = 'ready'
powermeter = 0
#score and highscore
score_value1 = 0
score_value = 0
if os.path.exists('score.txt'):
    with open('score.txt','r') as file:
        score_value1 = int(file.read())
else:
    score_value1= 0 
life_value = 3
class healthbar():
    def __init__(self,x,y,w,h,hp,max_hp):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.hp=hp
        self.max_hp=max_hp
    def draw(self,surface):
        ratio=self.hp/self.max_hp
        pygame.draw.rect(surface,'red',(self.x,self.y,self.w,self.h))
        pygame.draw.rect(surface,'green',(self.x,self.y,self.w*ratio,self.h))
phealth_bar=healthbar(650,700,200,20,100,100)
boohealth_bar=healthbar(550,10,400,40,2000,2000)
textx = 10
texty = 10
#energy
earthimg= pygame.image.load('earth.png')
energy_value = 150
earthx = -10
earthy = 670
#laser
laserimg = []
laserx = []
lasery = []
laserx_change = []
lasery_change = []
num_of_lasers = 2
for i in range(num_of_lasers):
    laserimg.append(pygame.image.load('glaser.jpg'))
    laserx.append(random.randint(1500,1800))
    lasery.append(random.randint(250,550))
    laserx_change.append(-2)
    lasery_change.append(0)
glaserimg = []
glaserx = []
glasery = []
glaserx_change = []
glasery_change = []
num_of_glasers = 2
for i in range(num_of_lasers):
    glaserimg.append(pygame.image.load('laser.png'))
    glaserx.append(random.randint(1500,1800))
    glasery.append(random.randint(250,550))
    glaserx_change.append(-2)
    glasery_change.append(0)
#start menue
background2=pygame.image.load('background4.jpg')
background3=pygame.image.load('lvlbackground.png')


#portal
portalimg = pygame.image.load('portal.png')
portalx = 0
portaly = 0
portaluse = 10
portal_state = 'notplaced'
p = 0
#coins and diamonds
coins_value=10
if os.path.exists('score1.txt'):
    with open('score1.txt','r') as file:
        coins_value=int(file.read())
else:
    score_value1= 0
diamonds_value=10
if os.path.exists('score2.txt'):
    with open('score2.txt','r') as file:
        diamonds_value = int(file.read())
else:
    score_value1= 0
coinimg=pygame.image.load('coin.png')
diamondimg=pygame.image.load('diamond.png')
dchestimg=pygame.image.load('dchest.png')
dchestx=1100
dchesty=390
#defs for bliting imagies
def welcome():
    tet_text = font.render('Welcome to space invaders extreme',True,(200,0,200))
    screen.blit(tet_text,(500,10))
def restart_txt():
    game_text = font.render('press R to restart',True,(200,0,200))
    screen.blit(game_text,(600,440))
def game_over():
    game_text = font.render('!!GAME OVER!!',True,(255,0,255))
    screen.blit(game_text,(650,150))
def youwon():
    game_text = font.render('<YOU WON>',True,(0,255,0))
    screen.blit(game_text,(650,390))
def highscore(x,y):
    highscore = font.render('highscore :' + str(score_value1),True,(240,0,240))
    screen.blit(highscore,(x,y))
def show_lifes(x,y):
    lifes = font.render('lifes :' + str(life_value),True,(240,0,240))
    screen.blit(lifes,(x,y))
def show_score(x,y):
    score = font.render('score :' + str(score_value),True,(255,0,255))
    screen.blit(score,(x,y))
def granny(x,y):
    screen.blit(grannypng,(x,y))
def earth(x,y):
    screen.blit(earthimg,(x,y))
def blaser(x,y):
    screen.blit(blaserimg,(x,y))
def coins(x,y):
    screen.blit(coinimg,(x,y))
def show_coins(x,y):
    coins1 = font.render(str(coins_value),True,(255,0,255))
    screen.blit(coins1,(x,y))
def diamonds(x,y):
    screen.blit(diamondimg,(x,y))
def show_diamonds(x,y):
    diamond1 = font.render(str(diamonds_value),True,(255,0,255))
    screen.blit(diamond1,(x,y))
def dchest(x,y):
    screen.blit(dchestimg,(x,y)) 
def energy(x,y):
    energy= font.render('cows :'+ str(energy_value),True,(253,208,23))
    screen.blit(energy,(x,y))
def value(x,y):
    svalue = font.render('1000',True,(250,0,0))
    screen.blit(svalue,(x,y))
def value2(x,y):
    savalue = font.render('1000000',True,(250,0,0))
    screen.blit(savalue,(x,y))
def nodiamonds(x,y):
    nodia = font.render('you have inseficient diamonds',True,(250,0,0))
    screen.blit(nodia,(x,y))
def danger1(x,y):
    danger3 = font.render('!DANGER!',True,(250,0,0))
    screen.blit(danger3,(x,y))
def gamepause(x,y):
    pause = font.render('Game Is Paused',True,(250,0,250))
    screen.blit(pause,(x,y))
def frenzie(x,y):
    frenzie = font.render('boo is angry',True,(200,0,0))
    screen.blit(frenzie,(x,y))
def danger2(x,y):
    screen.blit(dangerimg,(x,y))
def star(x,y):
    screen.blit(starimg,(x,y))
def player2(x,y):
    screen.blit(player2img,(x,y))
def player(x,y):
    screen.blit(player1img,(x,y))
def player3(x,y):
    screen.blit(player3img,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def senemy(x,y,i):
    screen.blit(senemyimg[i],(x,y))
def missile(x,y,i):
    screen.blit(missileimg[i],(x,y))
def asteroid(x,y,i):
    screen.blit(asteroidimg[i],(x,y))
def portal(x,y):
    screen.blit(portalimg,(x,y))
def thehole(x,y):
    screen.blit(theholeimg,(x,y))
def enemy2(x,y):
    screen.blit(enemy2img,(x,y))
def boss(x,y):
    screen.blit(bossimg,(x,y))
def heart(x,y):
    screen.blit(heartimg,(x,y))
def boss_lifes(x,y):
    boolifes = font.render('boo lifes :' + str(boolife_value),True,(240,0,240))
    screen.blit(boolifes,(x,y))
def powerup(x,y):
    screen.blit(powerupimg,(x,y))
def warning1(x,y):
    screen.blit(warning1img,(x,y))
def laser(x,y,i):
    screen.blit(laserimg[i],(x,y))
def glaser(x,y,i):
    screen.blit(glaserimg[i],(x,y))
def nuke(x,y):
    screen.blit(nukeimg,(x,y))
def explosion(x,y):
    screen.blit(explosionimg,(x,y))
def dash1(x,y):
    screen.blit(dashimg,(x,y))
def angel(x,y):
    screen.blit(guardianimg,(x,y))
#cow shooter 
def fire_cow(x,y):
    global cow_state
    cow_state = 'fire'
    screen.blit(cowimg,(x, y + 10))
#powerup
def fire_cow2(x,y):
    global cow2_state
    cow2_state = 'fire'
    screen.blit(cow2img,(x , y - 10))
#chestd
def diamondscollision(dchestx,dchesty,cowx,cowy):
    distance = math.sqrt((math.pow(dchestx - cowx,2)) +((math.pow(dchesty - cowy,2))))
    if (distance < 80):
        return True
    else:
        return False
#detonation
def explodecolision(nukex,nukey,enemyx,enemyy):
   distance = math.sqrt((math.pow(nukex - enemyx,2)) + ((math.pow(nukey - enemyy,2))))
   if (distance < 1000):
       return True
   else:
       return False
#nuke collision
def nukecollision(nukex,nukey,cowx,cowy):
   distance = math.sqrt((math.pow(nukex - cowx,2)) + ((math.pow(nukey - cowy,2))))
   if (distance < 40):
       return True
   else:
       return False
#energy gather collision
def energycollision(player2x,player2y,earthx,earthy):
   distance = math.sqrt((math.pow(player2x - earthx,2)) + ((math.pow(player2y - earthy,2))))
   if (distance < 130):
       return True
   else:
       return False
#missile collision
def missilecollision(missilex,missiley,player2x,player2y):
   distance = math.sqrt((math.pow(missilex - player2x,2)) + ((math.pow(missiley - player2y,2))))
   if (distance < 27):
       return True
   else:
       return False
def lasercollision(laserx,lasery,player2x,player2y):
   distance = math.sqrt((math.pow(laserx - player2x,2)) + ((math.pow(lasery - player2y,2))))
   if (distance < 100):
       return True
   else:
       return False
#senemycollision
def senemyCollision(senemyx,senemyy,cowx,cowy):
   distance = math.sqrt((math.pow(senemyx - cowx,2)) + ((math.pow(senemyy - cowy,2))))
   if (distance < 40):
       return True
   else:
       return False
#collision for the player + cow against the enemy1
def isCollision(enemyx,enemyy,cowx,cowy):
   distance = math.sqrt((math.pow(enemyx - cowx,2)) + ((math.pow(enemyy - cowy,2))))
   if (distance < 40):
       return True
   else:
       return False
#solision for the player + cow against the enemy2 
def iscollision2(enemy2x,enemy2y,cowx,cowy):
   distance = math.sqrt((math.pow(enemy2x - cowx,2)) + ((math.pow(enemy2y - cowy,2))))
   if (distance < 40):
       return True
   else:
       return False
#powerup collision
def isCollision3(enemyx,enemyy,cow2x,cow2y):
   distance = math.sqrt((math.pow(enemyx - cow2x,2)) + ((math.pow(enemyy - cow2y,2))))
   if (distance < 40):
       return True
   else:
       return False
#boss to cow 1 collision
def bosscollision(bossx,bossy,cowx,cowy):
    distance = math.sqrt((math.pow(bossx - cowx,2)) +((math.pow(bossy - cowy,2))))
    if (distance < 80):
        return True
    else:
        return False
#boss to cow 2 collision
def bosscollision2(bossx,bossy,cow2x,cow2y):
    distance = math.sqrt((math.pow(bossx - cow2x,2)) +((math.pow(bossy - cow2y,2))))
    if (distance < 80):
        return True
    else:
        return False
#blackhole collision
def theholecollision(holex,holey,player2x,player2y):
   distance = math.sqrt((math.pow(holex - player2x,2)) + ((math.pow(holey - player2y,2))))
   if (distance < 150):
       return True
   else:
       return False
#hearts collision
def heartcollision(heartx,hearty,player2x,player2y):
   distance = math.sqrt((math.pow(heartx - player2x,2)) + ((math.pow(hearty - player2y,2))))
   if (distance < 50):
       return True
   else:
       return False
#asteroid collision
def astercollision(asteroidx,asteroidy,player2x,player2y):
   distance = math.sqrt((math.pow(asteroidx - player2x,2)) + ((math.pow(asteroidy - player2y,2))))
   if (distance < 50):
       return True
   else:
       return False
#death collision  
def space_death(enemyx,enemyy,player2x,player2y):
   distance = math.sqrt((math.pow(enemyx - player2x,2)) + ((math.pow(enemyy - player2y,2))))
   if (distance < 40):
       return True
   else:
       return False
#death collision for enemy2
def space_death2(enemy2x,enemy2y,player2x,player2y):
   distance = math.sqrt((math.pow(enemy2x - player2x,2)) + ((math.pow(enemy2y - player2y,2))))
   if (distance < 40):
       return True
   else:
       return False
def powerup1(powerupx,powerupy,player2x,player2y):
   distance = math.sqrt((math.pow(powerupx- player2x,2)) + ((math.pow(powerupy - player2y,2))))
   if (distance < 41):
       return True
   else:
       return False
def blowme(blaserx,enemy2x,):
   distance = math.sqrt((math.pow(blaserx- enemy2x,2)))
   if (distance < 500):
       return True
   else:
       return False
def blowme2(blaserx,bossx,):
   distance = math.sqrt((math.pow(blaserx- bossx,2)))
   if (distance < 500):
       return True
   else:
       return False
run = True
gameover_state ='log in'
#guardiam
guardian_state = 'in'
guardianimg =pygame.image.load('angel.png')
#music player
mixer.music.load("pirates.mp3")
mixer.music.play(-1)
#charachter select
charactershow = 0
ship_state = 'ship1'
if os.path.exists('score3.txt'):
    with open('score3.txt','r') as file:
        ship_state = file.read()
else:
    ship_state= 'ship1'
exploduration = 0
#lvl state
lvl1_state='notbeat'
if os.path.exists('score6.txt'):
    with open('score6.txt','r') as file:
        lvl1_state = file.read()
lvl2_state='notbeat'
lvl3_state='notbeat'
purchased_state='notpurchased'
purchased2_state='notpurchased'
dashimg = pygame.image.load('dash.png')
special_state = 'dash'
specialshow = 0
if os.path.exists('score5.txt'):
    with open('score5.txt','r') as file:
        special_state = file.read()
if os.path.exists('score4.txt'):
    with open('score4.txt','r') as file:
        purchased_state = file.read()
else:
    purchased_state= 'notpurchased'

def read_pos(str):
    str = str.split(',')
    return int(str[0]),int(str[1])
def make_pos(tup):
    return str(tup[0])+','+str(tup[1])
#startPos = read_pos(n.getPos())
#player2x = startPos[0]
#player2y = startPos[1]

if os.path.exists('ussername.txt'):
            with open('ussername.txt','r')as file:
                a = str(file.read())
                
if os.path.exists('password.txt'):
            with open('password.txt','r')as file:
                b = str(file.read())
                
if os.path.exists('ussername1.txt'):
            with open('ussername1.txt','r')as file:
                c = str(file.read())
                
if os.path.exists('password1.txt'):
            with open('password1.txt','r')as file:
                g = str(file.read())
page_state ='a'

while (run == True):
    #player2Pos = read_pos(n.send(make_pos((player2x,player2y))))
    #player2x = player2Pos[0]
    #player2y = player2Pos[1]
    if (gameover_state=='enter'):
        screen.fill((0,0,0))
        screen.blit(background2,(0,0))
        if os.path.exists('ussername.txt'):
            with open('ussername.txt','r')as file:
                a = str(file.read())
        if os.path.exists('ussername1.txt'):
            with open('ussername1.txt','r')as file:
                c = str(file.read())
        if(login_button.draw()==True):
            if(c in a and g in b):
                gameover_state='ready'
        if(quit_button.draw()==True):
                gameover_state='log in'
        
    if (page_state == 'gui'):
        def saveFile():
            c = Entry.get(myentry)
            with open('ussername1.txt','w')as file:
                file.write(str(c))
                
            g = Entry.get(myentry1)
            with open('password1.txt','w')as file:
                file.write(str(g))
        window = Tk()
        label = tk.Label(window, text='Welcome\n \n plaese log in to continue',font=('Arial',18))
        label.pack(padx=40,pady=40)
        label1 = tk.Label(window, text='ussername',font=('Arial',18))
        label1.pack(padx=10,pady=10)
        myentry = tk.Entry(window)
        myentry.pack()
        label2 = tk.Label(window, text='password',font=('Arial',18))
        label2.pack(padx=10,pady=10)
        myentry1 = tk.Entry(window)
        myentry1.pack()
        button = Button(text = '->', command = saveFile)
        button1 = Button(text = 'exit', command = window.destroy)
        button.pack()
        button1.pack()
        c = Entry.get(myentry)
        g = Entry.get(myentry1)
        
        window.mainloop()
        if os.path.exists('ussername.txt'):
            with open('ussername.txt','r')as file:
                a = str(file.read())
        if os.path.exists('ussername1.txt'):
            with open('ussername1.txt','r')as file:
                c = str(file.read())
        if os.path.exists('password.txt'):
            with open('password.txt','r')as file:
                b = str(file.read())
        if os.path.exists('password1.txt'):
            with open('password1.txt','r')as file:
                g = str(file.read())
        if(c in a and g in b):
                gameover_state='ready'
        page_state='a'
    if (page_state == 'gui1'):
        def saveFile():
            #file = filedialog.asksaveasfile(initialdir= 'G:\\ergasies html-Copy',
                                       #     defaultextension='.txt',
                                        #    filetypes =[('txt file','.txt'),
                                         #               ('HTML file','.html')])
            #if file is None:
            #    return
            #filetext = str(text.get(1.0,END))
            #file.write(filetext)
            #file.close()
                if os.path.exists('ussername.txt'):
                    with open('ussername.txt','r')as file:
                        a = str(file.read())
                a = a+Entry.get(myentry2)
                with open('ussername.txt','w')as file:
                    file.write(str(a))
                if os.path.exists('password.txt'):
                    with open('password.txt','r')as file:
                        b = str(file.read())   
                b = b+Entry.get(myentry1)
                with open('password.txt','w')as file:
                    file.write(str(b))
        window = Tk()
        label = tk.Label(window, text='Welcome to space invaders extreme \n \n plaese create an account to continue',font=('Arial',18))
        label.pack(padx=40,pady=40)
        label1 = tk.Label(window, text='ussername',font=('Arial',18))
        label1.pack(padx=10,pady=10)
        myentry2 = tk.Entry(window)
        myentry2.pack()
        a = myentry2
        if os.path.exists('ussername.txt'):
                    with open('ussername.txt','r')as file:
                        a = str(file.read())
        with open('ussername.txt','w')as file:
                    file.write(str(a))
        label2 = tk.Label(window, text='password',font=('Arial',18))
        label2.pack(padx=10,pady=10)
        myentry1 = tk.Entry(window)
        myentry1.pack()
        button = Button(text = '->', command = saveFile)
        button1 = Button(text = 'exit', command = window.destroy)
        button.pack()
        button1.pack()
        b = myentry1
        if os.path.exists('password.txt'):
                    with open('password.txt','r')as file:
                        b = str(file.read())
        with open('password.txt','w')as file:
                    file.write(str(b))
        window.mainloop()
        page_state='a'
    if (gameover_state == 'log in'):
        screen.fill((0,0,0))
        screen.blit(background2,(0,0))
        if (sign_button.draw()==True):
            page_state = 'gui1'
        if (log_button.draw()==True):
            page_state = 'gui'
    if (gameover_state == 'lvl3'):
        screen.fill((50,50,50))
        screen.blit(background,(0,0))
        if(ship_state == 'ship1'):
            player2(player2x,player2y)
        if(ship_state == 'ship2'):
            player(player2x,player2y)
        if(ship_state=='ship3'):
            player3(player2x,player2y)
        key = pygame.key.get_pressed()
        #pause
        if (pause_button.draw()==True):
            gameover_state ='pause'
        #restart
        if (reload_button.draw()== True):
            life_value = 3
            danger = 0
            energy_value = 150
            bossx =1200
            boolife_value = 250
            powermeter = 0
            bossmeter = 0
            with open('score1.txt','w') as file:
                    file.write(str(coins_value))
            with open('score2.txt','w') as file:
                    file.write(str(diamonds_value))
            if (score_value > score_value1):
                score_value1 = score_value
                with open('score.txt','w') as file:
                    file.write(str(score_value1))
            score_value = 0
            for i in range(num_of_enemies):
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
                enemy2x = random.randint(1820,1830)
                enemy2y = random.randint(320,580)
            for i in range(num_of_missiles):
                missilex[i] = random.randint(13500,13700)
                missiley[i] = random.randint(0,740)
    if(gameover_state=='chestroom'):
        screen.fill((50,50,50))
        dchest(dchestx,dchesty)
        diacollision=diamondscollision(dchestx,dchesty,cow2x,cow2y)
        if(quit_button.draw()==True):
            diamonds_value+=50
        if (pause_button.draw()==True):
            gameover_state ='pause' 
    if(gameover_state=='lvl2'):
        screen.fill((50,50,50))
        screen.blit(background,(0,0))
        if(ship_state == 'ship1'):
            player2(player2x,player2y)
        if(ship_state == 'ship2'):
            player(player2x,player2y)
        if(ship_state=='ship3'):
            player3(player2x,player2y)
        key = pygame.key.get_pressed()
        #pause
        if (pause_button.draw()==True):
            gameover_state ='pause'
        #restart
        if (reload_button.draw()== True):
            life_value = 3
            danger = 0
            energy_value = 150
            bossx =1200
            boolife_value = 250
            powermeter = 0
            bossmeter = 0
            with open('score1.txt','w') as file:
                    file.write(str(coins_value))
            with open('score2.txt','w') as file:
                    file.write(str(diamonds_value))
            if (score_value > score_value1):
                score_value1 = score_value
                with open('score.txt','w') as file:
                    file.write(str(score_value1))
            score_value = 0
            for i in range(num_of_enemies):
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
                enemy2x = random.randint(1820,1830)
                enemy2y = random.randint(320,580)
            for i in range(num_of_missiles):
                missilex[i] = random.randint(13500,13700)
                missiley[i] = random.randint(0,740)
        #player movement
        if (key[pygame.K_LEFT]== True):
           player2x_change = -15
           player2y_change = 0
           if (key[pygame.K_f]==True):
              if (dash<2):
                  if(energy_value >= 20):
                    dash +=1
                    player2x = player2x -100
                    energy_value -=2
        elif (key[pygame.K_RIGHT]== True):
            player2x_change = +15
            player2y_change = 0
            if (key[pygame.K_f]==True):
               if (dash<2):
                  if(energy_value >= 20):
                      dash +=1
                      player2x = player2x +100
                      energy_value -=2
        elif (key[pygame.K_UP]== True):
            player2y_change = -15
            player2x_change = 0
            if (key[pygame.K_f]==True):
               if (dash<2):
                   if(energy_value >= 20):
                      dash +=1
                      player2y = player2y -100
                      energy_value -=2
        elif (key[pygame.K_DOWN]== True):
            player2y_change = +15
            player2x_change = 0
            if (key[pygame.K_f]==True):
               if (dash<2):
                   if(energy_value >= 20):
                      dash +=1
                      player2y = player2y +100
                      energy_value -=2
        elif (key[pygame.K_a]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_d]== True):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_w]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_s]== False):
            player2x_change = 0
            player2y_change = 0
        if (key[pygame.K_f]==False):
               dash = 0 
        #wasd
        if (key[pygame.K_a]== True):
            player2x_change = -15
        elif (key[pygame.K_d]== True):
            player2x_change = +15
        elif (key[pygame.K_w]== True):
            player2y_change = -15
        elif (key[pygame.K_s]== True):
            player2y_change = +15
        elif (key[pygame.K_a]== False):
            player2_change = 0
        elif (key[pygame.K_d]== True):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_w]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_s]== False):
            player2x_change = 0
            player2y_change = 0
           
        collis = energycollision(player2x,player2y,earthx,earthy)
        earth(earthx,earthy)
        if (collis):
            energy_value +=2
        if(energy_value >=150):
            energy_value = 150
        #nuke method
        nukey += nukey_change
        nuke(nukex, nukey)
        if (special_state== 'nuke'):
            if (key[pygame.K_p]):
                nukex= player2x
                nukey= player2y
                nukey_change=10
                nuke(nukex, nukey)
                
                nukeammo -=1
        if(special_state=='blaser'):
            if(energy_value>=1):
                if(key[pygame.K_p]):
                    blaserx=player2x
                    blasery=player2y
                    blaser(blaserx,blasery)
                    energy_value-=1
        for i in range(num_of_enemies):
            nuklision = nukecollision(nukex,nukey,enemyx[i], enemyy[i])
            explolision = explodecolision(nukex,nukey,enemyx[i], enemyy[i])
            if(nuklision):
                nuke(2000,2000)
                if(explolision):
                        explosionx=enemyx[i]
                        explosiony=enemyy[i] 
                        explosion(explosionx,explosiony)
                        enemyx[i] = random.randint(1500,1510)
                        enemyy[i] = random.randint(0,1000)
        for i in range(num_of_enemies):
            if(enemyx[i]<=1400):
                blowmee=blowme(blaserx,enemyx[i])
                if(blowmee):
                    score_value+=1
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
        #cow shotting method
        if(energy_value >= 2):
           if (key[pygame.K_SPACE]== True):
               if (cow_state == 'ready'):
                   cow_sound = mixer.Sound("pew.mp3")
                   cow_sound.play()
                   cowx = player2x
                   cowy = player2y
                   fire_cow(cowx,cowy)
                   energy_value -=2
               if (powerme>=1):
                   if (cow2_state == 'ready'):
                       cow2_sound = mixer.Sound("pew.mp3")
                       cow2_sound.play()
                       cow2x = player2x
                       cow2y = player2y
                       fire_cow2(cow2x,cow2y)
                       energy_value -=2
        player2x += player2x_change
        #powerup
        powercollision = powerup1(powerupx,powerupy,player2x,player2y)
        if (powermeter>=50):
            powerup(powerupx,powerupy)
            powerupx += powerupx_change
            powerupy += powerupy_change
            if (powerupy >= 640):
                powerupy_change = - 2
                powerupx_change = - 2
            if (powerupy <= 0):
                powerupy_change = 2
                powerupx_change = -2
            if (powerupx <=0):
                powerupx = 40000
            if (powercollision):
                powerupx = 40000
                powerme = 2
        #player boundries
        if ( player2x <= 0 ):
            player2x = 0
        elif ( player2x >= 1440):
            player2x = 1440
        elif ( player2y >= 690):
            player2y = 690
        elif (player2y <= 0):
            player2y = 0
        #death image and conditions  
        for i in range(num_of_enemies):
            spacedeath = space_death(enemyx[i], enemyy[i], player2x,player2y)
            spacedeath2 = space_death2(enemy2x, enemy2y, player2x,player2y)
            if (spacedeath or enemyx[i]<= 0 or spacedeath2 or enemy2x <= 0):
                life_value -= 1
                player2x = 100
                player2y = 390
                powermeter = 0
                powerme = 0
                enemyx[i] = random.randint(1300,1400)
                enemyy[i] = random.randint(0,1000)
                enemy2x = 2500
                enemy2y = 500
                if (guardian_state=='notin'):
                    if (life_value <= 0):
                       life_value = 0
                       gameover_state = 'ready1'
                if(guardian_state =='in'):
                    if (life_value<=0):
                        life_value = 3
                        guardian_state = 'notin'
                        purchased2_state = 'notpurchased'
            #enemy movement
            enemyy[i] += enemyy_change[i]
            if ( enemyy[i] >= 920):
                enemyy_change[i] = -5
                enemyx[i] -= enemyx_change[i]
            elif (enemyy[i] <= 0):
                enemyy_change[i] = 5
                enemyx[i] -= enemyx_change[i]
            if (enemyx[i] <=0):
                enemyx[i]= 1500
            if (score_value >= 20):
                if ( enemyy[i] >= 920):
                   enemyy_change[i] = -5.9
                   enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                    enemyy_change[i] = 5.9
                    enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                        enemyx[i]= 1500
            if (score_value >= 90):
                if ( enemyy[i] >= 920):
                        enemyy_change[i] = -7.7
                        enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                     enemyy_change[i] = 7.7
                     enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                     enemyx[i]= 1500
            if (score_value >= 120):
                if ( enemyy[i] >= 920):
                   enemyy_change[i] = -8.3
                   enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                   enemyy_change[i] = 8.3
                   enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                    enemyx[i]= 1500
            enemy(enemyx[i],enemyy[i],i)
            #enemy2 movement
            if (score_value >= 50):
               enemy2y += enemy2y_change
               if (enemy2y >= 580):
                  enemy2y_change = -3
                  enemy2x -= enemy2x_change 
               elif (enemy2y <= 250):
                  enemy2y_change = 3
                  enemy2x -= enemy2x_change
               elif (enemy2x <=0):
                  enemy2x= 2500
               enemy2(enemy2x,enemy2y)
            if (score_value >= 80):
               enemy2y += enemy2y_change
               if (enemy2y >= 580):
                  enemy2y_change = -4
                  enemy2x -= enemy2x_change 
               elif (enemy2y <= 250):
                  enemy2y_change = 4
                  enemy2x -= enemy2x_change
               elif (enemy2x <=0):
                  enemy2x= 2500
               enemy2(enemy2x,enemy2y)
            if (score_value >= 140):
               enemy2y += enemy2y_change
               if (enemy2y >= 580):
                  enemy2y_change = -4.5
                  enemy2x -= enemy2x_change 
               elif (enemy2y <= 250):
                  enemy2y_change = 4.5
                  enemy2x -= enemy2x_change
               elif (enemy2x <=0):
                  enemy2x= 2500
               enemy2(enemy2x,enemy2y)
            #cow to enemy1 collision
            collision = isCollision(enemyx[i], enemyy[i],cowx,cowy)
            if (collision):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cowy = 400
                cow_state = 'ready'
                score_value +=1
                powermeter +=1
                bossmeter +=1
                coins_value+=10
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
            collision3 = isCollision3(enemyx[i], enemyy[i],cow2x,cow2y)
            if (collision3):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cow2y = 400
                cow2_state = 'ready'
                score_value +=1
                powermeter += 1
                bossmeter +=1
                coins_value+=10
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
            #cow to enemy2 collision
            collision2 = iscollision2(enemy2x,enemy2y,cowx,cowy)
            if (collision2):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cowy = 400
                cow_state = 'ready'
                score_value +=5
                powermeter += 5
                bossmeter +=1
                coins_value+=10
                enemy2x = 2500
                enemy2y = 500
        #missiles
        if (score_value >= 75):
            for i in range(num_of_missiles):
                missilex[i] += missilex_change[i]
                if (missilex[i]<=0):
                    missilex[i] = random.randint(13500,13700)
                    missiley[i] = random.randint(0,740)
                    warnme = 0
                missile(missilex[i],missiley[i],i)
                missiledeath = missilecollision(missilex[i],missiley[i],player2x,player2y)
                if (missiledeath):
                    life_value -=1
                    missilex[i] = random.randint(13500,13700)
                    player2x = 100
                    player2y = 390
                    powermeter = 0
                    powerme = 0
                if (life_value <= 0):
                   life_value = 0 
                   for j in range(num_of_enemies):
                       enemyx[j] = -1
                       enemy2y = -1
                       game_over()
                   for j in range(num_of_missiles):
                       missiley[j]= -2000
                if(missilex[i]<= 7000):
                    warning1(warning1x,warning1y)
                    warning1y = missiley[i]
                if(missilex[i]<=1500):
                    warning1(10000,20000)
        #cow state 
        show_score(textx,texty)
        show_lifes(200,10)
        highscore(1200,10)
        energy(10,50)
        if (cowy <= 0 or cowx >=1860):
            cowy = 400
            cowx = 700
            cow_state = 'ready'
        if (cow_state =='fire'):
            fire_cow(cowx,cowy)
            cowx += cowx_change
        if (cow2y <= 0 or cow2x >=1860):
            cow2y = 400
            cow2x = 700
            cow2_state = 'ready'
        if (cow2_state == 'fire'):
            fire_cow2(cow2x,cow2y)
            cow2x += cow2x_change
        player2y += player2y_change
        if(score_value>=200):
            lvl2_state='beat'
            youwon()
            for i in range(num_of_enemies):
                enemyx[i] = 222210
                enemyy[i] = 222210
                enemy2x = 222210
                enemy2y = 222210
            if(menu_button.draw()==True):
                gameover_state='lvl'
                life_value = 3
                danger = 0
                energy_value = 150
                bossx =1200
                boolife_value = 250
                powermeter = 0
                bossmeter = 0
                if (score_value > score_value1):
                    score_value1 = score_value
                score_value = 0
                for i in range(num_of_enemies):
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
                    enemy2x = random.randint(1820,1830)
                    enemy2y = random.randint(320,580)
                for i in range(num_of_missiles):
                    missilex[i] = random.randint(13500,13700)
                    missiley[i] = random.randint(0,740)
            if(nextlvl_button.draw()==True):
                gameover_state='lvl3'
                life_value = 3
                danger = 0
                energy_value = 150
                bossx =1200
                boolife_value = 250
                powermeter = 0
                bossmeter = 0
                if (score_value > score_value1):
                    score_value1 = score_value
                score_value = 0
                for i in range(num_of_enemies):
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
                    enemy2x = random.randint(1820,1830)
                    enemy2y = random.randint(320,580)
                for i in range(num_of_missiles):
                    missilex[i] = random.randint(13500,13700)
                    missiley[i] = random.randint(0,740)
    if(gameover_state=='lvl1'):
        screen.fill((0,0,0))
        screen.fill((50,50,50))
        screen.blit(background,(0,0))
        if(ship_state == 'ship1'):
            player2(player2x,player2y)
        if(ship_state == 'ship2'):
            player(player2x,player2y)
        if(ship_state=='ship3'):
            player3(player2x,player2y)
        key = pygame.key.get_pressed()
        #pause
        if (pause_button.draw()==True):
            gameover_state ='pause'
        #restart
        if (reload_button.draw()== True):

            life_value = 3
            danger = 0
            energy_value = 150
            bossx =1200
            boolife_value = 250
            powermeter = 0
            bossmeter = 0
            if (score_value > score_value1):
                score_value1 = score_value
            score_value = 0
            for i in range(num_of_enemies):
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
                enemy2x = random.randint(1820,1830)
                enemy2y = random.randint(320,580)
            for i in range(num_of_missiles):
                missilex[i] = random.randint(13500,13700)
                missiley[i] = random.randint(0,740)
        #player movement

        if (key[pygame.K_LEFT]== True):
           player2x_change = -15
           player2y_change = 0
           if (key[pygame.K_f]==True):
              if (dash<2):
                  if(energy_value >= 20):
                    dash +=1
                    player2x = player2x -100
                    energy_value -=2
        elif (key[pygame.K_RIGHT]== True):
            player2x_change = +15
            player2y_change = 0
            if (key[pygame.K_f]==True):
               if (dash<2):
                  if(energy_value >= 20):
                      dash +=1
                      player2x = player2x +100
                      energy_value -=2
        elif (key[pygame.K_UP]== True):
            player2y_change = -15
            player2x_change = 0
            if (key[pygame.K_f]==True):
               if (dash<2):
                   if(energy_value >= 20):
                      dash +=1
                      player2y = player2y -100
                      energy_value -=2
        elif (key[pygame.K_DOWN]== True):
            player2y_change = +15
            player2x_change = 0
            if (key[pygame.K_f]==True):
               if (dash<2):
                   if(energy_value >= 20):
                      dash +=1
                      player2y = player2y +100
                      energy_value -=2
        elif (key[pygame.K_a]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_d]== True):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_w]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_s]== False):
            player2x_change = 0
            player2y_change = 0
        if (key[pygame.K_f]==False):
               dash = 0 
        #wasd
        if (key[pygame.K_a]== True):
            player2x_change = -15
        elif (key[pygame.K_d]== True):
            player2x_change = +15
        elif (key[pygame.K_w]== True):
            player2y_change = -15
        elif (key[pygame.K_s]== True):
            player2y_change = +15
        elif (key[pygame.K_a]== False):
            player2_change = 0
        elif (key[pygame.K_d]== True):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_w]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_s]== False):
            player2x_change = 0
            player2y_change = 0
           
        collis = energycollision(player2x,player2y,earthx,earthy)
        earth(earthx,earthy)
        if (collis):
            energy_value +=2
        if(energy_value >=150):
            energy_value = 150
        #nuke method
        nukey += nukey_change
        nuke(nukex, nukey)
        if (ship_state == 'ship3'):
            if (key[pygame.K_p]):
                nukex= player2x
                nukey= player2y
                nukey_change=10
                nuke(nukex, nukey)
                nukeammo -=1
        if(ship_state == 'ship2'):
            if(energy_value>=1):
                if(key[pygame.K_p]):
                    blaserx=player2x
                    blasery=player2y
                    blaser(blaserx,blasery)
                    energy_value-=1
        for i in range(num_of_enemies):
            nuklision = nukecollision(nukex,nukey,enemyx[i], enemyy[i])
            explolision = explodecolision(nukex,nukey,enemyx[i], enemyy[i])
            if(nuklision):
                nuke(2000,2000)
                if(explolision):
                        explosionx=enemyx[i]
                        explosiony=enemyy[i] 
                        explosion(explosionx,explosiony)
                        enemyx[i] = random.randint(1500,1510)
                        enemyy[i] = random.randint(0,1000)
        for i in range(num_of_enemies):
            if(enemyx[i]<=1400):
                blowmee=blowme(blaserx,enemyx[i])
                if(blowmee):
                    score_value+=1
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
        #cow shotting method
        if(energy_value >= 2):
           if (key[pygame.K_SPACE]== True):
               if (cow_state == 'ready'):
                   cow_sound = mixer.Sound("pew.mp3")
                   cow_sound.play()
                   cowx = player2x
                   cowy = player2y
                   fire_cow(cowx,cowy)
                   energy_value -=2
               if (powerme>=1):
                   if (cow2_state == 'ready'):
                       cow2_sound = mixer.Sound("pew.mp3")
                       cow2_sound.play()
                       cow2x = player2x
                       cow2y = player2y
                       fire_cow2(cow2x,cow2y)
                       energy_value -=2
        player2x += player2x_change
        #powerup
        powercollision = powerup1(powerupx,powerupy,player2x,player2y)
        if (powermeter>=50):
            powerup(powerupx,powerupy)
            powerupx += powerupx_change
            powerupy += powerupy_change
            if (powerupy >= 640):
                powerupy_change = - 2
                powerupx_change = - 2
            if (powerupy <= 0):
                powerupy_change = 2
                powerupx_change = -2
            if (powerupx <=0):
                powerupx = 40000
            if (powercollision):
                powerupx = 40000
                powerme = 2
        #player boundries
        if ( player2x <= 0 ):
            player2x = 0
        elif ( player2x >= 1440):
            player2x = 1440
        elif ( player2y >= 690):
            player2y = 690
        elif (player2y <= 0):
            player2y = 0
        #death image and conditions  
        for i in range(num_of_enemies):
            spacedeath = space_death(enemyx[i], enemyy[i], player2x,player2y)
            spacedeath2 = space_death2(enemy2x, enemy2y, player2x,player2y)
            if (spacedeath or enemyx[i]<= 0 or spacedeath2 or enemy2x <= 0):
                life_value -= 1
                player2x = 100
                player2y = 390
                powermeter = 0
                powerme = 0
                enemyx[i] = random.randint(1300,1400)
                enemyy[i] = random.randint(0,1000)
                enemy2x = 2500
                enemy2y = 500
                if (life_value <= 0):
                   life_value = 0
                   gameover_state = 'ready1'
            
            #enemy movement
            enemyy[i] += enemyy_change[i]
            if ( enemyy[i] >= 920):
                enemyy_change[i] = -4
                enemyx[i] -= enemyx_change[i]
            elif (enemyy[i] <= 0):
                enemyy_change[i] = 4
                enemyx[i] -= enemyx_change[i]
            if (enemyx[i] <=0):
                enemyx[i]= 1500
            if (score_value >= 20):
                if ( enemyy[i] >= 920):
                   enemyy_change[i] = -4.9
                   enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                    enemyy_change[i] = 4.9
                    enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                        enemyx[i]= 1500
            if (score_value >= 90):
                if ( enemyy[i] >= 920):
                        enemyy_change[i] = -5.7
                        enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                     enemyy_change[i] = 5.7
                     enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                     enemyx[i]= 1500
            if (score_value >= 120):
                if ( enemyy[i] >= 920):
                   enemyy_change[i] = -6.3
                   enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                   enemyy_change[i] = 6.3
                   enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                    enemyx[i]= 1500
            enemy(enemyx[i],enemyy[i],i)
            #cow to enemy1 collision
            collision = isCollision(enemyx[i], enemyy[i],cowx,cowy)
            if (collision):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cowy = 400
                cow_state = 'ready'
                score_value +=1
                powermeter +=1
                bossmeter +=1
                coins_value+=10
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
            collision3 = isCollision3(enemyx[i], enemyy[i],cow2x,cow2y)
            if (collision3):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cow2y = 400
                cow2_state = 'ready'
                score_value +=1
                powermeter += 1
                bossmeter +=1
                coins_value+=10
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
        #armoredenemies
        for i in range(num_of_senemies):
            if(score_value>=50):
                senemyy[i] += senemyy_change[i]
                if ( senemyy[i] >= 920):
                    senemyy_change[i] = -4
                    senemyx[i] -= senemyx_change[i]
                elif (senemyy[i] <= 0):
                    senemyy_change[i] = 4
                    senemyx[i] -= senemyx_change[i]
                if (senemyx[i] <=0):
                    senemyx[i]= 1500
                if (score_value >= 20):
                    if ( senemyy[i] >= 920):
                       senemyy_change[i] = -4.9
                       senemyx[i] -= senemyx_change[i]
                    elif (senemyy[i] <= 0):
                        senemyy_change[i] = 4.9
                        senemyx[i] -= senemyx_change[i]
                    elif (senemyx[i] <=0):
                            senemyx[i]= 1500
                if (score_value >= 90):
                    if ( senemyy[i] >= 920):
                            senemyy_change[i] = -5.7
                            senemyx[i] -= senemyx_change[i]
                    elif (senemyy[i] <= 0):
                         senemyy_change[i] = 5.7
                         senemyx[i] -= enemyx_change[i]
                    elif (senemyx[i] <=0):
                         senemyx[i]= 1500
                if (score_value >= 120):
                    if ( senemyy[i] >= 920):
                       senemyy_change[i] = -6.3
                       senemyx[i] -= senemyx_change[i]
                    elif (senemyy[i] <= 0):
                       senemyy_change[i] = 6.3
                       senemyx[i] -= senemyx_change[i]
                    elif (senemyx[i] <=0):
                        senemyx[i]= 1500
                senemy(senemyx[i],senemyy[i],i)
            scollision = senemyCollision(senemyx[i], senemyy[i],cowx,cowy)
            if (scollision):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cowy = 400
                cow_state = 'ready'
                score_value +=1
                powermeter +=1
                bossmeter +=1
                senemylife_value-=1
                coins_value+=1
                if(senemylife_value<= 0):
                    senemyx[i] = random.randint(1500,1510)
                    senemyy[i] = random.randint(0,1000)
            collision3 = isCollision3(enemyx[i], enemyy[i],cow2x,cow2y)
        if(score_value>=150):
            lvl1_state='beat'
            youwon()
            for i in range(num_of_enemies):
                enemyx[i] = 222210
                enemyy[i] = 222210
            for i in range(num_of_senemies):
                senemyx[i] = 22222210
                senemyy[i]=2222210
            if(menu_button.draw()==True):
                gameover_state='lvl'
                life_value = 3
                danger = 0
                energy_value = 150
                bossx =1200
                boolife_value = 250
                powermeter = 0
                bossmeter = 0
                if (score_value > score_value1):
                    score_value1 = score_value
                score_value = 0
                for i in range(num_of_enemies):
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
                    enemy2x = random.randint(1820,1830)
                    enemy2y = random.randint(320,580)
                for i in range(num_of_missiles):
                    missilex[i] = random.randint(13500,13700)
                    missiley[i] = random.randint(0,740)
            if(nextlvl_button.draw()==True):
                gameover_state='lvl2'
                life_value = 3
                danger = 0
                energy_value = 150
                bossx =1200
                boolife_value = 250
                powermeter = 0
                bossmeter = 0
                if (score_value > score_value1):
                    score_value1 = score_value
                score_value = 0
                for i in range(num_of_enemies):
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
                    enemy2x = random.randint(1820,1830)
                    enemy2y = random.randint(320,580)
                for i in range(num_of_missiles):
                    missilex[i] = random.randint(13500,13700)
                    missiley[i] = random.randint(0,740)
        if(player2y>=3000):
            gameover_state='chestroom'
        show_score(textx,texty)
        show_lifes(200,10)
        highscore(1200,10)
        energy(10,50)
        if (cowy <= 0 or cowx >=1860):
            cowy = 400
            cowx = 700
            cow_state = 'ready'
        if (cow_state =='fire'):
            fire_cow(cowx,cowy)
            cowx += cowx_change
        if (cow2y <= 0 or cow2x >=1860):
            cow2y = 400
            cow2x = 700
            cow2_state = 'ready'
        if (cow2_state == 'fire'):
            fire_cow2(cow2x,cow2y)
            cow2x += cow2x_change
        player2y += player2y_change
    if(gameover_state=='selection'):
        screen.fill((0,0,0))
        screen.blit(background3,(0,0))
        coins(10,10)
        show_coins(30,7)
        diamonds(10,40)
        show_diamonds(30,37)
        if(lvls_button.draw()==True):
            gameover_state='lvl'
        if(endless_button.draw()==True):
            gameover_state='notready'
        if(quit_button.draw()==True):
            gameover_state = 'ready'
    if(gameover_state=='lvl'):
        screen.fill((0,0,0))
        screen.blit(background3,(0,0))
        star(320,250)
        coins(10,10)
        show_coins(30,7)
        diamonds(10,40)
        show_diamonds(30,37)
        if(lvl1_state=='notbeat'):
            if(bluelvl1_button.draw()==True):
                gameover_state='lvl1'
        elif(lvl1_state=='beat'):
            if(graylvl1_button.draw()==True):
                gameover_state='lvl1'
        if(lvl2_state=='notbeat'):
            if(graylvl2_button.draw()==True):
                gameover_state='lvl2'
        if(bluelvl2_button.draw()==True):
            gameover_state='lvl2'
        if(lvl3_state=='notbeat'):
            if(graylvl3_button.draw()==True):
                gameover_state='lvl3'
        if(bluelvl3_button.draw()==True):
            gameover_state='lvl3'
        if(quit_button.draw()==True):
            gameover_state = 'selection'
    if (gameover_state == 'change'):
        screen.fill((0,0,0))
        screen.blit(background2,(0,0))
        coins(10,10)
        show_coins(30,7)
        diamonds(10,40)
        show_diamonds(30,37)
        if (charactershow == 0 ):
            player2(300,300)
            if(next_button.draw()==True):
                charactershow = 1
            if(select_button.draw()==True):
                ship_state = 'ship1'
        elif(charactershow ==1):
            player(300,300)
            if(next_button.draw()==True):
                charactershow = 2
            if(previous_button.draw()==True):
                charactershow = 0
            if(purchased_state=='notpurchased'):
                diamonds(300,370)
                value(320,360)
                if(purchase_button.draw()==True):
                    if(diamonds_value >=100):
                        purchased_state='purchased'
                        with open('score4.txt','w') as file:
                            file.write(purchased_state)
                        diamonds_value-=1000
                    if(diamonds_value<1000 ):
                        nodiamonds(700,20)
            if(purchased_state=='purchased'):
                if(select_button.draw()==True):
                 ship_state = 'ship2'
        elif(charactershow==2):
            player3(300,300)
            if(previous_button.draw()==True):
                charactershow = 1
            if(select_button.draw()==True):
                 ship_state = 'ship3'
        if (specialshow == 0):
            dash1(500,300)
            if (next2_button.draw()== True):
                specialshow = 1
            if (select2_button.draw()==True):
                special_state = 'dash'
        if (specialshow == 1):
            blaser(500,300)
            if (next2_button.draw()== True):
                specialshow= 2
            if (previous2_button.draw()==True):
                specialshow = 0
            if (select2_button.draw()==True):
                special_state = 'blaser'
        if (specialshow == 2):
            nuke(500,300)
            if (next2_button.draw()== True):
                specialshow= 3
            if (previous2_button.draw()==True):
                specialshow = 1
            if (select2_button.draw()==True):
                special_state = 'nuke'
        if (specialshow == 3):
            portal(500,300)
            if (previous2_button.draw()==True):
                specialshow = 2
            if (select2_button.draw()==True):
                special_state ='portal'
        if(quit_button.draw()==True):
            gameover_state='ready'
    if (gameover_state == 'pause'):
        screen.fill((0,0,0))
        gamepause(620,100)
        coins(10,10)
        show_coins(30,7)
        diamonds(10,40)
        show_diamonds(30,37)
        if (resume_button.draw()==True):
            gameover_state = 'notready'
        if(quit_button.draw()==True):
                gameover_state = 'ready'
                life_value = 3
                phealth_bar.hp=100
                danger = 0
                energy_value = 150
                bossx =1200
                boolife_value = 250
                powermeter = 0
                bossmeter = 0
                with open('score1.txt','w') as file:
                        file.write(str(coins_value))
                with open('score2.txt','w') as file:
                        file.write(str(diamonds_value))
                if (score_value > score_value1):
                    score_value1 = score_value
                    with open('score.txt','w') as file:
                        file.write(str(score_value1))
                score_value = 0
                for i in range(num_of_enemies):
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
                    enemy2x = random.randint(1820,1830)
                    enemy2y = random.randint(320,580)
                for i in range(num_of_missiles):
                    missilex[i] = random.randint(13500,13700)
                    missiley[i] = random.randint(0,740)
    if (gameover_state == 'ready1'):
        screen.fill((0,0,0))
        coins(10,10)
        show_coins(30,7)
        diamonds(10,40)
        show_diamonds(30,37)
        game_over()
        highscore(650,300)
        show_score(650,270)
        if(quit_button.draw()==True):
            gameover_state = 'ready'
            life_value = 3
            phealth_bar.hp=100
            danger = 0
            energy_value = 150
            bossx =1200
            boolife_value = 250
            powermeter = 0
            bossmeter = 0
            if (score_value > score_value1):
                score_value1 = score_value
                with open('score.txt','w') as file:
                    file.write(str(score_value1))
            score_value = 0
            for i in range(num_of_enemies):
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
                enemy2x = random.randint(1820,1830)
                enemy2y = random.randint(320,580)
            for i in range(num_of_missiles):
                missilex[i] = random.randint(13500,13700)
                missiley[i] = random.randint(0,740)
    if (gameover_state == 'ready'):
        screen.fill((0,0,0))
        screen.blit(background2,(0,0))
        coins(10,10)
        show_coins(30,7)
        diamonds(10,40)
        show_diamonds(30,37)
        key = pygame.key.get_pressed()
        welcome()
        if (start_button.draw()== True):
            gameover_state ='selection'
            with open('score1.txt','w') as file:
                    file.write(str(coins_value))
            with open('score2.txt','w') as file:
                    file.write(str(diamonds_value))
            gameover_state ='selection'
        if (character_button.draw()==True):
            gameover_state = 'change'
        if(quit_button.draw()==True):
            life_value = 3
            phealth_bar.hp=100
            guardian_state = 'notin'
            purchased2_state = 'notpurchased'
            with open('score3.txt','w') as file:
                    file.write(ship_state)
            with open('score1.txt','w') as file:
                    file.write(str(coins_value))
            with open('score2.txt','w') as file:
                    file.write(str(diamonds_value))
            with open('score5.txt','w') as file:
                    file.write(special_state)
            with open('score6.txt','w') as file:
                    file.write(lvl1_state)
            run = False
    if(gameover_state == 'notready'):
        #n = network()
        #startPos = n.getPos()
        #screen.fill((50,50,50))
        screen.blit(background,(0,0))
        if (ship_state == 'ship1'):
            player2(player2x,player2y)
        if (ship_state == 'ship2'):
            player(player2x,player2y)
        if (ship_state == 'ship3'):
            player3(player2x,player2y)
        key = pygame.key.get_pressed()
        #pause
        if (pause_button.draw()==True):
            gameover_state ='pause'
        #restart
        if (reload_button.draw()== True):
            life_value = 3
            phealth_bar.hp=100
            danger = 0
            energy_value = 150
            bossx =1200
            boolife_value = 250
            powermeter = 0
            bossmeter = 0
            with open('score1.txt','w') as file:
                    file.write(str(coins_value))
            with open('score2.txt','w') as file:
                    file.write(str(diamonds_value))
            if (score_value > score_value1):
                score_value1 = score_value
                with open('score.txt','w') as file:
                    file.write(str(score_value1))
            score_value = 0
            for i in range(num_of_enemies):
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
                enemy2x = random.randint(1820,1830)
                enemy2y = random.randint(320,580)
            for i in range(num_of_missiles):
                missilex[i] = random.randint(13500,13700)
                missiley[i] = random.randint(0,740)
        #player movement
        if (key[pygame.K_LEFT]== True):
           player2x_change = -15
           player2y_change = 0
           if (key[pygame.K_f]==True):
              if (special_state == 'dash'):
                  if (dash<2):
                      if(energy_value >= 20):
                        dash +=1
                        player2x = player2x -100
                        energy_value -=2
        elif (key[pygame.K_RIGHT]== True):
            player2x_change = +15
            player2y_change = 0
            if (key[pygame.K_f]==True):
                if (special_state == 'dash'):
                   if (dash<2):
                      if(energy_value >= 20):
                          dash +=1
                          player2x = player2x +100
                          energy_value -=2
        elif (key[pygame.K_UP]== True):
            player2y_change = -15
            player2x_change = 0
            if (key[pygame.K_f]==True):
                if (special_state == 'dash'):
                   if (dash<2):
                       if(energy_value >= 20):
                          dash +=1
                          player2y = player2y -100
                          energy_value -=2
        elif (key[pygame.K_DOWN]== True):
            player2y_change = +15
            player2x_change = 0
            if (key[pygame.K_f]==True):
                if (special_state == 'dash'):
                   if (dash<2):
                       if(energy_value >= 20):
                          dash +=1
                          player2y = player2y +100
                          energy_value -=2
        elif (key[pygame.K_a]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_d]== True):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_w]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_s]== False):
            player2x_change = 0
            player2y_change = 0
        if (key[pygame.K_f]==False):
               dash = 0 
        #wasd
        if (key[pygame.K_a]== True):
            player2x_change = -15
        elif (key[pygame.K_d]== True):
            player2x_change = +15
        elif (key[pygame.K_w]== True):
            player2y_change = -15
        elif (key[pygame.K_s]== True):
            player2y_change = +15
        elif (key[pygame.K_a]== False):
            player2_change = 0
        elif (key[pygame.K_d]== True):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_w]== False):
            player2x_change = 0
            player2y_change = 0
        elif (key[pygame.K_s]== False):
            player2x_change = 0
            player2y_change = 0
           
        collis = energycollision(player2x,player2y,earthx,earthy)
        earth(earthx,earthy)
        if (collis):
            energy_value +=2
            phealth_bar.hp+=0.025
        if(energy_value >=150):
            energy_value = 150
        if(phealth_bar.hp>=100):
            phealth_bar.hp=100
        #nuke method
        nukey += nukey_change
        nuke(nukex, nukey)
        if (special_state== 'nuke'):
            if (key[pygame.K_p]):
                nukex= player2x
                nukey= player2y
                nukey_change=10
                nuke(nukex, nukey)
                
                nukeammo -=1
        if(special_state=='blaser'):
            if(energy_value>=1):
                if(key[pygame.K_p]):
                    blaserx=player2x
                    blasery=player2y
                    blaser(blaserx,blasery)
                    energy_value-=1
        if(special_state =='portal'):
            if(portal_button.draw()==True):
                       portaluse-=1
                       if (portaluse >=1):
                           player2x = earthx
                           player2y = earthy
                                
        if (portaluse <=10):
            portaluse +=0.05
                                        
        for i in range(num_of_enemies):
            nuklision = nukecollision(nukex,nukey,enemyx[i], enemyy[i])
            explolision = explodecolision(nukex,nukey,enemyx[i], enemyy[i])
            if(nuklision):
                nuke(2000,2000)
                if(explolision):
                        explosionx=enemyx[i]
                        explosiony=enemyy[i] 
                        explosion(explosionx,explosiony)
                        enemyx[i] = random.randint(1500,1510)
                        enemyy[i] = random.randint(0,1000)
        for i in range(num_of_enemies):
            if(enemyx[i]<=1400):
                blowmee=blowme(blaserx,enemyx[i])
                if(blowmee):
                    score_value+=1
                    enemyx[i] = random.randint(1500,1510)
                    enemyy[i] = random.randint(0,1000)
        #cow shotting method
        if(energy_value >= 2):
           if (key[pygame.K_SPACE]== True):
               if (cow_state == 'ready'):
                   cow_sound = mixer.Sound("pew.mp3")
                   cow_sound.play()
                   cowx = player2x
                   cowy = player2y
                   fire_cow(cowx,cowy)
                   energy_value -=2
               if (powerme>=1):
                   if (cow2_state == 'ready'):
                       cow2_sound = mixer.Sound("pew.mp3")
                       cow2_sound.play()
                       cow2x = player2x
                       cow2y = player2y
                       fire_cow2(cow2x,cow2y)
                       energy_value -=2
        player2x += player2x_change
        #powerup
        powercollision = powerup1(powerupx,powerupy,player2x,player2y)
        if (powermeter>=50):
            powerup(powerupx,powerupy)
            powerupx += powerupx_change
            powerupy += powerupy_change
            if (powerupy >= 640):
                powerupy_change = - 2
                powerupx_change = - 2
            if (powerupy <= 0):
                powerupy_change = 2
                powerupx_change = -2
            if (powerupx <=0):
                powerupx = 40000
            if (powercollision):
                powerupx = 40000
                powerme = 2
        #player boundries
        if ( player2x <= 0 ):
            player2x = 0
        elif ( player2x >= 1440):
            player2x = 1440
        elif ( player2y >= 690):
            player2y = 690
        elif (player2y <= 0):
            player2y = 0
        #death image and conditions  
        for i in range(num_of_enemies):
            spacedeath = space_death(enemyx[i], enemyy[i], player2x,player2y)
            spacedeath2 = space_death2(enemy2x, enemy2y, player2x,player2y)
            if (spacedeath or enemyx[i]<= 0 or spacedeath2 or enemy2x <= 0):
                life_value -= 1
                phealth_bar.hp-=25
                player2x = 100
                player2y = 390
                powermeter = 0
                powerme = 0
                enemyx[i] = random.randint(1300,1400)
                enemyy[i] = random.randint(0,1000)
                enemy2x = 2500
                enemy2y = 500
                if (guardian_state=='notin'):
                    if (phealth_bar.hp <= 0):
                       life_value = 0
                       gameover_state = 'ready1'
                if(guardian_state =='in'):
                    if (life_value<=0):
                        life_value = 3
                        guardian_state = 'notin'
                        purchased2_state = 'notpurchased'
            #enemy movement
            enemyy[i] += enemyy_change[i]
            if ( enemyy[i] >= 920):
                enemyy_change[i] = -7
                enemyx[i] -= enemyx_change[i]
            elif (enemyy[i] <= 0):
                enemyy_change[i] = 7
                enemyx[i] -= enemyx_change[i]
            if (enemyx[i] <=0):
                enemyx[i]= 1500
            if (score_value >= 20):
                if ( enemyy[i] >= 920):
                   enemyy_change[i] = -7.9
                   enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                    enemyy_change[i] = 7.9
                    enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                        enemyx[i]= 1500
            if (score_value >= 90):
                if ( enemyy[i] >= 920):
                        enemyy_change[i] = -9.7
                        enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                     enemyy_change[i] = 9.7
                     enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                     enemyx[i]= 1500
            if (score_value >= 120):
                if ( enemyy[i] >= 920):
                   enemyy_change[i] = -10.3
                   enemyx[i] -= enemyx_change[i]
                elif (enemyy[i] <= 0):
                   enemyy_change[i] = 10.3
                   enemyx[i] -= enemyx_change[i]
                elif (enemyx[i] <=0):
                    enemyx[i]= 1500
            enemy(enemyx[i],enemyy[i],i)
            #enemy2 movement
            if (score_value >= 50):
               enemy2y += enemy2y_change
               if (enemy2y >= 580):
                  enemy2y_change = -3
                  enemy2x -= enemy2x_change 
               elif (enemy2y <= 250):
                  enemy2y_change = 3
                  enemy2x -= enemy2x_change
               elif (enemy2x <=0):
                  enemy2x= 2500
               enemy2(enemy2x,enemy2y)
            if (score_value >= 80):
               enemy2y += enemy2y_change
               if (enemy2y >= 580):
                  enemy2y_change = -4
                  enemy2x -= enemy2x_change 
               elif (enemy2y <= 250):
                  enemy2y_change = 4
                  enemy2x -= enemy2x_change
               elif (enemy2x <=0):
                  enemy2x= 2500
               enemy2(enemy2x,enemy2y)
            if (score_value >= 140):
               enemy2y += enemy2y_change
               if (enemy2y >= 580):
                  enemy2y_change = -4.5
                  enemy2x -= enemy2x_change 
               elif (enemy2y <= 250):
                  enemy2y_change = 4.5
                  enemy2x -= enemy2x_change
               elif (enemy2x <=0):
                  enemy2x= 2500
               enemy2(enemy2x,enemy2y)
            #cow to enemy1 collision
            collision = isCollision(enemyx[i], enemyy[i],cowx,cowy)
            if (collision):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cowy = 400
                cow_state = 'ready'
                score_value +=1
                powermeter +=1
                bossmeter +=1
                coins_value+=10
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
            collision3 = isCollision3(enemyx[i], enemyy[i],cow2x,cow2y)
            if (collision3):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cow2y = 400
                cow2_state = 'ready'
                score_value +=1
                powermeter += 1
                bossmeter +=1
                coins_value+=10
                enemyx[i] = random.randint(1500,1510)
                enemyy[i] = random.randint(0,1000)
            #cow to enemy2 collision
            collision2 = iscollision2(enemy2x,enemy2y,cowx,cowy)
            if (collision2):
                explosion_Sound = mixer.Sound("deathsound.mp3")
                explosion_Sound.play()
                cowy = 400
                cow_state = 'ready'
                score_value +=5
                powermeter += 5
                bossmeter +=1
                coins_value+=10
                enemy2x = 2500
                enemy2y = 500
        #missiles
        if (score_value >= 75):
            for i in range(num_of_missiles):
                missilex[i] += missilex_change[i]
                if (missilex[i]<=0):
                    missilex[i] = random.randint(13500,13700)
                    missiley[i] = random.randint(0,740)
                    warnme = 0
                missile(missilex[i],missiley[i],i)
                missiledeath = missilecollision(missilex[i],missiley[i],player2x,player2y)
                if (missiledeath):
                    life_value -=1
                    missilex[i] = random.randint(13500,13700)
                    player2x = 100
                    player2y = 390
                    powermeter = 0
                    powerme = 0
                if (life_value <= 0):
                   life_value = 0 
                   for j in range(num_of_enemies):
                       enemyx[j] = -1
                       enemy2y = -1
                       game_over()
                   for j in range(num_of_missiles):
                       missiley[j]= -2000
                if(missilex[i]<= 7000):
                    warning1(warning1x,warning1y)
                    warning1y = missiley[i]
                if(missilex[i]<=1500):
                    warning1(10000,20000)
        #lasers
        if (score_value >= 75):
            for i in range(num_of_lasers):
                laser(laserx[i],lasery[i],i)
                laserx[i] += laserx_change[i]
                if (laserx[i]<=-1000):
                    laserx_change[i]= 2
                if (laserx[i]>=3500):
                    laserx_change[i]= -2
                    lasery_change[i]= random.randint(100,500)
                laserdeath = lasercollision(laserx[i],lasery[i],player2x,player2y)
                if (laserdeath):
                    player2x = 100
                    player2y = 350
                    life_value -=1
            for i in range(num_of_glasers):
                glaser(laserx[i]-54,lasery[i]-57,i)
                glaserx[i] += laserx_change[i]
                if (glaserx[i]<=-1000):
                    glaserx_change[i]= 2
                if (glaserx[i]>=3500):
                    glaserx_change[i]= -2
                    glasery_change[i]= random.randint(100,500)
        bossy += bossy_change
        thehocollision = theholecollision(holex,holey,player2x,player2y)
        collision4 = bosscollision(bossx,bossy,cowx,cowy)
        collision6 = bosscollision2(bossx,bossy,cow2x,cow2y)
        if (bossmeter>=200):
            for i in range(num_of_enemies):
                   enemyy[i] = 2000
                   enemy2y = 2000
                   enemyx[i]= 2000
                   enemy2x = 2000
            for i in range(num_of_missiles):
                missiley[i] = -1000
            if(danger<140):
                 danger_sound = mixer.Sound("danger.mp3")
                 danger_sound.play()
                 danger1(670,400)
                 danger2(670,200)
                 danger+=1
            elif(danger>=140):
                for i in range(num_of_asteroids):
                     astecollision = astercollision(asteroidx[i],asteroidy[i],player2x,player2y)
                collision5 = heartcollision(heartx,hearty,player2x,player2y)
                if(collision4):
                   boohealth_bar.hp-=10
                   cowy = player2y
                   cowx = player2x
                   cow_state = 'ready'
                if (collision6):
                   boohealth_bar.hp -=10
                   cow2y = player2y
                   cow2x = player2x
                   cow2_state = 'ready'
                   for i in range(num_of_asteroids):
                       asteroidy[i]=2000
                if (collision5):
                   phealth_bar.hp+=5
                   heartx = 12200
                if(phealth_bar.hp<=0):
                   phealth_bar.hp = 0
                   gameover_state = 'ready1'
                boss(bossx,bossy)
                boohealth_bar.draw(screen)
                asteroid(asteroidx[i],asteroidy[i],i)
                asteroidx[i] += asteroidx_change[i]
                thehole(holex,holey)
                holex += holex_change
                if (bossy <= 0):
                    bossy = random.randint(100,300)
                    bossy_change = 5
                    asteroidx_change[i] = -10
                    if (boohealth_bar.hp<=150):
                        bossy_change = 10
                        asteroidx_change[i]= -20
                    elif(boohealth_bar.hp<=50):
                         bossy_change = 15
                         asteroidx_change[i]= -40
                for i in range(num_of_asteroids):
                     if (asteroidx[i]<= 0):
                         asteroidx[i]=random.randint(1200,1210)
                         asteroidy[i]= player2y
                         asmeter +=1
                if(boohealth_bar.hp<=500):
                   if(frenzie2<100):
                      frenzie(700,700)
                      frenzie2 +=1
                if (bossy >= 700):
                    bossy = random.randint(300,600)
                    bossy_change = -5
                    if (boohealth_bar.hp<500):
                        bossy_change = -10
                    elif(boohealth_bar.hp<=250):
                        bossy_change = 15
                for i in range(num_of_asteroids):
                     if (asteroidx[i]<= 0):
                         asteroidx[i] =1200
                         asteroidy[i]= bossy
                         asmeter +=1
                         if (boolife_value<= 150):
                             asteroidx_change = -20
                         elif(boolife_value<=50):
                             asteroidx_change = -40
                if (astecollision):
                    phealth_bar.hp -=15
                    player2x = 100
                    powermeter = 0
                    player2y = 390
                    for i in range(num_of_asteroids):
                        if (asteroidx[i]<= 0 or astecollision):
                           asteroidx[i] =random.randint(1200,1210)
                           asteroidy[i]= random.randint(100,600)
                           asmeter +=1
                           powermeter = 0
                           powerme = 0
                if (asmeter >=4):
                   holex_change = -2
                   if(holex<=0):
                      holey= bossy
                      holex= 1200
                      asmeter = 0
                if(thehocollision):
                   phealth_bar.hp -=50
                   powermeter = 0
                   player2x = random.randint(0,900)
                   player2y = random.randint(0,700)
                heartx +=heartx_change
                hearty +=hearty_change
                if (boohealth_bar.hp <= 500):
                    heart(heartx,hearty)
                if (hearty<=200):
                    hearty_change =+3
                if (hearty>=500):
                    hearty_change = -3
                if (heartx<=0):
                    heartx = 12200
                if (special_state == 'blaser'):
                    blowme1 = blowme2(blaserx,bossx)
                    if(boohealth_bar.hp>=500):
                        if (blowme):
                            boohealth_bar.hp -=0.1
        if(boohealth_bar.hp<=0):
            coins_value+=100
            bossmeter = -1000
            bossx = 2000
            hearty = 1400
            holey= 11000
            for i in range(num_of_asteroids):
                asteroidy[i] = 12000
        if(score_value>=5):
            granny(grannyx,grannyy)
            grannyx+=grannyx_change
            grannyy+=grannyy_change
            if (grannyy<=0):
                grannyx_change-=0.1
                grannyy_change+=1
            if (grannyy>=1860):
                grannyy_change-=1
                grannyx_change-=0.1
            if (grannyx<=0):
                grannyx=2000
            if (grannyx>=2010):
                grannyx=2000
        #cow state 
        show_score(textx,texty)
        
        phealth_bar.draw(screen)
        highscore(1200,10)
        energy(10,50)
        if (cowy <= 0 or cowx >=1860):
            cowy = 400
            cowx = 700
            cow_state = 'ready'
        if (cow_state =='fire'):
            fire_cow(cowx,cowy)
            cowx += cowx_change
        if (cow2y <= 0 or cow2x >=1860):
            cow2y = 400
            cow2x = 700
            cow2_state = 'ready'
        if (cow2_state == 'fire'):
            fire_cow2(cow2x,cow2y)
            cow2x += cow2x_change
        player2y += player2y_change
        #quit
    for event in pygame.event.get():
        if event. type == pygame.QUIT:    
            run = False
    pygame.display.update()
pygame.quit()  

