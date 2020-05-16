#########################################################
#Andrew Merrow
#5/7/2020
#Steg assignment
#
#########################################################

from sys import stdin, argv, stdout

DEBUG = False


def bit_store(wrapper, hidden, offset, interval, sentinel):
	i = 0
	#print("wrapper: " + str(wrapper[offset]))
	while(i < len(hidden)):
		for j in range(0,7):
			#temps used to avoid assignment errors
			temp = wrapper[offset]
			temp2 = hidden[i]
			temp = "0b" + temp
			temp2 = "0b" + temp2
			temp = int(temp, 2)
			temp2 = int(temp2, 2)
			#print temp
			temp  &= 0b11111110
			temp |= ((temp2 & 0b10000000) >> 7)
			temp2  << 1
			wrapper[offset] = temp
		#	hidden[i] = temp2
			offset += interval
		i += 1
	
	i = 0
	while(i < len(sentinel)):
		for j in range(0,7):
			temp = wrapper[offset]
			temp2 = sentinel[i]
			temp = "0b" + temp
			temp = int(temp, 2)
			temp &= 11111110
			temp |= ((temp2 & 10000000) >> 7)
			temp2 <<= 1
			offset += interval
		i += 1

	#print("bit mode selected")

def bit_extract(wrapper, offset, interval, sentinel):
	hidden = []

	b = 0
	for j in range(0,7):
		temp = wrapper[offset]
		temp = "0b" + temp
		temp = int(temp, 2)
		b |= (temp & 0b00000001)
	#	print("b after &: " + str(b))
		if(j < 7):
			b = (b << 1) & (2**8 -1)
#			print("b after shift: " + str(b))
			offset += interval
	hidden.append(b)
	offset += interval
	stdout.write(str(hidden))

def byte_store(wrapper, hidden, offset, interval, sentinel):
	i = 0 
	while(i < len(hidden)):
		wrapper[offset] = hidden[i]
		offset += interval
		i += 1
	
	i = 0
	while(i < len(sentinel)):
		wrapper[offset] = sentinel[i]
		offset += interval
		i += 1

	print wrapper
	if(DEBUG):
		print("byte mode selected")

def byte_extract(wrapper, offset, interval, sentinel):
	hidden = []

	while(offset < len(wrapper)):
		b = wrapper[offset]
		hidden += b
		offset += interval
	stdout.write(str(hidden))

###############################main##############################
#default values initalized
sentinal = [0b00000000, 0b11111111, 0b00000000, 0b00000000, 0b11111111, 0b00000000]
if(DEBUG):
	print ("Sentinal binary: " + str(sentinal[1]))

offset = 0
interval = 1
hidden = ""
#read the command line arguments
for i in range(0, len(argv)):
	if(argv[i][0:2] == "-s" or argv[i][:2] == "-r"):
		operation = argv[i]

	if(argv[i][0:2] == "-b" or argv[i][:2] == "-B"):
                mode = argv[i]

	if(argv[i][0:2] == "-o"):
                offset = int(argv[i][2:])

	if(argv[i][0:2] == "-i"):
                interval = int(argv[i][2:])

	if(argv[i][0:2] == "-w"):
                wrapper  = argv[i][2:]

	if(argv[i][0:2] == "-h"):
                hidden = argv[i][2:]


if(DEBUG):
	print("Operation: " + str(operation))
	print("Mode: " + str(mode))
	print("Offset: " + str(offset))
	print("Interval: " + str(interval))
	print("Wrapper: " + str(wrapper))
	print("hidden: " + str(hidden))

#read the wrapper file
with open(wrapper, "rb") as info:
	wrapper = info.read()

#convert wrapper to binary data
wrapper = wrapper.rstrip('\n')
wrapper = ''.join(format(ch, 'b') for ch in bytearray(wrapper))
wrapper = bin(int(wrapper,2))
wrapper = wrapper[2:]

#convert to a list of bytes
chunks, chunck_size = len(wrapper), 8
wrapper = [wrapper[i:i+chunck_size] for i in range(0, chunks, chunck_size)]


#read hidden file if one is provided
if(hidden != ""):
	with open(hidden, "rb") as info:
		hidden = info.read()
	hidden = hidden.rstrip('\n')
	hidden = ''.join(format(ch, 'b') for ch in bytearray(hidden))
	hidden = hidden[2:]
	#convert to list of bytes
	chunks, chunk_size = len(hidden), 8
	hidden = [hidden[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

if(DEBUG):
	print("Wrapper read from file: " + str(wrapper))
	print("Hidden read from file: " + str(hidden))

#store operation selected
if(operation == "-s"):
	if(mode == "-b"):
		bit_store(wrapper, hidden, offset, interval, sentinal)
	if(mode == "-B"):
		byte_store(wrapper, hidden, offset, interval, sentinal)

#retrieve operation selected
if(operation == "-r"):
	if(mode == "-b"):
		bit_extract(wrapper, offset, interval, sentinal)
	if(mode == "-B"):
		byte_extract(wrapper, offset, interval, sentinal)








