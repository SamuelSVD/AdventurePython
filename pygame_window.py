import pygame
from pygame.locals import *
import time

class Path:
	def __init__(self, direction, course, x, y):
		self.direction = direction
		self.course = course
		self.x = x
		self.y = y
		self.finished = False
def pathfind(grid,taken_grid, paths, destination, count):
	DIRS = ((0,-1),(1,0),(0,1),(-1,0))
	OPP = (2,3,0,1)
	new_paths = []
	finished = True
	for path in paths:
		if path.finished == True:
			new_paths.append(path)
			continue
		dirs = []
		for i in range(4):
			try:
				x = path.x + DIRS[i][0]
				y = path.y + DIRS[i][1]
				if x < 0 or y < 0:
					continue
				if not grid[x][y]  and not taken_grid[x][y] and not path.direction == OPP[i]:
					dirs.append(i)
			except:
				pass
		if len(dirs) == 0:
			path.finished = True
			new_paths.append(path)
		for dir in dirs:
			finished = False
			if (path.x + DIRS[dir][0],path.y + DIRS[dir][1]) == destination:
				way = path.course
				way.append(dir)
				path.course = way
				path.finished = True
				new_paths.append(path)
			else:
				taken_grid[path.x + DIRS[dir][0]][path.y + DIRS[dir][1]] = 1
				new_paths.append(Path(dir, path.course + [dir], path.x + DIRS[dir][0], path.y + DIRS[dir][1]))
	if finished:
		return grid, taken_grid, new_paths
	return grid, taken_grid, new_paths
class Window:
	def __init__(self, size, caption):
		self.screen = pygame.display.set_mode(size)
		pygame.display.set_caption(caption)


		self.grid = [[1,1,1,1,0,0,0,0,0,0],[0,1,0,0,0,1,1,1,1,0],[0,1,0,1,1,1,0,0,1,0],[0,1,0,0,0,0,1,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,0,0,0,1,0],[0,0,0,1,0,1,1,0,1,1],[0,1,1,1,0,1,0,0,0,1],[0,0,0,0,0,0,0,1,0,1],[1,1,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0],[1,1,0,1,1,0,1,1,1,0]]
		self.t_grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]


		self.paths = [Path(None,[],1,0)]
		self.selected_path = None;
		self.count = 0
		self.delay = 1
	def run(self):
		running = True
		previous_time = time.time()
		while running:
			delta = time.time() - previous_time
			previous_time = time.time()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					mousePos = pygame.mouse.get_pos()
					if mousePos[0] > 32 and mousePos[0] <= 160 and mousePos[1] > 256 and mousePos[1] <= 308: 
						print mousePos
			if not running: break
			self.count += delta
			
			if self.count > self.delay:
				self.count = 0
				self.grid, self.t_grid, self.paths = pathfind(self.grid, self.t_grid, self.paths, (10, 7), 0)


			self.screen.fill((0,0,0))
			for i in range(len(self.grid)):
				for j in range(len(self.grid[i])):
					if self.grid[i][j]:
						pygame.draw.rect(self.screen, (255,255,255), (100 + i * 10, 100 + j * 10, 10, 10))
			for path in self.paths:
				x = 1
				y = 0
				for i in range(len(path.course)):
					if path.course[i] == 0:
						y -= 1
					elif path.course[i] == 1:
						x += 1
					elif path.course[i] == 2:
						y += 1
					elif path.course[i] == 3:
						x -= 1
					pygame.draw.rect(self.screen,(0,0,255), (100 + x*10, 100 + y*10, 10,10))
			pygame.draw.rect(self.screen,(255,0,0,0.5), (100 + 100, 100 + 70, 10 ,10),1)
			pygame.display.flip()
		
win = Window((500,500),'Pygame Window')
win.run()