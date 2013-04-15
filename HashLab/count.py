import hashlib
ter=open('hash.txt','w')
for i in range(0,1000): 
	y = hashlib.md5()
	y.update(str(i)+"Example")
	i+=1
	ter.write(y.hexdigest() +'\n')
ter.close()
