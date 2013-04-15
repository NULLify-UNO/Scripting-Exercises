#Sever Application that generates a random number for each session
#for the user to guess

from twisted.internet import protocol, reactor
import random

class Echo(protocol.Protocol):
	passlist =[]
	def __init__(self, data):
		self.start = 0
		self.passlist = []
		ins=open('hash.txt','r')
		for line in ins:
			self.passlist.append( line )
		ins.close()
		self.num1=random.randint(0,20)
		self.num2=random.randint(0,20)
		if self.num2 == self.num1:
			self.num2=random.randint(0,20)
	def connectionMade(self):
		self.transport.write('\nhash1: '+self.passlist[self.num1]+'\n')
		self.transport.write('hash2: '+self.passlist[self.num2]+'\n')
		self.transport.write('INPUT HERE 1 or 2: \n')
		
	def putout(self, found):
		self.transport.write('Correct\n')
		self.start += 1
		self.transport.write('you have this many right: '+str(self.start)+'\n')
		self.num1=random.randint(0,20)
		self.num2=random.randint(0,20)
		self.transport.write('\nhash1: '+self.passlist[self.num1]+'\n')
		self.transport.write('hash2: '+self.passlist[self.num2]+'\n')
		self.transport.write('INPUT HERE 1 or 2: ')

	def dataReceived(self, data):
		self.transport.write('The you guessed is '+ data)
		guess = data #expect 1 or 2
		if int(guess) != 2 and int(guess) != 1:
			self.transport.loseConnection()
		if self.num2 <= self.num1:
			thing = 2
		else:
			thing = 1
		client = self.transport.getPeer()
		print "jerk: ",
		print client,
		print " has "+str(self.start)+" Correct just said ",
		print guess
		if int(guess) == int(thing):
			self.putout(data)
		else:
			self.transport.write('wrong bye bye now...')
			self.transport.loseConnection()
			
		if self.start >= 20:
			print "Someone Got the easy one!"
			self.transport.write("Good Job now try the next one called \"Meh\"")


class EchoFactory(protocol.Factory):
    def __init__(self):
        self.number = 0
        self.start = 0
        self.passlist = []
        self.num1=0
        self.num2=0
    def buildProtocol(self, addr):
        return Echo(self.number)

reactor.listenTCP(8671, EchoFactory())
reactor.run()
