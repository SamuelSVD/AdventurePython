#!/usr/bin/env python
# The directions are going to be in this order:
#	U	UR	R	DR	D	DL	L	UL
#	0	1	2	3	4	5	6	7
import time
import math
import pygame
from pygame.locals import *
import os
import os.path

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
		#pygame.draw.rect(s, (10,10,20),(0,0,self.shad_size[0],self.shad_size[1]))
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

#------------- Images ---------------------------------------------------------------------------------- #
class Animation:
	def __init__(self, images, delay, order):
		self.images = images
		self.delay = delay
		self.order = order
		self.count = 0
		self.current_time = 0
		self.next_time = delay
	def update(self,delta):
		self.current_time += delta
		if self.current_time > self.next_time:
			self.next_time = self.current_time + self.delay
			self.count += 1
	def getImage(self):
		i = self.count % len(self.order)
		return self.images[self.order[i]]
	def reset(self):
		self.count = 0
		self.current_time = 0
		self.next_time = self.delay
class TextureLoader:
	def __init__(self):
		self.items = []
		self.floor_texture = []
		self.environment_texture = []
		self.characters = {}
		self.mobs = {}
		self.character_base = {}
		self.hair_base = {}
		self.directory = 'Animation/64x64/'
		self.loadItems()
		self.loadCharacters()
		self.loadMobs()
		#self.loadBase()
		self.loadEnvironmentTexture()
		self.loadFloorTexture()
	def loadItems(self):
		for name in sorted(os.listdir(self.directory + 'Items')):
			self.items.append(pygame.image.load(self.directory + 'Items/' + name))
	def loadCharacters(self):
		for name in sorted(os.listdir(self.directory + 'Characters')):
			char = (pygame.image.load(self.directory + 'Characters/' + name))
			name = name[0:-4]
			self.characters[name] = char
	def loadMobs(self):
		for name in sorted(os.listdir(self.directory + 'Mobs')):
			mob = (pygame.image.load(self.directory + 'Mobs/' + name))
			name = name[0:-4]
			self.mobs[name] = mob
	def loadBase(self):
		for name in sorted(os.listdir(self.directory + 'Base/Character')):
			character_base = (pygame.image.load(self.directory + 'Base/Character/' + name))
			name = name[0:-4]
			self.character_base[name] = character_base
		for name in sorted(os.listdir(self.directory + 'Base/Hair')):
			hair_base = (pygame.image.load(self.directory + 'Base/Hair/' + name))
			name = name[0:-4]
			self.hair_base[name] = hair_base
	def loadFloorTexture(self):
		if not os.path.isfile('Texture.png'):
			print 'Texture file not found.'
			return
		image = pygame.image.load('Texture.png')
		for j in range(2):
			for i in range(10):
				floor = pygame.Surface((32,32))
				floor.blit(image, (0,0), (32*i, 32*j, 32,32))
				self.floor_texture.append(floor)
	def loadEnvironmentTexture(self):
		if not os.path.isfile('Environment.png'):
			print 'Env. texture file not found.'
			return
		image = pygame.image.load('Environment.png')
		size = image.get_size()[0]/32
		for i in range(size):
			print 'loading...', i
			env = pygame.Surface((32,64),pygame.SRCALPHA)
			env.blit(image, (0,0), (32*i, 0, 32,64))
			self.environment_texture.append(env)
	def getAnimation(self, image, ordinal):
		num = 3
		delay = 0.2
		order = [0,1,2,1]
		if ordinal < 8:
			pass
		elif ordinal < 16:
			num = 2
			delay = 0.5
			order = [0,1]
		elif ordinal < 24:
			num = 3
			delay = 0.5
			order = [0,1]
		return createAnimation(image,(0,ordinal*64),(64,64),num,delay,order)
	def buildCharacterAnimations(self, skin, hair):
		skin = self.character_base[skin]
		hair = self.hair_base[hair]
		image = pygame.surface.Surface(skin.get_size(), pygame.SRCALPHA)
		image.fill((0,0,0,0))
		image.set_alpha(0)
		image.blit(skin, (0,0))
		image.blit(hair, (0,0))
		anims = []
		for i in range(24):
			anims.append(self.getAnimation(image, i))
		return anims
	def getCharacterAnimation(self, name, ordinal): #returns a single animation of the selected ordinal.
		num = 3
		delay = 0.2
		order = [0,1,2,1]
		if ordinal < 8:
			pass
		elif ordinal < 16:
			num = 2
			delay = 0.5
			order = [0,1]
		elif ordinal < 24:
			num = 3
			delay = 0.5
			order = [0,1]
		try:
			return createAnimation(self.characters[name],(0,ordinal*64),(64,64),num,delay,order)
		except:
			return createAnimation(self.characters['character'],(0,ordinal*64),(64,64),num,delay,order)
	def getCharacterAnimations(self, name): #returns the complete set of the selected animation
		if name in self.characters:
			anims = []
			for i in range(24):
				anims.append(self.getCharacterAnimation(name, i))
			return anims
		else:
			anims = []
			for i in range(24):
				anims.append(self.getCharacterAnimation('character', i))
			return anims
	def getFloor(self, num):
		if num >= len(self.floor_texture) or num < 0:
			return pygame.Surface((1,1))
		return self.floor_texture[num]
	def getEnvironment(self, num):
		if num >= len(self.environment_texture) or num < 0:
			img = pygame.Surface((1,1),pygame.SRCALPHA)
			img.set_alpha(0)
			return img
		return self.environment_texture[num]
def createAnimation(image,start,size,num,delay,order):
	textures = []
	for i in range(num):
		s = pygame.Surface(size,pygame.SRCALPHA)
		s.blit(image, (0,0),(start[0]+size[0]*i,start[1],size[0],size[1]))
		textures.append(s)
	return Animation(textures, delay, order)
texture_loader = TextureLoader()

