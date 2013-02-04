import threading
import datetime

#Basic example of threads
#Use as refence to make chat.py much better :)       

class ThreadClass(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print "%s says Hello World at time: %s" %(self.getName(), now)
        
for i in range(10):
	t = ThreadClass()
	t.start()