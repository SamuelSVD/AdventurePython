import pygame
class Animation:
	def __init__(self, images, delay, order):
		self.count = 0
		self.images = images
		self.delay = delay
		self.order = order
		self.current_time = 0
		self.next_time = delay
	def update(self,delta):
		self.current_time += delta
		if self.current_time > self.next_time:
			self.next_time = self.delay
			self.current_time = 0
			self.count += 1
	def getImage(self):
		i = self.count % len(self.order)
		return self.images[self.order[i]]

def main():
	texture = pygame.image.load('64x64/sam.png')
	anims = []
	SIZE = 64
	for j in range(8):
		textures = []
		for i in range(3):
			s = pygame.Surface((SIZE,SIZE))
			s.blit(texture,(0,0),(SIZE*i,SIZE*j,SIZE,SIZE))
			textures.append(s)
		anim = Animation(textures,0.2,[0,1,2,1])
		anims.append(anim)
	for j in range(8):
		textures = []
		for i in range(2):
			s = pygame.Surface((SIZE,SIZE))
			s.blit(texture,(0,0),(SIZE*i,SIZE*(8+j),SIZE,SIZE))
			textures.append(s)
		anim = Animation(textures,0.5,[0,1])
		anims.append(anim)
	for j in range(8):
		textures = []
		for i in range(2):
			s = pygame.Surface((SIZE,SIZE))
			s.blit(texture,(0,0),(SIZE*i,SIZE*(16+j),SIZE,SIZE))
			textures.append(s)
		anim = Animation(textures,0.5,[0,1])
		anims.append(anim)
	screen = pygame.display.set_mode((SIZE * 8,SIZE * 3))
	clock = pygame.time.Clock()
	clock.tick(30)
	clock.tick(30)
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
		delta = clock.get_time()/1000.0
		for anim in anims:
			anim.update(delta)
			if anims.index(anim) < 8:
				screen.blit(anim.getImage(),(SIZE * anims.index(anim),0))
			elif anims.index(anim) < 16:
				screen.blit(anim.getImage(),(SIZE * (anims.index(anim)-8),SIZE))
			else:
				screen.blit(anim.getImage(),(SIZE * (anims.index(anim)-16),SIZE*2))
		pygame.display.flip()
		clock.tick(30)
main()
