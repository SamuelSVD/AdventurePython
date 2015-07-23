from classes import *
import pygame
from pygame.locals import *
import time

temp = pygame.image.load('Images/Texture.png')
texture = [pygame.Surface((32,32)),pygame.Surface((32,32)),pygame.Surface((32,32)),pygame.Surface((32,32))]
for i in range(len(texture)):
    texture[i].blit(temp,(0,0), (i*32,0,(i+1)*32,32))

class Chunk:
    image = None
    def __init__(self, position,location,environment,size):
        self.position = position
        self.location = location
        self.environment = environment
        self.size = size
        self.generateImage()

    def generateImage():
        self.image = pygame.Surface((self.size*self.environment.getX(),self.size*self.environment.getY()))
        for i in range(self.environment.getX()):
            for j in range(self.environment.getY()):
                self.image.blit(texture[self.environment.getComponent(i,j).getType()],(self.size*i,self.size*j))

    def drawChunk(self, surface):
        surface.blit(self.image,(self.position.getX(),self.position.getY()))
    
def loadEnvironment(url):
    f = open(url,'r').read()
    print f
    f = f.split('\n')
    s = f[0].split()
    f = f[1:]
    for n in s:
        n = int(n)
    E = Environment(s[0],s[1])
    for l in f:
        l = l.split()
    for i in range(len(f)):
        for j in range(len(f[i])):
            # loading the environment component
            n = int(f[i][j])
            n = EnvironmentComponent(i,j,n)
            E.setComponent(i,j,n)
    return E


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Pygame Window')
running = True
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
    screen.blit(texture[0],(0,0))
    screen.blit(texture[1],(32,32))
    screen.blit(texture[2],(0,32))
    pygame.display.flip()
