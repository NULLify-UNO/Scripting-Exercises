#! /usr/bin/python

#####Basic use of sockets#####

from socket import *   #import the socket library

HOST = '127.0.0.1' #Host to connect to
PORT = 8675	#Port to connect to

sock = socket(AF_INET,SOCK_STREAM)	#Set a socket to a variable

sock.connect((HOST, PORT))	#Connect to the server

sock.send('Hello Server!')	#Send a string to the server

print sock.recv(1024)	#Recive information for the server

sock.close()	#Close connection IMPORTANT

