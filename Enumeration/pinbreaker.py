import hashlib
import threading
import sys
import thread
from multiprocessing import Process
str = raw_input("please press key to start");
a = 0

class myThread (threading.Thread):
    def __init__(self, threadID, direction):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.direction = direction
    def run(self):
        print "Starting a thread"
        #print self.direction
        # Get lock to synchronize threads
        threadLock.acquire()
        startcounting(self.direction)
        # Free lock to release next thread
        threadLock.release()
        

    
def startcounting(direction):
	if direction == 1:
		a = 0
		print "up"
		for x in range(0, 5000000):
			b = "%07d" % (a,)			
			m = hashlib.md5()
			m.update(b)
			mh = m.hexdigest()
			s1 = hashlib.sha1()
			s1.update(b)
			s1h = s1.hexdigest()
			s2 = hashlib.sha256()
			s2.update(b)
			s2h = s2.hexdigest()
			if mh[30:] == "5a" and s1h[:2] == "f1" and s2h[30:-32] == "91":
				print "The correct pin is :"+b
				print "Opening the file..."
				target = open('manly.txt', 'w')
				target.write(b)
				target.close()
			a = a+1
	if direction == 0:
		a = 9999999
		print "down"
		for x in range(0, 5000000):
			b = "%07d" % (a,)
			#print "down: "+b
			m = hashlib.md5()
			m.update(b)
			mh = m.hexdigest()
			s1 = hashlib.sha1()
			s1.update(b)
			s1h = s1.hexdigest()
			s2 = hashlib.sha256()
			s2.update(b)
			s2h = s2.hexdigest()
			if mh[30:] == "5a" and s1h[:2] == "f1" and s2h[30:-32] == "91":
				print "The correct pin is :"+b
				print "Opening the file..."
				target = open('manly.txt', 'w')
				target.write(b)
				target.close() 
				sys.exit()
			a = a-1

if __name__ == '__main__':
    p1 = Process(target=startcounting, args=(0,))
    p1.start()
    p1.join()
    p2 = Process(target=startcounting, args=(1,))
    p2.start()
    p2.join()
	    
##print "I got to threads"	
#threadLock = threading.Lock()
#threads = []

## Create new threads
#thread1 = myThread(1, 0)
#thread2 = myThread(2, 1)

## Start new Threads
#thread1.start()
#thread2.start()

## Add threads to thread list
#threads.append(thread1)
#threads.append(thread2)

## Wait for all threads to complete
#for t in threads:
    #t.join()
#print "Exiting Main Thread"