# ------------ Login GUI ------------------------------------------------------------------------------ #
class Window:
	def __init__(self,title = None,x = 0,y = 0,width = 0,height = 0,color = (0,0,0), titleColor = (255,255,255)):
		self.title = title
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.titleColor = titleColor
		self.buttons = []
	def addButton(self, name, x, y, width, height, bgColor = None, nameColor = (255,255,255), function = None, parameters = None):
		self.buttons.append([name,x,y,width,height,bgColor, nameColor, function, parameters])
	def getButton(self, num):
		return self.buttons[num]
	def handleClick(self, click):
		click = [click[0] - self.x, click[1] - self.y]
		for button in self.buttons:
			if click[0] > button[1] and click[0] <= button[1] + button[3] and click[1] > button[2] and click[1] <= button[2] + button[4]:
				if button[7] and button[8]:
					#print button[8]
					apply(button[7],button[8])
					return True
				elif button[7]:
					button[7]()
					return True
		if click[0] > 0 and click[0] < self.width and click[1] > 0 and click[1] < self.height:
			return True
	def drawWindow(self, screen, font = None, titleFont = None):
		pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height))
		lighter_shade = (self.color[0] * 1.1, self.color[1] * 1.1, self.color[2] * 1.1)
		for c in lighter_shade:
			if c > 255:
				c = 255
			elif c < 0:
				c = 0
		darker_shade = (self.color[0] * 0.9, self.color[1] * 0.9, self.color[2] * 0.9)
		for c in darker_shade:
			if c > 255:
				c = 255
			elif c < 0:
				c = 0
		pygame.draw.rect(screen, darker_shade, (self.x,self.y,self.width,self.height),1)
		
		if self.title:
			if titleFont:
				s = titleFont.size(self.title)[1]
				pygame.draw.rect(screen,darker_shade,(self.x,self.y,self.width,s+4),1)
				pygame.draw.rect(screen,lighter_shade,(self.x+1,self.y+1,self.width-2,s+2),1)
				
				screen.blit(titleFont.render(self.title,1,self.titleColor),(self.x + 2,self.y + 2))
			elif font:
				s = font.size(self.title)[1]
				pygame.draw.rect(screen, darker_shade,(self.x,self.y,self.width,s+4),1)
				pygame.draw.rect(screen,lighter_shade,(self.x+1,self.y+1,self.width-2,s+2))
				screen.blit(font.render(self.title,1,self.titleColor),(self.x + 2,self.y + 2))
		for button in self.buttons:
			if button[5]:
				pygame.draw.rect(screen,button[5],(self.x + button[1],self.y + button[2],button[3],button[4]))
		if font:
			for button in self.buttons:
				screen.blit(font.render(button[0],1,button[6]),(self.x + button[1] + 2,self.y + button[2] + 2))
def makeLoginWindow(client):
	login_window = Window('Login',260,175,280,150,(200,134,123))
	login_window.addButton(client.text[0],100,35,150,20, (160,107,98),function = LoginClient.setSelection, parameters = (client,0))
	login_window.addButton('*' * len(client.text[1]),100,65,150,20, (160,107,98),function = LoginClient.setSelection, parameters = (client,1))
	login_window.addButton('Username',20,38,0,0)
	login_window.addButton('Password',20,68,0,0)
	login_window.addButton('Login',120,105,60,25,function = client.login)
	login_window.addButton('Register',460,400,60,25, function = client.toggleMode)
	return login_window
def makeRegisterWindow(client):
	register_window = Window('Register',260,175,280,200,(200,134,123))
	register_window.addButton('Username',20,38,0,0)
	register_window.addButton(client.text[0],100,35,150,20, (160,107,98),function = LoginClient.setSelection, parameters = (client, 0))
	register_window.addButton('Password',20,68,0,0)
	register_window.addButton(client.text[1],100,65,150,20, (160,107,98),function = LoginClient.setSelection, parameters = (client, 1))
	register_window.addButton('Re-enter',20,92,0,0)
	register_window.addButton('password',20,107,0,0)
	register_window.addButton(client.text[2],100,95,150,20, (160,107,98),function = LoginClient.setSelection, parameters = (client, 2))
	register_window.addButton('Login',460,400,60,25, function = client.toggleMode)
	register_window.addButton('Cancel',150,150,60,25,function = client.toggleMode)
	register_window.addButton('Register',70,150,60,25,function = client.register)
	return register_window
def makePopUp(title, message, array):
	popup_window = Window(title,260,195,280,120,(200,134,123))
	if len(message) > 28:
		message = message.split()
		total = 0
		messages = []
		s = ''
		for i in range(len(message)):
			if total + len(message[i]) > 28:
				messages.append(s)
				s = ''
			s += (message[i]+ ' ')
		messages.append(s)
		for i in range(len(messages)):
			popup_window.addButton(messages[i], 20,50 + 18 * i,0,0)
	else:
		popup_window.addButton(message, 20,50,0,0)
	popup_window.addButton('    OK',110,90,60,25,(190,124,113),function = array.remove,parameters = [popup_window])
	array.append(popup_window)

# ------------ Component ------------------------------------------------------------------------------ #
class Component:
	def __init__(self):
		self.adventure = None
		self.visible = True
		self.active = True
		self.queue_tcp = []
		self.queue_udp = []
	def draw(self, screen):
		pass
	def update(self, delta = None):
		pass
	def handleKey(self, key_event):
		pass
	def handleMouse(self, mouse_event):
		pass
	def handleMessageTCP(self, message):
		pass
	def handleMessageUDP(self, message):
		pass
	def getQueueTCP(self):
		q = self.queue_tcp
		self.queue_tcp = []
		return q
	def getQueueUDP(self):
		q = self.queue_udp
		self.queue_udp = []
		return q
	def isActive(self):
		return self.active
	def isVisible(self):
		return self.visible
	def setAdventure(self, adventure):
		self.adventure = adventure
# ------------ Components ------------------------------------------------------------------------------ #
class LoginClient(Component):
	def __init__(self):
		Component.__init__(self)
		self.title_image = pygame.image.load('title.png')
		self.text = ['','','']
		self.text = ['Ravages','abcd123','']
		self.font = pygame.font.SysFont('calibri', 16, True, False)
		self.selection = 0
		self.mode = 'LOGIN'
		self.loginFailed = False
		self.registerFailed = False
		self.registerSuccess = False
		self.message = ''
		self.popups = []
		self.login_window = makeLoginWindow(self)####
		self.register_window = makeRegisterWindow(self)####
	def draw(self, screen):
		screen.blit(self.title_image, (0,0))
		if self.mode == 'LOGIN':
			self.login_window.drawWindow(screen, self.font)
		elif self.mode == 'REGISTER':
			self.register_window.drawWindow(screen, self.font)
		for pop in self.popups:
			pop.drawWindow(screen, self.font)
	def update(self, delta = None):
		if self.mode == 'LOGIN':
			self.login_window = makeLoginWindow(self)####
		elif self.mode == 'REGISTER':
			self.register_window = makeRegisterWindow(self)####
		if self.loginFailed:
			self.loginFailed = False
			makePopUp('Login Failed',self.message,self.popups)
		if self.registerFailed:
			self.registerFailed = False
			makePopUp('Register Failed',self.message,self.popups)
		if self.registerSuccess:
			self.registerSuccess = False
			makePopUp('Registered',self.message,self.popups)
	def handleKey(self, key_event):
		if key_event.type == pygame.KEYDOWN:
			letter = key_event.unicode
			add = False
			if len(letter) == 0:
				#print letter
				add = False
			elif ord(letter) >= 48 and ord(letter) <= 57:
				add = True
			elif ord(letter) >= 65 and ord(letter) <= 90:
				add = True
			elif ord(letter) == 95:
				add = True
			elif ord(letter) >= 97 and ord(letter) <= 122:
				add = True
			elif ord(letter) == 8: # Handle Backspace
				self.text[self.selection] = self.text[self.selection][0:-1]
				#print client.text
			elif ord(letter) == 9: # Handle Tab
				if self.selection == 0 or self.selection == 1:
					self.selection += 1
					self.selection = self.selection % 2
			if add:
				if len(self.text[self.selection]) < 13:
					self.text[self.selection] += letter
	def handleMouse(self, mouse_event):
		if mouse_event.type == pygame.MOUSEBUTTONDOWN:
			hasClicked = False
			mousePos = pygame.mouse.get_pos()
			for pop in self.popups:
				if not hasClicked:
					hasClicked = pop.handleClick(mousePos)
			if self.mode == 'LOGIN' and not hasClicked:
				hasClicked = self.login_window.handleClick(mousePos)
			elif self.mode == 'REGISTER' and not hasClicked:
				hasClicked = self.register_window.handleClick(mousePos)
	def handleMessageTCP(self, message):
