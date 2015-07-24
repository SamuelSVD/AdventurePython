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
		self.chunks = {}
		self.character = Entity(None, Vector(0,0),  0,  0,  0, None)
		size = 1
		for i in range(size):
			for j in range(size):
				loc = '%d_%d'%(i-size/2,j-size/2)
				self.chunks[loc] = Chunk(loc, open('Map/Floor/%s.SAM' % loc, 'rb').read(), open('Map/Env/%sE.SAM' % loc, 'rb').read())
	def run(self):
		running = True
		offset = self.screen.get_size()
		offset = (offset[0]/2,offset[1]/2)
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
			keys = pygame.key.get_pressed()
			if keys[K_UP]:
				self.character.position.y -= 128*delta
			elif keys[K_DOWN]:
				self.character.position.y += 128*delta
			if keys[K_RIGHT]:
				self.character.position.x += 128*delta
			elif keys[K_LEFT]:
				self.character.position.x -= 128*delta
		
			self.screen.fill((0,0,0))
			for loc, chunk in self.chunks.iteritems():
				chunk.drawFloor(self.screen, self.character, offset)
				for i in range(20):
					chunk.drawRow(self.screen, self.character, offset, i)
			pygame.display.flip()
			time.sleep(0.033)

win = Window((800,500),'Pygame Window')
win.run()