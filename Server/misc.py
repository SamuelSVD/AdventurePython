# ------------ Math ------------------------------------------------------------------------------------ #
class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		return "%0.2f %0.2f" % (self.x, self.y)
	def setMagnitude(self, mag):
		if mag == 0:
			self.x = 0
			self.y = 0
		else: ## This does not work when the values for x and y are both 0
			self.x, self.y = self.x/float((self.x**2+self.y**2)**0.5)*mag,self.y/float((self.x**2+self.y**2)**0.5)*mag
	def getMagnitude(self):
		return ((self.x)**2+(self.y)**2)**0.5
	def add(self, vector):
		self.x += vector.x
		self.y += vector.y
	def distance(self, vector):
		return ((self.x-vector.x)**2+(self.y-vector.y)**2)**0.5
	def negative(self):
		return Vector(-self.x, -self.y)
	def copy(self):
		return Vector(-(-self.x),-(-self.y))
	def sin(self):
		try:
			return self.y/self.getMagnitude()
		except:
			return None
	def cos(self):
		try:
			return self.x/self.getMagnitude()
		except:
			return None
	def tan(self):
		try:
			return self.y/self.x
		except:
			return None
	def delta(self, vector):
		return Vector(-self.x+vector.x, -self.y+vector.y)
	def scale(self, scalar_multiple):
		return Vector(self.x*scalar_multiple,self.y*scalar_multiple)

# ------------ Entities -------------------------------------------------------------------------------- #
class Entity:
	def __init__(self, id, position, direction, speed, moving, animations = None):
		self.id = id
		self.position = position
		self.direction = direction
		self.speed = speed
		self.moving = moving
		self.animations = animations
		
		self.shad_size = (20,14)
		self.velocity = Vector(0,0)
		self.fixAnim = False
		self.__fix__()
	def __dict__(self):
		return {'id':self.id, 'position':self.position, 'direction':self.direciton,'speed':self.direction}
	def __fix__(self):
		#print self.get()
		if self.moving:
			if self.direction == 7 or self.direction == 0 or self.direction == 1:
				self.velocity.y = -1
			elif self.direction == 3 or self.direction == 4 or self.direction == 5:
				self.velocity.y = 1
			else:
				self.velocity.y = 0
			if self.direction == 5 or self.direction == 6 or self.direction == 7:
				self.velocity.x = -1
			elif self.direction == 1 or self.direction == 2 or self.direction == 3:
				self.velocity.x = 1
			else:
				self.velocity.x = 0
			#print self.velocity
			self.velocity.setMagnitude(self.speed)
			#print self.velocity
			if self.animations and self.fixAnim:
				self.fixAnim = False
				#print 'resetting'
				self.animations[self.direction].reset()
		else:
			self.velocity.setMagnitude(0)
			if self.animations and self.fixAnim:
				self.fixAnim = False
				#print 'resetting'
				self.animations[self.direction+8].reset()
	def setDirection(self,direction):
		if direction != self.direction:
			self.direction = direction
			self.__fix__()
			self.fixAnim = True
			return True
	def setMoving(self, moving):
		if self.moving != moving:
			#print moving
			self.moving = moving
			self.__fix__()
			self.fixAnim = True
			return True
	def setSpeed(self, speed):
		self.speed = speed
		self.__fix__()
	def update(self, delta):
		self.position.add(self.velocity.scale(delta))
		#if not self.moving:
		#	print self.id, 'can\'t move\t', self.velocity
		#else:
		#	print self.id, 'can move\t', self.velocity
		if self.animations:
			if self.moving:
				self.animations[self.direction].update(delta)
			else:
				self.animations[self.direction + 8].update(delta)
	def get(self):
		#print self.id,self.position.x,self.position.y,self.direction,self.speed, self.moving
		return 'E%s %0.0f %0.0f %d %d %d' % (self.id,self.position.x,self.position.y,self.direction,self.speed, self.moving)
	def getImage(self):
		#print repr(self.moving), self.direction
		if self.moving:
			return self.animations[self.direction].getImage()
		else:
			return self.animations[self.direction + 8].getImage()
	def getShadow(self):
		s = pygame.Surface(self.shad_size,pygame.SRCALPHA)
		pygame.draw.ellipse(s, (10,10,20),(0,0,self.shad_size[0],self.shad_size[1]))
		return s
