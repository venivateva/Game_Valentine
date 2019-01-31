import pygame
import time
import sys
from pygame.locals import *



pygame.init()


DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('First Game')


# set used colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#my character
x=60
y=50
width=20
height=10
vel=5
isJump=False


# set background music
music = pygame.mixer.music.load('HONNE.mp3')
music = pygame.mixer.music.play()
time.sleep(1)

# mouse
pygame.mouse.set_visible(True)


while True: # main game loop

    Circleplace=pygame.draw.circle(DISPLAYSURF, RED, (24, 24), 7)
    pos = pygame.mouse.get_pos()
    pressed=pygame.mouse.get_pressed()


    if Circleplace.collidepoint(pos) and pressed:
        pygame.draw.ellipse(DISPLAYSURF, GREEN, (20,20,10,25),0)


    pygame.display.update()
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y-= vel

    if keys[pygame.K_DOWN]:
        y += vel


    DISPLAYSURF.fill((0,0,0))
    pygame.draw.rect(DISPLAYSURF,RED,(x,y,width,height))
    pygame.display.update()

