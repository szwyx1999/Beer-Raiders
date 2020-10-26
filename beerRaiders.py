import os
import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((950, 750))

#clock
clock = pygame.time.Clock()

# Background
background = pygame.image.load('brewery-background.png')

# Title and Icon
pygame.display.set_caption("Beer Raiders")
icon = pygame.image.load('alcohol.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("BRsprites/LshootUp(1).png") #standing sprite
playerX_change = 0
playerX = 475
playerY = 620
playerY_change = 0
left = False
right = False
movCount = 0

#animation to walk right
walkRight = [pygame.image.load('BRsprites/RshootUp(1).png'), pygame.image.load('BRsprites/RshootUp(2).png'), pygame.image.load('BRsprites/RshootUp(3).png'), pygame.image.load('BRsprites/RshootUp(4).png')]
#animation to walk left
walkLeft = [pygame.image.load('BRsprites/LshootUp(1).png'), pygame.image.load('BRsprites/LshootUp(2).png'), pygame.image.load('BRsprites/LshootUp(3).png'), pygame.image.load('BRsprites/LshootUp(4).png')]

def animation():
    global movCount

    if movCount + 1 >= 28:
        movCount = 0

    if left:
        screen.blit(walkLeft[movCount // 7], (playerX, playerY))
        movCount += 1

    if right:
        screen.blit(walkRight[movCount // 7], (playerX, playerY))
        movCount += 1

    if not (left or right):
        screen.blit(playerImg, (playerX, playerY))

    pygame.display.update()



# bullet
# ready - you can't see the bullet on teh screen
# fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 620
bulletX_change = 0
bulletY_change = 17
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))



def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))



# Game Loop
running = True
while running:

    clock.tick(40)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check if left or right arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
                left = True
                right = False
            elif event.key == pygame.K_RIGHT:
                playerX_change = 10
                right = True
                left = False
            else:
                right = False
                left = False
                movCount = 0

            if event.key == pygame.K_SPACE:
                right = False
                left = False
                movCount =0
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                right = False
                left = False
                movCount = 0



    # player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 886:
        playerX = 886


    # bullet movement
    if bulletY <= 0:
        bulletY = 620
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    animation()
    show_score(textX, textY)
    pygame.display.update()
