import threading
from socket import *
        
class ThreadClass(threading.Thread):
    def run(self):
    	while True:
        	print cname+': '+conn.recv(1024),
       
HOST = ''
PORT = input('Enter port to use: ')
ADDR = (HOST,PORT)
sname = raw_input('Enter Your Name: ')
serv = socket( AF_INET,SOCK_STREAM)

serv.bind((ADDR))
serv.listen(5)
print 'Listening...'

conn,addr = serv.accept()
print 'Connection from '+str(addr[0])

conn.send('Chat!!!\nEnter Your Name: ')
cname = conn.recv(1024)
cname = cname.rstrip('\n')
conn.send('You are now chatting with '+sname+'\n')

print cname+' has connected!'

t = ThreadClass()
t.start()

while True:
	message = raw_input()
	conn.send(sname+': '+message+'\n')
	if 'exit' in message:
		conn.close()
		break