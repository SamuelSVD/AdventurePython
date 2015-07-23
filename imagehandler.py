import pygame
from pygame.locals import *
from classes import *
from FileIO import *

temp = pygame.image.load('Images/Texture.png')
texture = [pygame.Surface((32,32)),pygame.Surface((32,32)),pygame.Surface((32,32)),pygame.Surface((32,32))]
for i in range(len(texture)):
    texture[i].blit(temp,(0,0), (i*32,0,(i+1)*32,32))

##class Chunk:
##    image = None
##    def __init__(self, position,location,environment,size):
##        self.position = position
##        self.location = location
##        self.environment = environment
##        self.size = size
##        self.generateImage()
##
##    def generateImage(self):
##        self.image = pygame.Surface((self.size*self.environment.getX(),self.size*self.environment.getY()))
##        for j in range(self.environment.getY()):
##            for i in range(self.environment.getX()):
##                self.image.blit(texture[self.environment.getComponent(i,j).getType()],(self.size*i,self.size*j))
##
##    def drawChunk(self, surface):
##        surface.blit(self.image,(self.position.getX(),self.position.getY()))
##
##    def drawChunkI(self, surface):
##        for i in range(self.environment.x):
##            for j in range(self.environment.y):
##                surface.blit(texture[self.environment.getComponent(i,j).getType()],(self.size*i+self.position.getX(),self.size*j+self.position.getY()))
    

C = []
for i in range(20):
    for j in range(20):
        C.append(loadChunk(i,j,texture))

#C = [c,c2,c3,c4,c5,c6,c7]

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Pygame Window')
running = True
s = 4
while running:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if mousePos[0] > 32 and mousePos[0] <= 160 and mousePos[1] > 256 and mousePos[1] <= 308: 
                        print mousePos
                        
    if running == False: break

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        for c in C:
            c.position = Vector(c.position.x,c.position.y+s)
        
    if keys[K_DOWN]:
        for c in C:
            c.position = Vector(c.position.x,c.position.y-s)
    if keys[K_LEFT]:
        for c in C:
            c.position = Vector(c.position.x+s,c.position.y)
    if keys[K_RIGHT]:
        for c in C:
            c.position = Vector(c.position.x-s,c.position.y)
    
#    screen.blit(texture[0],(0,0))
#    screen.blit(texture[1],(32,32))
#    screen.blit(texture[2],(0,32))
    screen.fill((0,0,0))
    for c in C:
            c.drawChunk(screen)
    pygame.display.flip()
