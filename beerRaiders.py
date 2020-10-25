import os
import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((950, 750))

# Background
background = pygame.image.load('brewery-background.png')

# Title and Icon
pygame.display.set_caption("Beer Raiders")
icon = pygame.image.load('alcohol.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("BRsprites/LshootUp(1).png")
playerX_change = 0
playerX = 475
playerY = 620
playerX_change = 0

# bullet
# ready - you can't see the bullet on teh screen
# fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 620
bulletX_change = 0
bulletY_change = 3.5
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))
    #screen.blit(playerImg1, (x, y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))



# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check if left or right arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

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

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
