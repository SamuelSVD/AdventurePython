#!/usr/bin/env python
import struct
import pygame
colors = []
colors.append((121,121,121,255))
colors.append((147,104,42))
colors.append((189,138,65))
def loadFromOldFileFormat():
	map = []
	for i in range(20):
		temp = []
		for j in range(20):
			temp.append('')
		map.append(temp)
	for i in range(20):
		for j in range(20):
			lines = open('Map/%d_%dE.SAM' % (i,j), 'r').read()
			lines = lines.split('\n')
			lines = lines[1:]
			chunk = []
			for line in lines:
				line = line.split()
				code = []
				for number in line:
					code.append(int(number)+1)
				chunk.append(code)
			map[i][j] = chunk
	outfile = open('environment.SAM', 'wb')
	for chunk_row in range(20):
		for block_row in range(20):
			for column in range(20):
				for char in map[column][chunk_row][block_row]:
					outfile.write(struct.pack('B', char))
	outfile.close

def makeImage():
	size = (400,400)
	image = pygame.Surface(size)
	byte_array = open('environment.SAM', 'rb').read()
	for i in range(len(byte_array)):
		index = byte_array[i]
		index = ord(index)
		if index in range(1,12):
			image.fill(colors[0], (i%400, i/400, 1, 1))
		if index in range(12,23):
			print i
			image.fill(colors[1], (i%400, i/400, 1, 1))
		if index in range(23,34):
			image.fill(colors[2], (i%400, i/400, 1, 1))
	for i in range(len(colors)):
		image.fill(colors[i], (i%5,i/5, 1, 1))
	pygame.image.save(image, 'environment.png')

def makeFromImage():
	image = pygame.image.load('environment.png')
	size = image.get_size()
	outfile = open('environment.SAM', 'wb')
	for j in range(size[1]):
		for i in range(size[0]):
			color = image.get_at((i,j))
			num = 0
			if color == colors[0]:
				num = 1
			elif color == colors[1]:
				num = 12
			elif color == colors[2]:
				num = 23
			if num:
				directions = [False, False, False, False]
				try:
					if color == image.get_at((i,j-1)):
						directions[0] = True
				except:
					pass
				try:
					if color == image.get_at((i+1,j)):
						directions[1] = True
				except:
					pass
				try:
					if color == image.get_at((i,j+1)):
						directions[2] = True
				except:
					pass
				try:
					if color == image.get_at((i-1,j)):
						directions[3] = True
				except:
					pass
				if directions[0]:
					if directions[1]:
						if directions[2]:
							if directions[3]:
								num += 10
							else:
								num += 7
						elif directions[3]:
							num += 6
						else:
							num += 4
					elif directions[2]:
						if directions[3]:
							num += 9
						else:
							num += 3
					elif directions[3]:
						num += 5
					else:
						num += 3
				elif directions[1]:
					if directions[2]:
						if directions[3]:
							num += 8
						else:
							num += 0
					elif directions[3]:
						num += 1
					else:
						num += 1
				elif directions[2]:
					if directions[3]:
						num += 2
					else:
						num += 3
				elif directions[3]:
					num += 1
			outfile.write(struct.pack('B',num))
	outfile.close()
	
def makeFiles():
	file = open('environment.SAM', 'rb')
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
			file = open('Env/%d_%dE.SAM' % (i-len(chunk_grid)/2, j-len(chunk_grid[i])/2), 'wb')
			for line in chunk_grid[i][j]:
				file.write(line)
			file.close()

#makeImage()
makeFromImage()
makeFiles()