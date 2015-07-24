#!/usr/bin/env python
import time
import pygame
from pygame.locals import *
from classes import *

class Window:
	def __init__(self, size, caption):
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption(caption)
		self.time = time.time()
		
	def run(self):
		running = True
		offset = self.screen.get_size()
		offset = (offset[0]/2,offset[1]/2)
		run = 0
		next = run + 1
		floor = 0
		env = 0
		print 'floor:', len(texture_loader.floor_texture)
		print 'env:', len(texture_loader.environment_texture)
		while running:
			delta = time.time() - self.time
			self.time = time.time()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousePos = pygame.mouse.get_pos()
			if not running: break
			self.screen.fill((255,255,255))
			run += delta
			if run > next:
				floor += 1
				floor = floor % len(texture_loader.floor_texture)
				env += 1
				env = env % len(texture_loader.environment_texture)
				next = run+1
				
			self.screen.blit(texture_loader.getFloor(floor), (32*floor, 0))
			self.screen.blit(texture_loader.getEnvironment(env), (32*env, 32))
			
			pygame.display.flip()
			time.sleep(0.033)

win = Window((800,500),'Pygame Window')
win.run()