#		print 'LoginClient handling:\t%s' % message
		message_type = message[0]
		message = message[1:]
		if message_type == 'r':
			decider = int(message[0])
			message = message[1:]
			if decider:
				self.mode = 'LOGIN'
				self.registerSuccess = True
				self.message = message
			else:
				self.registerFailed = True
				self.message = message
		elif message_type == 'l':
			decider = int(message[0])
			message = message[1:]
			if decider:
#				print 'Logged in! %s' % message
				self.adventure.setState(2)
				self.adventure.username = message
				self.message = ''
			else:
				self.loginFailed = True
				self.message = message
	def setSelection(self, num):
#		print num
		self.selection = num
	def toggleMode(self):
#		print 'toggling Mode'
		if self.mode == 'LOGIN':
			self.mode = 'REGISTER'
			self.text = ['','','']
			self.selection = 0
		elif self.mode == 'REGISTER':
			self.mode = 'LOGIN'
			self.text = ['','','']
			self.selection = 0
	def register(self):
		if len(self.text[0]) == 0 or len(self.text[1]) == 0:
			self.registerFailed = True
			self.message = 'Entry blank.'
			return
		if self.mode == 'REGISTER':
			if self.text[1] == self.text[2]:
#				print 'Registering',self.text[0],self.text[1]
				self.queue_tcp.append('R%s %s' % (str(self.text[0]),str(self.text[1])))
			else:
				self.registerFailed = True
				self.message = 'Passwords must match.'
	def login(self):
		if len(self.text[0]) == 0 or len(self.text[1]) == 0:
			self.loginFailed = True
			self.message = 'Please enter a Username and Password'
			return
		self.queue_tcp.append('L%s %s' % (str(self.text[0]),str(self.text[1])))
class Fade(Component):
	def __init__(self, fade_in_time, wait_time, fade_out_time, animation, visible = False, active = False, fade_out_conditions = [], end_function= None, end_parameters = None):
		Component.__init__(self)
		self.fade_in_time = fade_in_time
		self.fade_in_count = 0
		self.wait_time = wait_time
		self.wait_count = 0
		self.fade_out_time = fade_out_time
		self.fade_out_count = 0
		self.animation = animation
		self.fade_out_conditions = fade_out_conditions
		self.end_function = end_function
		self.end_parameters = end_parameters
		pygame.font.init()
		self.font = pygame.font.SysFont('calibri', 24)
		self.previous_time = time.time()
		self.time_running = 0
		self.state = 'Invisible'
	def draw(self, screen):
		#print 'drawin Fade', self.visible
		if not self.visible:
			return

		size = screen.get_size()
		temp_screen = pygame.surface.Surface(size)#, pygame.SRCALPHA)
		if self.state == 'Invisible'or self.state == 'Done':
			temp_screen.set_alpha(0)
		elif self.state == 'IN':
			temp_screen.set_alpha(255*(self.fade_in_count/self.fade_in_time))
		elif self.state == 'OUT':
			temp_screen.set_alpha(255*(1 - self.fade_out_count/self.fade_out_time))
		temp_screen.fill((15,15,15))
		s = 'Loading'
		s += '.'*int(self.time_running%5)
		temp_screen.blit(self.font.render(s,1,(255,255,255)),(size[0] - 200, size[1] - 100))
		temp_screen.blit(self.animation.getImage(), (size[0] - 128, size[1] - 128))
		screen.blit(temp_screen, (0,0))
		if 0:
			screen.blit(self.font.render('In:',1,(255,255,255)),(10,10))
			screen.blit(self.font.render('Out:',1,(255,255,255)),(10,35))
			screen.blit(self.font.render('Running:',1,(255,255,255)),(10,60))
			screen.blit(self.font.render('%0.2f' % self.fade_in_count, 1, (255,255,255)), (100, 10))
			screen.blit(self.font.render('%0.2f' % self.fade_out_count, 1, (255,255,255)), (100, 35))
			screen.blit(self.font.render('%0.2f' % self.time_running, 1, (255,255,255)), (100, 60))
			screen.blit(self.font.render(self.state, 1, (255,255,255)), (10, 75))		
	def update(self, delta = None):
		#print 'Updating Fade'
		if not delta:
			delta = time.time() - self.previous_time
			self.previous_time = time.time()
		if self.state == 'Invisible':
			self.state = 'IN'
		if self.state == 'IN':
			self.fade_in_count += delta
			if self.fade_in_time - self.fade_in_count < 0:
				self.state = 'Visible'
				self.fade_in_count = 0
		elif self.state == 'OUT':
			self.fade_out_count += delta
			if self.fade_out_time - self.fade_out_count < 0:
				self.state = 'Done'
				self.__finish__()
				self.fade_out_count = 0
		elif self.state == 'Visible':
			if self.wait_time - self.wait_count < 0:
				move_on = False
				for condition in self.fade_out_conditions:
					if apply(condition,):
						move_on = True
					else:
						move_on = False
						break
				if move_on:
					self.state = 'OUT'
					self.wait_count = 0
			else:
				self.wait_count += delta
		self.time_running += delta
		self.animation.update(delta)
	def handleMouse(self,mouse_event):
		return
		if self.state == 'Invisible':
			self.state = 'IN'
		elif self.state == 'IN':
			self.state = 'Visible'
		elif self.state == 'Visible':
			self.state = 'OUT'
		elif self.state == 'OUT':
			self.state = 'Invisible'
	def handleMessageTCP(self, message):
#		print 'Fade handling:\t%s' % message
		self.adventure.gameplay.handleMessageTCP(message)
	def fadeIn(self):
		self.state = 'IN'
	def fadeOut(self):
		self.state = 'OUT'
	def reset(self):
		self.state = 'Invisible'
		self.previous_time = time.time()
		self.fade_in_count = 0
		self.wait_count = 0
		self.fade_out_count = 0
		self.time_running = 0
	def __finish__(self):
		if self.end_function:
			apply(self.end_function, self.end_parameters)
