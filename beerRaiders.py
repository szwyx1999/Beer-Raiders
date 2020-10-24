import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((950, 750))

# Background
background = pygame.image.load('barOutdoor.png')

# Title and Icon
pygame.display.set_caption("Beer Raiders")
icon = pygame.image.load('alcohol.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('LshootUp(1).png')
playerX_change = 0
playerX = 475
playerY = 600
speed = 3
playerImg1 = pygame.image.load('LshootUp(2).png')

def player(x, y):
    screen.blit(playerImg, (x, y))
    screen.blit(playerImg1, (x, y))

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
                playerX_change -= speed
            if event.key == pygame.K_RIGHT:
                playerX_change = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()