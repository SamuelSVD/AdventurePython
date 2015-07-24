#!/usr/bin/env python
import time
import os
import os.path
from misc import *

## Client state decides which part of the server handles a message
## Class to handle log-in and register.
class LoginServer:
	def __init__(self, adventure_server):
		self.adventure_server = adventure_server
		self.users = {}
		self.logged_in = {}
		self.folder_location = 'UserData'
		self.id_count = 0
		self.loadUsers()
	def loadUsers(self):
		file = open(self.folder_location + '/accounts.txt', 'r')
		list = file.read()
		file.close()
		list = list.split('\n')
		for line in list:
			if len(line) == 0:
				continue
			line = line.split()
			self.users[line[0]] = line[1]
			self.logged_in[line[0]] = False
	def login(self, username, password):
		print 'Attempted Login:\t%s\t%s' % (username, password)
		if self.users.has_key(username):
			if password == self.users[username]:
				if not self.logged_in[username]:
					self.logged_in[username] = True
					return 'l1%s' % username
				else:
					return 'l0Someone is already logged in under than account.'
			else:
				return 'l0Incorrect Username or Password'
		else:
			return 'l0Incorrect Username or Password'
	def register(self, username, password):
		for user, passwrd in self.users.iteritems():
			if username.lower() == user.lower():
				return 'r0Username already taken.'
		if len(username) < 6 or len(username) > 13:
			return 'r0Username invalid. (6 - 13 characters)'
		for char in username:
			char = ord(char)
			if char > 126 or char < 33:
				return 'r0Username invalid. Invalid characters used.'
		if len(password) < 6 or len(password) > 13:
			return 'r0Password invalid. (6 - 13 characters)'
		for char in password:
			char = ord(char)
			if char > 126 or char < 33:
				return 'r0Password invalid. Invalid characters used.'
		self.users[username] = password
		self.logged_in[username] = False
		print 'Registered:\t%s\t%s'% (username, password)
		file = open(self.folder_location + '/accounts.txt', 'a')
		file.write('\n%s %s' % (username, password))
		file.close()
		return 'r1Register Successful'
	def handleMessage(self, message, client):
		message_type = message[0]
		message = message[1:]
		print 'LoginServer handling message: %s %s' % (message_type,message)
		
		if message_type == 'R':
			message = message.split()
			username = message[0]
			password = message[1]
			response = self.register(username,password)
			print 'Seding response R:\t%s' % response
			client.sendTCP(response)
		elif message_type == 'L':
			message = message.split()
			username = message[0]
			password = message[1]
			response = self.login(username,password)
			print 'Seding response L:\t%s' % response
			client.sendTCP(response)
	def logOut(self, username):
		self.logged_in[username] = False
		self.adventure_server.message_server.broadcast('t<%s has left the game.>' % username)
## Class to handle messages
class MessageServer:
	def __init__(self, adventure_server):
		self.adventure_server = adventure_server
		self.clients = adventure_server.clients
		self.dest_folder = 'Messages/'
		self.logging = True
	def log(self, message):
		location = time.strftime('%b_%d_%Y.log', time.gmtime())
		file = open(self.dest_folder + location, 'a')
		file.write(time.strftime('%H:%M:%S\t') + message[1:] + '\n')
		file.close()
	def handleMessageTCP(self, message, client):
		message_type = message[0]
		if message_type == 'T':
			if message[1] == '/':
				message = message[2:].split()
				if message[0] == 'tp':
					try:
						client.character.position = Vector(float(message[1])*32, float(message[2])*32)
						print message[1], message[2]
						message = 'c' + client.character.getChar()[1:]
						client.sendTCP(message)
						return
					except:
						client.sendTCP('tInvalid use of command.')
						return
			message = 't%s: %s' % (client.username, message[1:])
			self.log(message[1:])
			for client in self.clients:
				client.sendTCP(message)
	def broadcast(self, message):
		for client in self.clients:
			client.sendTCP(message)