class TextWindow(Component):
	def __init__(self, maxCoord, minCoord, width, font, bg = (150,150,150), textBar_bg = (150,150,150)):
		Component.__init__(self)
		self.maxCoord = maxCoord
		self.minCoord = minCoord
		self.width = width
		self.height = (self.minCoord[1]-self.maxCoord[1])
		
		self.message = ''
		self.messages = []
		self.lines = []
		self.line_height = font.get_linesize() + 2
		self.lines_height = 0
		self.line_limit = 100
		
		self.font = font
		self.bg = bg
		self.textBar_bg = textBar_bg
		self.maximized = True
		self.selected = True # may be equal to self.maximized

		self.maxHeight = (self.minCoord[1]-self.maxCoord[1])
		self.minHeight = font.get_linesize() + 2
		self.height = self.minHeight * 3
		self.transparency = 250

		self.window_surface = pygame.Surface((self.width, self.height))
		self.text_surface = pygame.Surface((self.width, self.line_height))

		self.scroll = 0
		self.resizing = False
		self.initHeight = None # initial height when resizing
		self.startResize = None # coordinate of where the initial click was done.
		
		self.focus = False
	def draw(self, screen):
		self.window_surface.fill(self.bg)
		for i in range(len(self.lines)):
			self.window_surface.blit(self.font.render(self.lines[i],0,(0,0,0)),(6,self.height+ 3 - (self.line_height) * (len(self.lines) - i) + self.line_height * self.scroll))
			self.window_surface.blit(self.font.render(self.lines[i],1,(255,255,255)),(5,self.height+ 2 - (self.line_height) * (len(self.lines) - i) + self.line_height * self.scroll))
		pygame.draw.rect(self.window_surface, (0,0,0),(0,0,self.width,self.height),1)
		
		self.text_surface.fill(self.textBar_bg)
		size = self.font.size(self.message)
		if size[0] < self.width - 10:
			self.text_surface.blit(self.font.render(self.message,1,(0,0,0)),(6,4))
			self.text_surface.blit(self.font.render(self.message,1,(255,255,255)),(5,3))
		else:
			self.text_surface.blit(self.font.render(self.message,1,(0,0,0)),(self.width - 6 - size[0],4))
			self.text_surface.blit(self.font.render(self.message,1,(255,255,255)),(self.width - 5 - size[0],3))
		pygame.draw.rect(self.text_surface, (0,0,0),(0,0,self.width, self.line_height),1)
		
		self.text_surface.set_alpha(self.transparency)
		self.window_surface.set_alpha(self.transparency)
		
		if self.maximized:
			screen.blit(self.window_surface, (self.maxCoord[0], self.minCoord[1] - self.height))
		screen.blit(self.text_surface, self.minCoord)
	def handleKey(self, key_event):# key pressed on the keyboard.
		#print 'Text handling key event'
		if key_event.type == pygame.KEYDOWN:
			letter = key_event.unicode
			if len(letter) == 0:
				return
			elif ord(letter) >= 32 and ord(letter) <= 126: # from space to ~
				if len(self.message) < 100:
					self.message += str(letter)
				else:
					print 'message limit reached'
			elif ord(letter) == 8:   # Backspace
				self.message = self.message[0:-1]
			elif ord(letter) == 13:  # Enter
				self.focus = False
				if len(self.message) == 0:
					return
				self.queue_tcp.append('T%s'%self.message)
				self.message = ''
	def handleMouse(self, event):
		if event.type == pygame.MOUSEMOTION:
			'Motion!'
			if self.resizing:
				mousePos = pygame.mouse.get_pos()
				self.height = self.initHeight + self.startResize[1] - mousePos[1]
				if self.height > self.maxHeight:
					self.height = self.maxHeight
				elif self.height < self.minHeight:
					self.height = self.minHeight
				
				self.window_surface = pygame.Surface((self.width, self.height))
		elif event.type == pygame.MOUSEBUTTONDOWN:
			button = event.dict['button']
			if self.clickInBounds(event):
				self.focus = True
			else:
				self.focus = False
			if button == 1:
				#print 'left-click'
				if self.maximized:
					mousePos = pygame.mouse.get_pos()
					top = (self.maxCoord[0], self.minCoord[1] - self.height)
					#print 'trying to resize'
					#print mousePos[0],mousePos[1],top[0], top[0] + self.width, top[1], top[1] + 10
					if mousePos[0] > top[0] and mousePos[0] < top[0] + self.width and mousePos[1] > top[1] and mousePos[1] < top[1] + 10:
						#print 'resize start'
						self.resizing = True
						self.initHeight = self.height
						self.startResize = mousePos
				'left'
			elif button == 2:
				'middle'
			elif button == 3:
				'right'
			elif button == 4:
				if self.clickInBounds(event):
					height = self.height / self.line_height
					if len(self.lines) > height and not self.scroll - len(self.lines) > - height - 1:
						self.scroll += 1
					#print 'scroll-up'
			elif button == 5:
				if self.clickInBounds(event):
					if not self.scroll == 0:
						self.scroll -= 1
					#print 'scroll-down'
			
		elif event.type == pygame.MOUSEBUTTONUP:
			button = event.dict['button']
			if button == 1:
				self.resizing = False
			'Release!'
	def handleMessageTCP(self, message):
#		print 'TextWindow handling:\t%s'%message
		if message[0] == 't':
			self.addMessage(message[1:])
	def clickInBounds(self, click_event):
		try:
			mousePos = pygame.mouse.get_pos()
			if self.maximized:
				mousePos = (mousePos[0] - self.maxCoord[0], mousePos[1] - self.minCoord[1] + self.height)
				#print mousePos[0],mousePos[1]
				if mousePos[0] > 0 and mousePos[0] < self.width and mousePos[1] > 0 and mousePos[1] < self.height + self.line_height:
					return True
		except:
			#print 'error'
			return
	def addMessage(self, message):
		while len(self.messages) > 50:
			self.messages.pop(0)
		self.messages.append(message)
		self.__addLine__(message)
	def splitIndex(self, message, word, limit, font, index = 0):
		half = len(word)/2
		bottomHalf = word[0:half]
		topHalf = word[half:len(word)]
		message_width = font.size(message)[0]
		bottom_width = font.size(bottomHalf)[0]
		if len(bottomHalf) == 0:
			return index
		elif message_width + bottom_width < limit:
			return self.splitIndex(message+bottomHalf,topHalf,limit,font, index + len(bottomHalf))
		else:
			return self.splitIndex(message, bottomHalf, limit, font, index)
	def __addLine__(self, message):
		''
		#print '-------',i
		size = self.font.size(message)[0]
		#print size, self.width - 10, size >self.width - 10
		if size > self.width - 10:
			temp_messages = []
			temp = ''
			message = message.split(' ')
			for word in message:
				#print word
				#print temp_messages
				if len(word) < 10:
					word_length = self.font.size(word)[0]
					temp_length = self.font.size(temp)[0]
					if word_length + temp_length > self.width - 10:
						temp_messages.append(temp)
						temp = ''
				while word:
					#print word
					word_length = self.font.size(word)[0]
					temp_length = self.font.size(temp)[0]
					temp_word = ''
					#print word, word_length,temp_length
					if word_length + temp_length > self.width - 10:
						index = self.splitIndex(temp, word, self.width - 10, self.font)
						temp += word[0:index] + ' '
						temp_messages.append(temp)
						temp = ''
						word = word[index:len(word)]
					else:
						temp += word + ' '
						word = ''
			if temp:
				temp_messages.append(temp)
			#print temp_messages
			for i in range(len(temp_messages)):
				self.lines.append(temp_messages[i])
		else:
			self.lines.append(message)
		while len(self.lines) > self.line_limit:
			self.lines.pop(0)
		self.lines_height = self.line_height * len(self.lines)
