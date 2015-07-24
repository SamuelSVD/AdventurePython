import time
import pygame
# [Start coords, size coords, order, scale, delay]
littleMan = [(0,0),(20,50),[0,1,2,1,0,4,3,4],(600,600),0.15]
runningMan = [(0,50),(40,70),[0,1,2,3,4,5,6,7,8],(400,400),0.1]

walk = [(0,0),(32,64),[0,1,2,1],(200,200),0.2]
walk2 = [(0,0),(32,32),[0,1,2,1],(600,600),0.2]
walk3 = [(0,0),(32,134),[0,1,2,1],(600,600),0.15]
projectile = [(0,0),(32,96),[0,2,1,2],(32,96),0.2]
def loadImage(url):
    return pygame.image.load(url)

def setAnimation(item):
    return item[0],item[1],item[2],item[3],item[4]

def main():
#    texture = loadImage('walk_6.bmp')
    texture = loadImage('projectiles.bmp')
    start, size, order, scale, delay = setAnimation(projectile)
    screen = pygame.display.set_mode((200,600))
    screen.fill((70,150,70))
    i = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        i += 1
        
        t = pygame.Surface(size)
        t.blit(texture,(0,0),(order[i%len(order)]*size[0]+start[0],start[1],size[0],size[1]))
        #t = pygame.transform.rotate(t, (time.time()%360)*10)
        screen.blit(pygame.transform.scale(t,scale),(0,0))
        
        #tempScreen.blit(texture,(0,0),(order[i%len(order)]*size[0]+start[0],start[1],size[0],size[1]))
        #screen.blit(pygame.transform.scale(tempScreen,scale),(0,0))
        pygame.display.flip()
        time.sleep(delay)

main()
