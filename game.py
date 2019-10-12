import pygame
import time
import sys
import os
from pygame.locals import *



class MyPlayer(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images=[]
        for i in range (1,5):
            image = pygame.image.load(os.path.join('data','skeleton'+str(i)+'.png')).convert()
            image.convert_alpha()
            image.set_colorkey(BLUE)
            self.images.append(image)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def movement (self,x,y):

        self.movex += x
        self.movey += y

    def updatechar(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]


#frames settings

fps=40
ani=4
clock=pygame.time.Clock()
pygame.init()


mainscreen= pygame.display.set_mode((400, 300))
background = pygame.image.load(os.path.join('data','background.png')).convert()
backfropbox= mainscreen.get_rect()
pygame.display.set_caption('First Game')



# set used colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# #my character spawn




player = MyPlayer()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
vel=5


# set background music
#music = pygame.mixer.music.load('HONNE.mp3')
#music = pygame.mixer.music.play()
#time.sleep(1)

# mouse
pygame.mouse.set_visible(True)


while True: # main game loop

    Circleplace=pygame.draw.circle(mainscreen, RED, (24, 24), 7)
    pos = pygame.mouse.get_pos()
    pressed=pygame.mouse.get_pressed()


    if Circleplace.collidepoint(pos) and pressed:
        pygame.draw.ellipse(mainscreen, GREEN, (20,20,10,25),0)


    pygame.display.update()
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.movement(-vel,0)
            if event.key == pygame.K_RIGHT:
                player.movement(vel,0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.movement(vel, 0)
            if event.key == pygame.K_RIGHT:
                player.movement(-vel, 0)




    mainscreen.blit(background,backfropbox)
    player.updatechar()
    pygame.display.update()
    player_list.draw(mainscreen)
    pygame.display.flip()
    clock.tick(fps)
    #mainscreen.fill((0,0,0))
    #pygame.draw.rect(mainscreen,RED,(x,y,width,height))