class Gameplay(Component):
	def __init__(self,character = None):
		Component.__init__(self)
		self.character = character
		self.entities = []
		self.map = Map()
		self.previousTime = time.time()
		self.terminate = False
		self.font = pygame.font.SysFont('calibri', 16)
		self.text_window = TextWindow((20,20),(20,550),600,self.font, (114,107,101))
		
		self.chunk_size = 20
		self.block_size = 32
		
		self.total_time = 0
		self.poll_delay = 0.5
		self.nextPoll = self.total_time + self.poll_delay
		
		self.corners = []
	def draw(self, screen):
		if not self.character:
			return
		
		chunk_height = 20
		
		offset = screen.get_size()
		offset = (offset[0]/2,offset[1]/2)

		character_blocks_y = int(math.floor(self.character.position.y/32.0))
		character_chunk_y = int(math.floor(character_blocks_y/20.0))
		character_block_y = character_blocks_y - character_chunk_y * 20

		character_blocks_x = int(math.floor(self.character.position.x/32.0))
		character_chunk_x = int(math.floor(character_blocks_x/20.0))
		character_block_x = character_blocks_x - character_chunk_x * 20

		# Get how many rows fit on the screen. 
		height = screen.get_height()/32 + 4
		# The starting row to draw is the character's row 
		starting_row = character_block_y - height/2 + 1
		starting_chunk = -1
		# The starting chunk to draw is the one above.
		rows_drawn = 0 
		for i in range(-1,2):
			for j in range(-1,2):
				self.map.drawFloor(screen, self.character, offset, '%d_%d' % (character_chunk_x + i, character_chunk_y + j))
		if starting_row < 0:
			starting_chunk = -1
			starting_row =chunk_height + starting_row
			toBeDrawn = [[],[],[]]
			for entity in self.entities:
				entity_block_y = int(math.floor(entity.position.y/32.0))
				entity_chunk_y = int(math.floor(entity_block_y/20.0))
				entity_block_y -= entity_chunk_y * 20
				if entity_chunk_y == character_chunk_y - 1:
					if not entity_block_y < starting_row:
						toBeDrawn[0].append(entity)
				elif entity_chunk_y == character_chunk_y:
					if not height - (chunk_height-starting_row + entity_block_y) < 0:
						toBeDrawn[1].append(entity)
				elif entity_chunk_y == character_chunk_y + 1:
					if not height - (chunk_height*2-starting_row + entity_block_y) < 0:
						toBeDrawn[2].append(entity)
			
		else:
			starting_chunk = 0
			toBeDrawn = [[],[]]
			for entity in self.entities:
				entity_block_y = int(math.floor(entity.position.y/32.0))
				entity_chunk_y = int(math.floor(entity_block_y/20.0))
				entity_block_y -= entity_chunk_y * 20
				if entity_chunk_y == character_chunk_y:
					if not height - (entity_block_y - starting_row) < 0:
						toBeDrawn[0].append(entity)
				elif entity_chunk_y == character_chunk_y + 1:
					if not height - (chunk_height - starting_row + entity_block_y) < 0:
						toBeDrawn[1].append(entity)
		#	Now comes the sorting.
		def sort(entity):
			return entity.position.y
		for i in range(len(toBeDrawn)):
			toBeDrawn[i].sort(None, sort, False)

		#	Now to draw row by row of the two chunks beside it.
		for chunk_row in range (starting_chunk, 2):
			for block_row in range(starting_row, chunk_height):
				rows_drawn += 1
				for list_of_entities in toBeDrawn:
					entities_drawn = 0
					for entity in list_of_entities:
						entity_block_y = int(math.floor(entity.position.y/32.0))
						entity_chunk_y = int(math.floor(entity_block_y/20.0))
						entity_block_y -= entity_chunk_y * 20
						if entity_chunk_y == character_chunk_y + chunk_row and block_row == entity_block_y:
							entities_drawn += 1
							x = entity.position.x - self.character.position.x
							y = entity.position.y - self.character.position.y
							
							image = entity.getShadow()
							size = image.get_size()
							relative_position = Vector(entity.position.x - self.character.position.x, entity.position.y - self.character.position.y)
							screen.blit(image,(relative_position.x-size[0]*0.5+offset[0],relative_position.y-size[1]*0.5+offset[1]))
							image = entity.getImage()
							size = image.get_size()
							screen.blit(image,(relative_position.x-size[0]/2+offset[0],relative_position.y-size[1]*0.7+offset[1]))
				for i in range(entities_drawn):
					if len(toBeDrawn[0]) == 0:
						toBeDrawn.pop(0)
					if len(toBeDrawn[0]) == 0:
						toBeDrawn.pop(0)
					toBeDrawn[0].pop(0)
				for i in range(-1,2):
					self.map.drawRow(screen,self.character,offset,'%d_%d' % (character_chunk_x + i, character_chunk_y + chunk_row), block_row)
				if rows_drawn == height:
					break
			starting_row = 0
			if rows_drawn == height:
				break
		#print height, rows_drawn
		self.text_window.draw(screen)
		
		if 1 and self.character:
			messages = []
			messages.append(['CB:  %0.0f  %0.0f' % (character_blocks_x, character_blocks_y),(10,10)])
			messages.append(['CC: (%0.0f, %0.0f)  (%0.0f, %0.0f)' % (character_chunk_x, character_chunk_y, character_block_x, character_block_y), (10,20)])
			messages.append(['E:  %d' % len(self.entities),(10,30)])
			messages.append([str(self.map.isSolidAt('%d_%d' % (character_chunk_x, character_chunk_y), (character_block_x, character_block_y))), (10,50)])
			messages.append([str(self.text_window.focus), (10,60)])
			for message in messages:
				screen.blit(self.font.render(message[0], 1, (0,0,0)), (message[1][0] + 1, message[1][1] - 1))
				screen.blit(self.font.render(message[0], 1, (255,255,255)), message[1])
	def update(self, delta = None):
		if not self.character:
			return
		if not delta:
			delta = time.time() - self.previousTime
		self.previousTime = time.time()
		self.total_time += delta
		if self.total_time > self.nextPoll:
			self.nextPoll = self.total_time + self.poll_delay
			self.poll()

		for entity in self.entities:
			#get initial position
			#update normally, if collision occurs, check if the block(s) in the direction of the entity are solid or not

			#We need to look at the four corners of the entity. these corners are determined by the shadow of the entity
			size = entity.getShadow().get_size()
			pos_x = entity.position.x
			pos_y = entity.position.y
			entity.update(delta)
			#corners can be done by checking (pos (+/-) (size/2))/ 32 if == pos/32 ignore corner. (???)
			is_solid = []
			collision_dir = [0,0,0,0]
			for j in range(2):
				for i in range(2):
					y = -1
					x = -1
					if i:
						x = 1
					if j:
						y = 1
					x = entity.position.x + size[0]/2 * x
					y = entity.position.y + size[1]/2 * y
					corner_block_y = int(math.floor(y/32.0))
					corner_chunk_y = int(math.floor(corner_block_y/20.0))
					corner_block_y -= corner_chunk_y * 20
					corner_block_x = int(math.floor(x/32.0))
					corner_chunk_x = int(math.floor(corner_block_x/20.0))
					corner_block_x -= corner_chunk_x * 20
					is_solid.append(self.map.isSolidAt('%d_%d' % (corner_chunk_x, corner_chunk_y), (corner_block_x, corner_block_y)))
			# is_solid = ['TOP_LEFT', 'TOP_RIGHT', 'BOT_LEFT', 'BOT_RIGHT']
			if is_solid[0]:
				if is_solid[1]:
					if is_solid[2]:
						if is_solid[3]:	# 0 1 2 3
							entity.position.x = pos_x
							entity.position.y = pos_y
						else:			# 0 1 2
							#TOP_LEFT corner
							collision_dir[0] = 1
							collision_dir[3] = 1
					elif is_solid[3]:	# 0 1 3
						#TOP_RIGHT corner
						collision_dir[0] = 1
						collision_dir[1] = 1
					else:				# 0 1
						#TOP
						collision_dir[0] = 1
				elif is_solid[2]:
					if is_solid[3]:		# 0 2 3
						#BOT_LEFT
						collision_dir[2] = 1
						collision_dir[3] = 1
					else:				# 0 2
						#LEFT
						collision_dir[3] = 1
				elif is_solid[3]:		# 0 3
					entity.position.x = pos_x
					entity.position.y = pos_y
				else:					# 0
					if entity.direction == 5 or entity.direction == 6:
						collision_dir[3] = 1
					elif entity.direction == 0 or entity.direction == 1:
						collision_dir[0] = 1
					elif entity.direction == 7:
						dy = abs(int(math.floor(entity.position.y / 32.0)) * 32 - (entity.position.y - size[1]/2))
						dx = abs(int(math.floor(entity.position.x / 32.0)) * 32 - (entity.position.x - size[0]/2))
						if dy > dx:
							collision_dir[3] = 1
						else:
							collision_dir[0] = 1
			elif is_solid[1]:
				if is_solid[2]:
					if is_solid[3]:		# 1 2 3
						collision_dir[1] = 1
						collision_dir[2] = 1
					else:				# 1 2
						entity.position.x = pos_x
						entity.position.y = pos_y
				elif is_solid[3]:		# 1 3
					collision_dir[1] = 1
				else:					# 1
					if entity.direction == 7 or entity.direction == 0:
						collision_dir[0] = 1
					elif entity.direction == 2 or entity.direction == 3:
						collision_dir[1] = 1
					elif entity.direction == 1:
						dy = abs(int(math.floor(entity.position.y / 32.0)) * 32 - (entity.position.y - size[1]/2))
						dx = abs(int(math.floor(entity.position.x / 32.0) + 1) * 32 - (entity.position.x + size[0]/2))
						if dy > dx:
							collision_dir[1] = 1
						else:
							collision_dir[0] = 1
			elif is_solid[2]:
				if is_solid[3]:			# 2 3
					collision_dir[2] = 1
				else:					# 2
					if entity.direction == 3 or entity.direction == 4:
						collision_dir[2] = 1
					elif entity.direction == 6 or entity.direction == 7:
						collision_dir[3] = 1
					elif entity.direction == 5:
						dy = abs(int(math.floor(entity.position.y / 32.0) + 1) * 32 - (entity.position.y + size[1]/2))
						dx = abs(int(math.floor(entity.position.x / 32.0)) * 32 - (entity.position.x - size[0]/2))
						if dy > dx:
							collision_dir[3] = 1
						else:
							collision_dir[2] = 1						
			elif is_solid[3]:			# 3
				if entity.direction == 1 or entity.direction == 2:
					collision_dir[1] = 1
				elif entity.direction == 4 or entity.direction == 5:
					collision_dir[2] = 1
				elif entity.direction == 3:
					dy = abs(int(math.floor(entity.position.y / 32.0) + 1) * 32 - (entity.position.y + size[1]/2))
					dx = abs(int(math.floor(entity.position.x / 32.0) + 1) * 32 - (entity.position.x + size[0]/2))
					if dy > dx:
						collision_dir[1] = 1
					else:
						collision_dir[2] = 1
					
			if collision_dir[0]:	#TOP Collision
				entity.position.y = pos_y - pos_y % 32 + size[1]/2
			elif collision_dir[2]:	#BOT Collision
				entity.position.y = pos_y + (32 - pos_y % 32) - size[1]/2 - 1
			if collision_dir[1]:	#RIGHT Collision
				entity.position.x = pos_x + (32 - pos_x % 32) - size[0]/2
			elif collision_dir[3]:	#LEFT Collision
				entity.position.x = pos_x - pos_x % 32 + size[0]/2
		
		character_block_y = int(math.floor(self.character.position.y/32.0))
		character_chunk_y = int(math.floor(character_block_y/20.0))
		character_block_x = int(math.floor(self.character.position.x/32.0))
		character_chunk_x = int(math.floor(character_block_x/20.0))
		
		unload = []
		for i in range(-2,3):
			for j in range(-2,3):
				if i in [-1, 0, 1]:
					if j in [-1,0,1]:
						continue
					else:
						unload.append('%d_%d' % (character_chunk_x + i, character_chunk_y + j))
				else:
					unload.append('%d_%d' % (character_chunk_x + i, character_chunk_y + j))
		for chunk in unload:
			if chunk in self.map.chunks:
				if self.map.chunks[chunk].env_loaded and self.map.chunks[chunk].floor_loaded:
					self.map.chunks[chunk].unload()
	def handleKey(self, key_event):
		#print 'Handling key in GAME screen'
		# Check if the current player is moving/what direction
		if self.text_window.focus:
			self.text_window.handleKey(key_event)
			return
		else:
			if key_event.type == pygame.KEYDOWN:
				letter = key_event.unicode
				if len(letter) == 0:
					pass
				elif ord(letter) == 13:  # Enter
					self.text_window.focus = True
			if not self.character:
				return
			if self.character:
				direction = self.character.direction
				moving = 0
				keys = pygame.key.get_pressed()
				if keys[K_UP] and not keys[K_DOWN]:
					if keys[K_LEFT] and not keys[K_RIGHT]:
						direction = 7
					elif keys[K_RIGHT] and not keys[K_LEFT]:
						direction = 1
					else:
						direction = 0
					moving = 1
				elif keys[K_DOWN] and not keys[K_UP]:
					if keys[K_LEFT] and not keys[K_RIGHT]:
						direction = 5
					elif keys[K_RIGHT] and not keys[K_LEFT]:
						direction = 3
					else:
						direction = 4
					moving = 1
				elif keys[K_LEFT] and not keys[K_RIGHT]:
					direction = 6
					moving = 1
				elif keys[K_RIGHT] and not keys[K_LEFT]:
					direction = 2
					moving = 1
				direction = self.character.setDirection(direction) 
				moving = self.character.setMoving(moving)
				if direction or moving:
					self.queue_udp.append(self.character.get())
	def handleMouse(self, mouse_event):
		if mouse_event.type == MOUSEBUTTONUP:
			self.text_window.handleMouse(mouse_event)
		else:
			if self.text_window.handleMouse(mouse_event):
				return
	def handleMessageTCP(self, message):