class Character(Entity):
	def __init__(self, id, position, direction, speed, moving, name, skin, hair, equipment, animations = None):
		Entity.__init__(self, id, position, direction, speed, moving, animations)
		self.name = name
		self.skin = skin
		self.hair = hair
		self.equipment = equipment
	def getChar(self):
		return 'C%s %0.0f %0.0f %d %d %d %s' % (self.id,self.position.x,self.position.y,self.direction,self.speed, self.moving, self.name)
class Mob(Entity):
	def __init__(self, id, position, direction, speed, moving, name, type, level, animations = None):
		Entity.__init__(self, id, position, direction, speed, moving, animations)
		self.name = name
		self.type = type
		self.level = level
class Item(Entity):
	def __init__(self, id, position, direction, speed, moving, item_number, animations = None):
		Entity.__init__(self, id, position, direction, speed, moving, animations)
		self.item_number = item_number
class Projectile(Entity):
	def __init__(self, id, position, direction, speed, moving, projectile_number, animations = None):
		Entity.__init__(self, id, position, direction, speed, moving, animations)
		self.projectile_number = projectile_number

		
class Chunk:
	def __init__(self, location,byte_array_a = None,byte_array_b = None):
		self.location = location
		self.byte_array_a = byte_array_a
		self.byte_array_b = byte_array_b
		self.floor = []
		self.environment = []
		self.floor_image = None
		self.rows = []
		self.loaded = False
		self.block_width = 32
		self.chunk_width = 0
		if self.byte_array_a:
			self.buildFloor()
		if self.byte_array_b:
			self.buildEnv()
		temp = self.location.split('_')
		temp = (int(temp[0]), int(temp[1]))
		self.x = temp[0] * 32 * self.chunk_width
		self.y = temp[1] * 32 * self.chunk_width
	def buildFloor(self):
		self.chunk_width = int(len(self.byte_array_a) ** 0.5)
		for i in range(self.chunk_width):
			self.floor.append(self.byte_array_a[i*self.chunk_width:(i+1)*self.chunk_width])
	def buildEnv(self):
		size = int(len(self.byte_array_b) ** 0.5)
		for i in range(size):
			self.environment.append(self.byte_array_b[i*size:(i+1)*size])
	def getFloor(self):
#		print len(self.byte_array_a)
		return 'mf%s %s' % (self.location, self.byte_array_a)
	def setFloor(self, byte_array):
		self.byte_array_a = byte_array
		self.buildFloor()
	def getEnvironment(self):
		return 'me%s %s' % (self.location, self.byte_array_b)
	def setEnvironment(self, byte_array):
		self.byte_array_b = byte_array
		self.buildEnv()

class Map:
	def __init__(self, size):
		self.size = size
		self.folder_location = 'Map'
		self.chunks = {}
		self.loadMap()
	def loadMap(self):
		for i in range(self.size):
			for j in range(self.size):
				file = open('%s/Floor/%d_%d.SAM' % (self.folder_location, i-self.size/2, j-self.size/2), 'rb')
				byte_array_a = file.read()
				file.close()
				file = open('%s/Env/%d_%dE.SAM' % (self.folder_location, i-self.size/2, j-self.size/2), 'rb')
				byte_array_b = file.read()
				file.close()
				self.chunks['%d_%d' % (i-self.size/2, j-self.size/2)] = Chunk('%d_%d' % (i-self.size/2, j-self.size/2), byte_array_a, byte_array_b)