## Class to handle positions and entities.... the rest of the game
#  - this class handles mobs, and sends the map.
class GameplayServer:
	def __init__(self, adventure_server):
		self.adventure_server = adventure_server
		self.clients = adventure_server.clients
		self.entities = []
		self.folder_location = 'UserData'
		self.id_count = 0
		self.previous_time = time.time()
		self.map = Map(20)
	def handleMessageUDP(self, message):
		message_type = message[0]
		message = message[1:].split()
		if message_type == 'E':
			for entity in self.entities:
				if int(message[0]) == entity.id:
					entity.position.x = float(message[1])
					entity.position.y = float(message[2])
					entity.direction = int(message[3])
					entity.speed = int(message[4])
					entity.moving = int(message[5])
		pass
	def handleMessageTCP(self, message, client):
		if message[0] == 'A':
			id = int(message[1:])
			print 'Requesting the data of id %d' % id
			for entity in self.entities:
				#print 'checking:',entity.id, id, entity.id == id 
				if entity.id == id:
					if str(entity.__class__) == 'misc.Character':
						print 'Sending requested char of id: %d' % id
						client.sendTCP(entity.getChar())
		if message[0] == 'M':
			location = message[1:]
			if location in self.map.chunks:
				client.sendTCP(self.map.chunks[location].getFloor())
				client.sendTCP(self.map.chunks[location].getEnvironment())
		pass
	def update(self):
		delta = time.time() - self.previous_time
		self.previous_time = time.time()
		for entity in self.entities:
			entity.update(delta)
	def newID(self):
		self.id_count += 1
		return self.id_count
	def loadUserData(self, username):
		if username in os.listdir(self.folder_location):
			file = open(self.folder_location + '/' + username, 'r')
			data = file.read().split('\n')
			character = Character(self.newID(), Vector(float(data[0]),float(data[1])), int(data[2]), int(data[3]), 0,username, None, None, None)
			self.entities.append(character)
			return character
		else:
			character = Character(self.newID(), Vector(0,0), 4, 128, 0,username, None, None, None)
			self.entities.append(character)
			return character
	def saveUserData(self, character):
		print 'Saving: %s' % character.name
		s = ''
		s += '%0.0f\n' % character.position.x
		s += '%0.0f\n' % character.position.y
		s += '%d\n' % character.direction
		s += '%d' % character.speed
		file = open(self.folder_location + '/' + character.name, 'w')
		file.write(s)
		file.close()
## Class that contains the client's state.
class Client:
	def __init__(self, login_server, message_server, gameplay_server, clients):
		self.login_server = login_server
		self.message_server = message_server
		self.gameplay_server = gameplay_server
		self.clients = clients
		self.states = ['LOGIN_REGISTER', 'GAMEPLAY', 'QUIT']
		self.state = 0
		self.udp_host = None
		self.udp_port = None
		self.udp_protocol = None
		self.tcp_protocol = None
		self.queueTCP = []
		self.queueUDP = []
		self.character = Character(None, None, Vector(0,0), 0, 0, 0, None, None, None)
	def handleMessageUDP(self, message):
		if self.state == 1:
			self.gameplay_server.handleMessageUDP(message)
			for client in self.clients:
				if client != self:
					#print 'forwarding UDP' 
					client.sendUDP(message)
	def handleMessageTCP(self, message):
		if self.state == 0:
			self.login_server.handleMessage(message, self)
		elif self.state == 1:
			self.message_server.handleMessageTCP(message, self)
			self.gameplay_server.handleMessageTCP(message, self)
	def checkOutgoingMessage(self, message):
		message_type = message[0]
		if message_type == 'l':
			if message[1] == '1':
				self.username = message[2:]
				self.state = 1
				self.character = self.gameplay_server.loadUserData(self.username)
				self.sendTCP('c' + self.character.getChar()[1:])
	def sendTCP(self, message):
		if self.tcp_protocol:
			self.tcp_protocol.sendLine(message)
			if self.state == 0:
				self.checkOutgoingMessage(message)
		else:
			raise Exception('The server-side client does not have a TCP Protocol assigned')
	def sendUDP(self, message):
		if self.udp_protocol:
			self.udp_protocol.sendLine(message, (self.udp_host, self.udp_port))
		else:
			raise Exception('The server-side client does not have a UDP Protocol assigned')

class AdventureServer:
	def __init__(self):
		self.clients = []
		self.login_server = LoginServer(self)
		self.message_server = MessageServer(self)
		self.gameplay_server = GameplayServer(self)
		self.udp_protocol = None
	def addClient(self, tcp_protocol):
		client = Client(self.login_server, self.message_server, self.gameplay_server, self.clients)
		client.tcp_protocol = tcp_protocol
		client.udp_protocol = self.udp_protocol
		self.clients.append(client)
		return client
	def loop(self):
		self.gameplay_server.update()
	def handleMessageUDP(self, message, (host,port)):
		for client in self.clients:
			if host == client.udp_host and port == client.udp_port:
				client.handleMessageUDP(message)
				return
	def removeClient(self, client):
		if client in self.clients:
			self.clients.pop(self.clients.index(client))
			if client.state == 1:
				self.login_server.logOut(client.character.name)
				if client.character in self.gameplay_server.entities:
					self.gameplay_server.entities.pop(self.gameplay_server.entities.index(client.character))
					self.message_server.broadcast('D%d' % client.character.id)
					self.gameplay_server.saveUserData(client.character)