#		print 'Gameplay handling:\t%s' % message
		
		self.text_window.handleMessageTCP(message)
		self.map.handleMessageTCP(message)
		message_type = message[0]
		message = message[1:].split()
		if message_type == 'c': #This client's character
			if self.character:
				self.character.position.x = float(message[1])
				self.character.position.y = float(message[2])
			else:
				self.character = Character(int(message[0]), Vector(float(message[1]), float(message[2])), int(message[3]), int(message[4]), int(message[5]), message[6], None, None, None)
				self.character.animations = texture_loader.getCharacterAnimations(self.character.name)
				self.entities.append(self.character)
		elif message_type == 'C': #This is other characters
			c = Character(int(message[0]), Vector(float(message[1]), float(message[2])), int(message[3]), int(message[4]), int(message[5]), message[6], None, None, None)
			c.animations = texture_loader.getCharacterAnimations(c.name)
			for entity in self.entities:
				if c.id == entity.id:
					self.entities.pop(self.entities.index(c))
					self.entities.append(c)
					return
			self.entities.append(c)
		elif message_type == 'D':
			for entity in self.entities:
				if int(message[0]) == entity.id:
					self.entities.pop(self.entities.index(entity))
	def handleMessageUDP(self, message):
#		print 'Handling:\t',message
		message_type = message[0]
		if message_type == 'E':
			if not self.character:
				return
			message = message[1:].split()
			for entity in self.entities:
				if int(message[0]) == self.character.id:
					s = ''
					return
				elif int(message[0]) == entity.id:
					entity.position.x = float(message[1])
					entity.position.y = float(message[2])
					entity.setDirection(int(message[3]))
					entity.setSpeed(int(message[4]))
					entity.setMoving(int(message[5]))
					return
