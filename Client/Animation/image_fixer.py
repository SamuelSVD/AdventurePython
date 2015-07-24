import pygame

def fix(url):
	image = pygame.image.load(url)
	size = image.get_size()
	fixed_image = pygame.Surface((size[0]*2, size[1]*2))
	fixed_image.fill((255,255,0))
	for i in range(size[0]/32):
		for j in range(size[1]/32):
			fixed_image.blit(image,(64*i+16,64*j+16),(32*i,32*j,32,32))
	pygame.image.save(fixed_image,'64x64/fixed_%s'%url)

fix('chr.png')