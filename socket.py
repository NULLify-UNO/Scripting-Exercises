#! /usr/bin/python

#####Basic use of sockets#####

from socket import *   #import the socket library

HOST = '127.0.0.1' #Host to connect to
PORT = '86753'	#Port to connect to

sock = socket(AF_INET,SOCK_STREAM)	#Set a socket to a variable

conn = sock.connect((HOST, PORT))	#Connect to the server and set connection to a variable

conn.send('Hello Server!')	#Send a string to the server

print conn.recv(1024)	#Recive information for the server

conn.close()	#Close connection IMPORTANT

