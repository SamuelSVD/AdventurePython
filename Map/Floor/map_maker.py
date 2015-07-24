#!/usr/bin/env python
import struct
import pygame

GRASS = (0, 255, 0, 255)
DIRT = (156, 93, 82, 255)
SAND = (255, 255, 128, 255)
WATER = (0, 0, 255, 255)
COBBLE = (100,100,100,255)
WOOD_PLANKS = (153,76,0,255)
RED_BRICK = (200,150,150,255)
colors = []
colors.append(GRASS)
colors.append(DIRT)
colors.append(SAND)
colors.append(WATER)
colors.append(COBBLE)
colors.append(WOOD_PLANKS)
colors.append(RED_BRICK)
def makeImage():
	size = (400,400)
	image = pygame.Surface(size)
	byte_array = open('floor.SAM', 'rb').read()
	for i in range(len(byte_array)):
		index = byte_array[i]
		index = struct.unpack('B', index)[0]
		image.fill(colors[index], (i%400, i/400, 1, 1))
	for i in range(len(colors)):
		image.fill(colors[i], (i % 10, i / 10, 1, 1))
	pygame.image.save(image, 'floor.png')

def makeFromImage():
	image = pygame.image.load('floor.png')
	size = image.get_size()
	outfile = open('floor.SAM', 'wb')
	for j in range(size[1]):
		for i in range(size[0]):
			color = image.get_at((i,j))
			outfile.write(struct.pack('B',colors.index(color)))
	outfile.close()
	
def makeFiles():
	file = open('floor.SAM', 'rb')
	temp = file.read()
	file.close()
	size = int(len(temp) ** 0.5)
	floor_grid = []
	for i in range(size):
		floor_grid.append(temp[i*size:(i+1)*size])
	print len(floor_grid), len(floor_grid[0])

	CHUNK_SIZE = 20
	chunk_grid = []
	for i in range(size / CHUNK_SIZE):
		t = []
		for j in range(size / CHUNK_SIZE):
			t.append('')
		chunk_grid.append(t)

	for j in range(size / CHUNK_SIZE):
		for i in range(size / CHUNK_SIZE):
			temp = []
			for y in range(CHUNK_SIZE):
				temp.append(floor_grid[j*CHUNK_SIZE + y][i*CHUNK_SIZE:(i+1)*CHUNK_SIZE])
			chunk_grid[i][j] = temp
	#

	for i in range(len(chunk_grid)):
		for j in range(len(chunk_grid[i])):
			file = open('Floor/%d_%d.SAM' % (i-len(chunk_grid)/2, j-len(chunk_grid[i])/2), 'wb')
			for line in chunk_grid[i][j]:
				file.write(line)
			file.close()
#makeImage
makeFromImage()
makeFiles()