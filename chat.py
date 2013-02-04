#! /usr/bin/python
from socket import *      #import the socket library

#Simple chat client, not even close to done
#Allows the user to chat with one client
#Can only send one message at a time

##let's set up some constants
HOST = ''    #we are the host
PORT = 56754    #arbitrary port not currently in use
ADDR = (HOST,PORT)    #we need a tuple for the address

serv = socket( AF_INET,SOCK_STREAM)    
 
##bind our socket to the address
serv.bind((ADDR))    #the double parens are to create a tuple with one element
serv.listen(5)    #5 is the maximum number of queued connections we'll allow
print 'listening...'
 
conn,addr = serv.accept() #accept the connection
print '...connected!'

conn.send('Chat!!!\nEnter name: ')
cname = conn.recv(1024)
cname = cname.rstrip('\n')

print cname+' has connected'
print 'Say something'
while True:
	message = raw_input('Message: ')
	conn.send('server: '+message+'\n')
	conn.send('message: ')
	print cname+': '+conn.recv(1024)
	if 'exit' in message:
		conn.close()
		break
