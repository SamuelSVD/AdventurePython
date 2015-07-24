#!/usr/bin/env python
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from serverclasses import *
# ----- UDP --------------------------------------------------------- #
class ServerProtocolUDP(DatagramProtocol):
	def __init__(self, adventure):
		self.adventure = adventure
		adventure.udp_protocol = self
	def datagramReceived(self, data, (host, port)):
		#print 'Received UDP: %s' % data
		self.adventure.handleMessageUDP(data, (host, port))
	def sendLine(self, message, (host, port)):
		self.transport.write(message, (host, port))

# ----- TCP --------------------------------------------------------- #
class ServerProtocolTCP(LineReceiver):
	def __init__(self, factory, adventure_server, address):
		self.factory = factory
		self.adventure_server = adventure_server
		self.address = address
		self.client = self.adventure_server.addClient(self)
	def lineReceived(self, line):
		if line[0] == 'U':
			self.client.udp_host = self.address.host
			self.client.udp_port = int(line[1:])
		self.client.handleMessageTCP(line)
	def connectionLost(self, reason):
		self.adventure_server.removeClient(self.client)
		pass
class ServerFactoryTCP(Factory):
	def __init__(self, adventure_server):
		self. adventure_server = adventure_server
	def buildProtocol(self, addr):
		print 'connection made with %s' % addr
		return ServerProtocolTCP(self, self.adventure_server, addr)

def main():
	adventure_server = AdventureServer()
	udp = ServerProtocolUDP(adventure_server)
	
	game_loop = LoopingCall(adventure_server.loop)
	game_loop.start(0.033, now = False)
	
#	message_loop = LoopingCall(adventure_server.sendQueues)
#	message_loop.start(0.05, now = False)
	
	reactor.listenUDP(11110, udp)
	reactor.listenTCP(11110, ServerFactoryTCP(adventure_server))
	print 'Started server.'
	reactor.run()

if __name__ == '__main__':
	main()