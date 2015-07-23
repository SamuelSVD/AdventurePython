# This is the game. This is where it all happens. Let's do this.
import pygame
from pygame.locals import *
from FileIO import *
from classes import *

#Game states
MAIN_MENU = 0
GAME = 1

def main():
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Pygame Window')
    running = True
    # start all variables
    gamestate = MAIN_MENU
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



        #Main Menu
        if gamestate == MAIN_MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousePos = pygame.mouse.get_pos()
                        if mousePos[0] > 32 and mousePos[0] <= 160 and mousePos[1] > 256 and mousePos[1] <= 308: 
                            print mousePos

            if running == False: return()
            
        #

