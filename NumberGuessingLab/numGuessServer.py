#Sever Application that generates a random number for each session
#for the user to guess

from twisted.internet import protocol, reactor
import random

class Echo(protocol.Protocol):
    def __init__(self, data):
        self.number = random.randint(0, 1000000000)
        print 'The number is '+str(self.number)


    def dataReceived(self, data):
        print 'The guess is '+data
        guess = data
        if int(guess) == self.number:
            print 'Correct'
            self.transport.write('   You are CORRECT!\n')
            self.transport.write("         .:.\n       _oOoOo\n      [_|||||\n        |||||\n        ~~~~~\n")
            self.transport.write('    Have a drink!\n\n')
        if int(guess) < self.number:
            self.transport.write('TOO LOW!\n')
        if int(guess) > self.number:
            self.transport.write('TOO HIGH!\n')

class EchoFactory(protocol.Factory):
    def __init__(self):
        self.number = 0

    def buildProtocol(self, addr):      
        return Echo(self.number)

reactor.listenTCP(8675, EchoFactory())
reactor.run()