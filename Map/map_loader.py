
# Server
class Chunk:
	def __init__(self, location, byte_array_a,byte_array_b):
		self.location = location
		self.byte_array_a = byte_array_a
		self.byte_array_b = byte_array_b
		self.floor = []
		self.environment = []
		if self.byte_array_a:
			self.buildFloor()
		if self.byte_array_b:
			self.buildEnv()
	def buildFloor(self):
		size = int(len(self.byte_array_a) ** 0.5)
		for i in size:
			self.floor.append(self.byte_array_a[i*size:(i+1)*size])
	def buildEnv(self):
		size = int(len(self.byte_array_b) ** 0.5)
		for i in size:
			self.environment.append(self.byte_array_b[i*size:(i+1)*size])
	def getFloor(self):
		return 'f%s %s' % (self.location, self.byte_array_a)
	def getEnvironment(self):
		return 'f%s %s' % (self.location, self.byte_array_a)
class Map:
	def __init__(self, size):
		self.size = size
		self.folder_location = 'Map'
		self.map = {}
		self.loadMap()
	def loadMap(self):
		for i in range(self.size):
			for j in range(self.size):
				file = open('%s/%d_%d.SAM' % (self.folder_location, i-self.size/2, j-self.size/2), 'rb')
				byte_array_a = file.read()
				file.close()
				chunk = Chunk('%d_%d' % (i, j), byte_array_a, None)
				size = int(len(temp)**0.5)
				#for y in range(size):
					
# Client
		
		
		
		
		
		
		
		
		
		
		
		