######################################################
# Andrew Merrow
# 4/20/20
# Covert Timing, Client
# Python 2.7
######################################################



import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False
ONE = 0.2
ZERO = 0.1

# set the server's IP address and port
ip = "138.47.99.163"
port = 12321

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
covert_bin = ""
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()
	#ignore .15
	if .146 <= delta < .152:
                continue;
                
	if (delta >= ONE):
		covert_bin += "1"
	else:
		covert_bin += "0"

covert = ""
i = 0
#counter used watch for EOF to signal the end
counter = 0
while(i < len(covert_bin)):
	b = covert_bin[i:i + 8]

	n = int("0b{}".format(b),2)
	try:
		#if the letter is E, O, or F, counter is incremented
		letter = unhexlify("{0:x}".format(n))
		if (letter == "E" or letter == "O" or letter == "F"):
			counter += 1
		#if the letter is none of those characters, we reset the timer
		else:
			counter = 0
		#if counter reaches 3, we know we have received EOF, so we can stop converting
		if (counter == 3):
			break
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	i += 8
# close the connection to the server
#print the contents of covert, but chop off the last 2 characters because they will be "E" and "O"
print ("Secret message: " + covert[:len(covert)-2])
s.close()

