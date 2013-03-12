#!/usr/bin/python

#Python Number guessing client for NULLify Lab
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

#Set up veriables needed to guess
high = 1000000000 #High bounds to guess
low = 0 #Low bounds to guess
failed = False #Set bool in case the number is not guessed
guessNum = 0 #Set number of guesses to 0
start = time.time() #Start timer to see how long it takes

#Start Guessing!
while 'CORRECT' not in resp: #Start loop untill we get a "CORRECT" responce
	guess = (high + low)/2 #Set guess to half way between High and Low bounds
	guessNum = guessNum + 1 #Increment number of guesses
	#Print the number of guesses and the value to send to the server
	print 'Guess Number '+str(guessNum)+': '+str(guess)
	sock.send(str(guess)+'\n') #Send the guess plus a newline char
	resp = sock.recv(1024) #Recive the responce from the server
	print 'Server Responce: '+resp #Print the responce
	if 'LOW' in resp: #If the server says "LOW"
		low = guess+1 #Raise low bound
	if 'HIGH' in resp: #If the server says "HIGH"
		high = guess-1 #Lower High bound
	if 'TOO MANY' in resp: #If the server says "TOO MANY"
		failed = True #Change failed bool to False
		break #Break from loop
#End of guessing

elapsed = (time.time() - start) #Calculate how long it took

if failed is True: #If the number was not guessed
    print 'Time till failure: '+str(elapsed) #Print how long it took to fail
else: #If the number was guessed
    print 'Time to guess: '+str(elapsed) #Print how long to took to win
sock.close() #Close the socket