#			print 'NEW ENTITY!'
			self.queue_tcp.append('A%s' % message[0])
	def getQueueTCP(self):
		q = self.queue_tcp
		self.queue_tcp = []
#		if self.character:
#			if not self.character.id:
#				q.append('R')
#		else:
#			q.append('R')
		for message in self.text_window.getQueueTCP():
			q.append(message)
		for message in self.map.getQueueTCP():
			q.append(message)
		return q
	def poll(self):
		if self.character:
			self.queue_udp.append(self.character.get())
	def setCharacter(self, character):
		if self.character in self.entities:
			self.entities.pop(self.entities.index(self.character))
		self.character = character
		self.entities.append(self.character)
	def reset(self):
		self.previous_time = time.time()

# ------------ Adventure ------------------------------------------------------------------------------- #
class Adventure:
	def __init__(self):
		self.screen = pygame.display.set_mode((800,600))
		pygame.display.set_caption('Pygame Window')
		pygame.font.init()
		self.font = pygame.font.SysFont('calibri', 24,False,False)
		self.login_client = LoginClient()
		self.fade = Fade(1.5,1.5,1.5,texture_loader.getCharacterAnimation('sam',3),True, True, [self.isReady], self.setState, [1])
		#self.fade = Fade(0.1,0.1,0.1,texture_loader.getCharacterAnimation('sam',3),True, True, [self.isReady], self.setState, [1])
		self.gameplay = Gameplay()
		self.states = ['LOGIN_REGISTER','GAMEPLAY', 'LOADING', 'QUIT']
		self.state = 0
		self.components = {}
		self.components['LOGIN_REGISTER'] = [self.login_client]
		self.components['LOADING'] = [self.fade]
		self.components['GAMEPLAY'] = [self.gameplay]
		for name, list in self.components.iteritems():
			for component in list:
				component.setAdventure(self)
		self.client_protocol_udp = None
		self.client_protocol_tcp = None
		self.username = None
		self.running = True
	def loop(self): #This is the game loop.
		if not self.running:
			return
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.close()
				return
			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
				for component in self.components[self.states[self.state]]:
					if component.isActive:
						component.handleKey(event)
			if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
				for component in self.components[self.states[self.state]]:
					if component.isActive:
						component.handleMouse(event)
#		self.screen.fill((70,150,70))
		self.screen.fill((0,0,0))
		for component in self.components[self.states[self.state]]:
			#print component
			component.update(0.033)
			if component.isVisible():
				component.draw(self.screen)
#		print repr(self.state), len(str(self.state))
#		self.screen.blit(self.font.render('state: %d' % self.state, 1, (255,255,255)), (10, 10))
#		self.screen.blit(self.font.render('username: %s' % str(self.username), 1, (255,255,255)), (10, 40))
		pygame.display.flip()
	def handleMessageTCP(self, message):
		for component in self.components[self.states[self.state]]:
			component.handleMessageTCP(message)
	def handleMessageUDP(self, message):
		if self.state == 1:
			self.gameplay.handleMessageUDP(message)
		pass
	def getQueueTCP(self):
		queue = []
		if self.state == self.states.index('QUIT'):
			queue.append('Q')
		else:
			for component in self.components[self.states[self.state]]:
				for message in component.getQueueTCP():
					queue.append(message)
		return queue
	def getQueueUDP(self):
		queue = []
		if self.state == self.states.index('GAMEPLAY'):
			for component in self.components[self.states[self.state]]:
				for message in component.getQueueUDP():
					queue.append(message)
		return queue
	def sendQueues(self):
		if self.client_protocol_tcp:
			for message in self.getQueueTCP():
