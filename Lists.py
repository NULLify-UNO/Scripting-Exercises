'''
Created on Jan 23, 2013
Simple script that is used to demonstrate lists and sockets
@author: various authors
'''

import socket, sys

if __name__ == '__main__':
    portList = []
    portList.append(21)
    portList.append(80)
    portList.append(443)
    portList.append(25)
    portList.append(3389)    
    portList.append(5000)
    
    print portList
    portList.sort()
    print portList
    
    host = sys.argv[1]
    socket.setdefaulttimeout(2)
    
    s = socket.socket()
    for x in portList:
        try:
            print x
            s.connect((host,x))
            print "[+] Port open... closing connection"
            s.close()
        except:
            print "[-] Port Closed"
        
    pass