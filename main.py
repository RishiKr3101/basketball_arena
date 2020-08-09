import pygame
import random
import math

pygame.init()
s=2
#WINDOW
screen= pygame.display.set_mode((800,600))
background= pygame.transform.scale(pygame.image.load('bg1.png'), (800, 600))
pygame.display.set_caption("Basketball arena by RISHI")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#PLAYER
BallImg = pygame.transform.scale(pygame.image.load('ball.png'), (64, 64))
BallX = 370
BallY = 480
BallX_change = 0
BallY_change = 0

#ENEMIES
no_of_enemy= 5
enemy=[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
for i in range(no_of_enemy):
    enemy.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 400))
    enemyX_change.append(2)
    enemyY_change.append(0)

#SCORE
score_value=0
font = pygame.font.Font('freesansbold.ttf', 32)

#LEVEL
level_value=1
font = pygame.font.Font('freesansbold.ttf', 32)
#GAME_OVER
over_font = pygame.font.Font('freesansbold.ttf', 64)

#LIVE
live=5
font = pygame.font.Font('freesansbold.ttf', 32)

#BASKET
bask= pygame.transform.scale(pygame.image.load('hoop.png'), (64,64))
basket_x=random.randint(0, 736)
basket_y=random.randint(0, 400)



def ball(x,y):
    screen.blit(BallImg, (x,y))

def enemy_opp(x,y,i):
    screen.blit(enemy[i], (x,y))

def basket(x,y):
    screen.blit(bask, (x,y))

def isCollisionenemy(enemyX, enemyY, BallX, BallY):
    distance = math.sqrt(math.pow(enemyX - BallX, 2) + (math.pow(enemyY - BallY, 2)))
    if distance < 40:
        return True
    else:
        return False

def isCollisionbasket(basket_x, basket_y, BallX, BallY):
    distance = math.sqrt(math.pow(basket_x - BallX, 2) + (math.pow(basket_y - BallY, 2)))
    if distance < 34:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0,0,0))
    screen.blit(score, (x, y))

def show_level(x, y):
    lev = font.render("Level : " + str(level_value), True, (0,0,0))
    screen.blit(lev, (x, y))

def show_lives(x, y):
    liv = font.render("Live : " + str(live), True, (0,0,0))
    screen.blit(liv, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0,0,0))
    screen.blit(over_text, (200, 250))

runtime = True
while runtime:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            runtime = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                BallX_change = -5
            if event.key == pygame.K_RIGHT:
                BallX_change = 5
            if event.key == pygame.K_UP:
                BallY_change = -5
            if event.key == pygame.K_DOWN:
                BallY_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                BallX_change = 0
                BallY_change = 0
    if BallX <= 0:
        BallX = 0
    elif BallX >= 736:
        BallX = 736
    if BallY <= 0:
        BallY = 0
    elif BallY>= 536:
        BallY= 536
    BallX += BallX_change
    BallY += BallY_change
    for i in range(no_of_enemy):



        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = s

        elif enemyX[i] >= 736:
            enemyX_change[i] = -s

        enemyY[i] += enemyY_change[i]

        collision = isCollisionenemy(enemyX[i], enemyY[i], BallX, BallY)
        collisionbasket = isCollisionbasket(basket_x, basket_y, BallX, BallY)
        if collision:

            live -= 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 500)
    collisionbasket = isCollisionbasket(basket_x, basket_y, BallX, BallY)
    if collisionbasket:
        score_value +=1
        basket_x = random.randint(0, 736)
        basket_y = random.randint(0, 500)
        if score_value % 10 == 0 and score_value!=0:
            s +=1
            no_of_enemy +=1
            enemy.append(pygame.image.load('enemy.png'))
            enemyX.append(random.randint(0, 736))
            enemyY.append(random.randint(0, 400))
            enemyX_change.append(s)
            enemyY_change.append(0)
            live +=1
            level_value +=1

    ball(BallX, BallY)
    for i in range(no_of_enemy):
        enemy_opp(enemyX[i],enemyY[i], i)

    if live <= 0:
        for j in range(no_of_enemy):
            enemyX_change[j] = 0
        game_over_text()


    basket(basket_x, basket_y)
    show_lives(680, 10)
    show_score(10, 10)
    show_level(360,10)
    pygame.display.update()