#				print 'TCP Sending:\t%s' % message
				self.client_protocol_tcp.sendLine(message)
		if self.client_protocol_udp:
			for message in self.getQueueUDP():
				self.client_protocol_udp.sendLine(message)
	def setClientProtocolUDP(self, protocol):
		self.client_protocol_udp = protocol
	def setClientProtocolTCP(self, protocol):
		self.client_protocol_tcp = protocol
	def register(self):
		self.client_protocol_tcp.sendLine('U%d' % self.client_protocol_udp.host)
	def isReady(self):
		if self.state == 0:
			return True
		if self.state == 1:
			return True
		if self.state == 2:
			if self.gameplay.character:
				return True
			else:
				return False
	def setState(self, num):
#		print 'setting mode: %d' % num
		self.state = num
		if self.state == 1:
			self.gameplay.reset()
		if self.state == 2:
			self.fade.reset()
	def close(self):
		#import twisted
		#twisted.internet.reactor.stop()
		self.client_protocol_tcp.transport.loseConnection()
		pygame.quit()
		self.running = False
		
		

class Chunk:
	def __init__(self, location,byte_array_a = None,byte_array_b = None):
		self.location = location
		self.byte_array_a = byte_array_a
		self.byte_array_b = byte_array_b
#		print 'The size is:', len(byte_array_a)#, len(byte_array_b)
		self.floor = []
		self.environment = []
		self.floor_image = None
		self.rows = []
		self.floor_loaded = False
		self.env_loaded = False
		self.block_width = 32
		self.chunk_width = 0
		if self.byte_array_a:
			self.buildFloor()
		if self.byte_array_b:
			self.buildEnv()
		temp = self.location.split('_')
#		print 'The location is:',repr(self.location),temp[0], temp[1]
		temp = (int(temp[0]), int(temp[1]))
		self.x = temp[0] * 32 * self.chunk_width
		self.y = temp[1] * 32 * self.chunk_width
		if 1: #Temporary. the client should decide when to build floor and when to discard it.
			self.buildTexture()
	def buildFloor(self):
		self.chunk_width = int(len(self.byte_array_a) ** 0.5)
		for i in range(self.chunk_width):
			self.floor.append(self.byte_array_a[i*self.chunk_width:(i+1)*self.chunk_width])
	def buildEnv(self):
		size = int(len(self.byte_array_b) ** 0.5)
		for i in range(size):
			self.environment.append(self.byte_array_b[i*size:(i+1)*size])
	def buildTexture(self):
		#print self.floor
		if self.byte_array_a and not self.floor_loaded:
			self.floor_loaded = True
			self.floor_image = pygame.Surface((len(self.floor) * self.block_width, len(self.floor[0]) * self.block_width))
			for j in range(len(self.floor)):
				for i in range(len(self.floor[j])):
					self.floor_image.blit(texture_loader.getFloor(ord(self.floor[j][i])), (i * self.block_width, j * self.block_width))
		if self.byte_array_b and not self.env_loaded:
			self.env_loaded = True
			self.rows = []
			for i in range(len(self.environment)):
				count = 0
				for j in self.environment[i]:
					count += ord(j)
				if count == 0:
					row = pygame.surface.Surface((1,1), pygame.SRCALPHA)
					row.set_alpha(0)
					self.rows.append(row)
					continue
				row = pygame.Surface((32*20, 64), pygame.SRCALPHA)
				row.set_alpha(0)
				for j in range(len(self.environment[i])):
					#print 'getting:',ord(self.environment[i][j])
					row.blit(texture_loader.getEnvironment(ord(self.environment[i][j])), (32*j, 0))
				self.rows.append(row)
	def unload(self):
		self.env_loaded = False
		self.floor_loaded = False
		self.floor_image = None
		self.rows = []
	def getFloor(self):
		return 'f%s %s' % (self.location, self.byte_array_a)
	def setFloor(self, byte_array):
#		print 'length:',len(byte_array)
		self.byte_array_a = byte_array
		self.buildFloor()
		self.buildTexture()
	def getEnvironment(self):
		return 'f%s %s' % (self.location, self.byte_array_a)
	def setEnvironment(self, byte_array):
		self.byte_array_b = byte_array
#		print len(self.byte_array_b)
		self.buildEnv()
		self.buildTexture()
	def drawFloor(self, screen, character, offset):
		if self.floor_loaded:
			relative_position = (self.x - character.position.x + offset[0], self.y - character.position.y + offset[1])
			screen.blit(self.floor_image, relative_position)
		else:
			self.buildTexture()
	def drawRow(self, screen, character, offset, num):
		if self.env_loaded:
			relative_position = (self.x - character.position.x + offset[0], 32 * (num - 1) + self.y - character.position.y + offset[1])
			screen.blit(self.rows[num], relative_position)
		else:
			self.buildTexture()
class Map(Component):
	def __init__(self):
		Component.__init__(self)
		self.chunks = {}
		self.requested = {}
		self.floor_white_list = [0,1,2,4,5,6]
		self.environment_white_list = [0]
	def drawFloor(self, screen, character, offset, location):
		if location in self.chunks:
			self.chunks[location].drawFloor(screen, character, offset)
		elif not location in self.requested:
			self.requested[location] = True
			self.queue_tcp.append('M%s' % location)
	def drawRow(self, screen, character, offset, location, num):
		if location in self.chunks:
			self.chunks[location].drawRow(screen, character, offset, num)
		elif not location in self.requested:
			self.requested[location] = True
			self.queue_tcp.append('M%s' % location)
	def handleMessageTCP(self, message):
		message_type = message[0]
		if message_type == 'm':
#			print 'The message, short is:', repr(message[0:8])
			map_type = message[1]
			index = message.index(' ')
			location = message[2:index]
#			print 'The location by map is:', location
			byte_array = message[index + 1:]
			if location in self.chunks:
				if map_type == 'f':
					self.chunks[location].setFloor(byte_array)
				elif map_type == 'e':
					self.chunks[location].setEnvironment(byte_array)
			else:
				if map_type == 'f':
					self.chunks[location] = Chunk(location, byte_array, None)
				elif map_type == 'e':
					self.chunks[location] = Chunk(location, None, byte_array)
	def isSolidAt(self, location, position):
		if location in self.chunks:
			if self.chunks[location].floor and self.chunks[location].environment:
				floor = ord(self.chunks[location].floor[position[1]][position[0]])
				env = ord(self.chunks[location].environment[position[1]][position[0]])
				#print location, position, 'floor:', floor, 'envir:', env
				if floor in self.floor_white_list and env in self.environment_white_list:
					return False
		elif not location in self.requested:
			self.requested[location] = True
			self.queue_tcp.append('M%s' % location)
		return True					






