import pygame
def reorganizePic(url,order):
	image = pygame.image.load(url)
	size = image.get_size()
	rows = []
	for i in range(size[1]/64):
		print i
		s = pygame.Surface((size[0],64),pygame.SRCALPHA)
		s.blit(image,(0,0),(0,64*i,size[0],64))
		rows.append(s)
	fixed_image = pygame.Surface(size,pygame.SRCALPHA)
	for i in range(len(order)):
		print i, order[i]
		fixed_image.blit(rows[order[i]],(0,64*i))
	pygame.image.save(fixed_image,'fixed_%s' % url)

#
order = [3,5,2,4,0,7,1,6,11,13,10,12,8,15,9,14,19,21,18,20,16,23,17,22]
reorganizePic('sam.png',order)