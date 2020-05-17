#############################################
#Andrew Merrow
#Binary decoder
#3/29/20
#Python 2.7
#############################################
import sys

#variables are created for 7 and 8 bit decoding
bit_7 = list()
bit_8 = list()
message7 = list()
message8 = list()
final7 = ''
final8 = ''

for line in sys.stdin:
	#line is read and slip into 7 and 8 bit chunks
	line.rstrip()
	bit_8  = [line[i:i+8] for i in range(0,len(line)-1,8)]
	bit_7 = [line[i:i+7] for i in range(0,len(line)-1,7)]
	
	#each chunk is turned into a decimal number, then into an ascii character
	for element in bit_8:
		x = int(element,2)
		y =  chr(x)
		message8.append(y)
	for element in bit_7:
		x = int(element,2)
		if(x == 8):
			message7.pop()
		else:
			y = chr(x)
			message7.append(y)

	#the lists are put into a single string
	for letter in message8:
		final8 = final8 + letter
	for letter in message7:
		final7 = final7 + letter
	
	#the final message is printed
	length = len(line) - 1
	if (length%8==0):
		print("8 bit: " + final8)
	else:
		print("7 bit: " + final7)
