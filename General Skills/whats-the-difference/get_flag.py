#!/usr/bin/python3

with open("cattos.jpg","rb") as cattos:
	BUF = 2    
        
	cattos_bytes  = bytearray(cattos.read())
#  	 print(cattos.read())

with open("kitters.jpg","rb") as kitter:
	kitter_bytes = bytearray(kitter.read())



for index in range(0,len(kitter_bytes)):
	
	

	kitt = kitter_bytes[index]
	catt = cattos_bytes[index]

	

	if kitt != catt:
		
		print(str(chr(catt)),end='')


#for byte in bytes_read:
#	print(byte)



