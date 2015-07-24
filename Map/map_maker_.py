#!/usr/bin/env python
import pygame
from struct import *

GRASS = (0, 255, 0, 255)
DIRT = (156, 93, 82, 255)
SAND = (255, 255, 128, 255)
DEEP_WATER = (0, 0, 255, 255)
palette = [GRASS, DIRT, SAND, DEEP_WATER]
floor = pygame.image.load('floor.bmp')
floor_grid = []
size = floor.get_size()

for j in range(size[1]):
	row = []
	for i in range(size[0]):
		color = floor.get_at((i,j))
		row.append(palette.index(color))
	floor_grid.append(bytearray(row))
file = open('map.SAM', 'w')
for row in floor_grid:
#	for block in row:
#		file.write(pack('B',block))
	file.write(row)
file.close()

file = open('map.SAM', 'rb')
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

