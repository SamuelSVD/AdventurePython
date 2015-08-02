import time

class Path:
	def __init__(self, direction, course, x, y):
		self.direction = direction
		self.course = course
		self.x = x
		self.y = y
		self.finished = False
def pathfind(grid,taken_grid, paths, destination, count):
#	print count
	DIRS = ((0,-1),(1,0),(0,1),(-1,0))
	OPP = (2,3,0,1)
	new_paths = []
	finished = True
#	print 'Num paths:', len(paths)
#	print taken_grid
	for path in paths:
		if path.finished == True:
			new_paths.append(path)
			continue
#		print 'finished = False'
		dirs = []
		for i in range(4):
			try:
#				print 'checking %d:' % i,repr(grid[path.x + DIRS[i][0]][path.y + DIRS[i][1]]), repr(taken_grid[path.x + DIRS[i][0]][path.y + DIRS[i][1]])
				x = path.x + DIRS[i][0]
				y = path.y + DIRS[i][1]
				if x < 0 or y < 0:
					continue
				if not grid[x][y]  and not taken_grid[x][y] and not path.direction == OPP[i]:
					dirs.append(i)
#					print i,'worked'
			except:
#				print 'error'
				pass
		if len(dirs) == 0:
			path.finished = True
			new_paths.append(path)
#			print 'Dirs:', dirs
		for dir in dirs:
			finished = False
			if (path.x + DIRS[dir][0],path.y + DIRS[dir][1]) == destination:
				way = path.course
				way.append(dir)
#				print 'There were',len(paths),'paths at the end'
				return way
			else:
				taken_grid[path.x + DIRS[dir][0]][path.y + DIRS[dir][1]] = 1
				new_paths.append(Path(dir, path.course + [dir], path.x + DIRS[dir][0], path.y + DIRS[dir][1]))
	if finished:
#		for path in new_paths:
#			print new_paths.index(path),':',path.course
		return None
#	time.sleep(5)
	return pathfind(grid, taken_grid, new_paths, destination, count + 1)

def main():
	p1 = [[0,0,0,0,0],[1,1,1,0,1],[0,0,0,0,1],[1,0,1,1,0],[1,0,0,0,0],[1,1,1,0,1]]
	P1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	t = time.time()
	print pathfind(p1, P1, [Path(3,[],0,0)],(4, 4), 0)
	print 'there was a delay of %0.5f seconds' % (time.time() - t)
	p1 = [[0,0,0,0,0],[1,1,1,0,1],[0,0,0,0,1],[1,0,1,1,0],[1,0,0,0,0],[1,1,1,0,1]]
	P1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	t = time.time()
	print pathfind(p1, P1, [Path(3,[],4,4)],(0, 0), 0)
	print 'there was a delay of %0.5f seconds' % (time.time() - t)


	p2 = [[1,1,1,1,0,0,0,0,0,0],[0,1,0,0,0,1,1,1,1,0],[0,1,0,1,1,1,0,0,1,0],[0,1,0,0,0,0,1,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,0,0,0,1,0],[0,0,0,1,0,1,1,0,1,1],[0,1,1,1,0,1,0,0,0,1],[0,0,0,0,0,0,0,1,0,1],[1,1,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0],[1,1,0,1,1,0,1,1,1,0]]
	P2 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
	t = time.time()
	print pathfind(p2, P2, [Path(None,[],1,0)],(11, 9), 0)
	print 'there was a delay of %0.5f seconds' % (time.time() - t)

	p3 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
	P3 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
	t = time.time()
	print pathfind(p3, P3, [Path(None,[],0,0)],(11, 9), 0)
	print 'there was a delay of %0.5f seconds' % (time.time() - t)

if __name__ == '__main__':
	main()