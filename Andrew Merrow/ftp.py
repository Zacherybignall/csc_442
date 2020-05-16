####################################################################
#Andrew Merrow
#FTP Covert Channel
#4/1/20
#Python 2.7
####################################################################



from ftplib import FTP

DEBUG = False

#set variables for connecting to FTP server
METHOD = 10
IP = "jeangourd.com"
PORT = 8008
FOLDER = ".secretstorage/.folder2/.howaboutonemore"	#name of folder you want to enter
USER = "valkyrie"
PASSWORD = "chooseroftheslain"

#decode function that takes a binary number, cuts it into 7 bit binary numbers and decodes it to ascii
def decode_7bit(number):
	message7 = list()
	bit_7 = list()
	final7 = ''

	# cut into 7 bit chunks
	bit_7 = [number[i:i+7] for i in range(0,len(number)-1,7)]

	# convert chunks into ascii
	for element in bit_7:
		x = int(element, 2)
		if(x == 8):
			message7.pop()
		else:
			y = chr(x)
			message7.append(y)
	# add each character to one string
	for letter in message7:
		final7 = final7 + letter
	print ("7 bit : " + final7)

#This function takes a binary number, cuts it into 8 bit binary numbers, then converts them to ascii
def decode_8bit(number):
	message8 = list()
	bit_8 = list()
	final8 = ''

	#cut into 8 bit chunks
	bit_8 = [number[i:i+8] for i in range(0,len(number)-1,8)]

	#convert chunks into ascii
	for element in bit_8:
		x = int(element, 2)
		y = chr(x)
		message8.append(y)

	# put all characters into one string
	for letter in message8:
		final8 = final8 + letter
	print ("8 bit: " + final8)

#variable for holding contents retrieved from ftp server
contents = []

ftp = FTP()
ftp.connect(IP, PORT) 		#choose which IP and port to connect to
ftp.login(USER,PASSWORD)			#anonynous login
ftp.cwd(FOLDER)			#navigate to folder
ftp.dir(contents.append)	# add data to contents
ftp.quit()			# end connection

########################main#############################################

# If method is 7, read the contents received from the ftp server, cut off the first three items
# then keep the next 7 elements (the permissions). Those 7 elements will be converted to a 7 bit
# binary number to be decoded
#print ("Check: " + str(contents))
code = ""
if (METHOD == 7):
	for i in range(0,len(contents)):
		code = code + contents[i][3:10]
	
	if(DEBUG):
		print code

#If method is 10, convert all the permissions to a binary number
if (METHOD == 10):
	for i in range(0,len(contents)):
		code = code + contents[i][:10]
	if(DEBUG):
		print code

# read the permissions, turn each - to a 0 and each letter to a 1
binary = ""
for letter in code:
	if (letter == '-'):
		binary = binary + "0"
	else:
		binary = binary + "1"
if(DEBUG):
	print binary

# decode and print message
if(METHOD == 10):
	decode_8bit(binary)
	decode_7bit(binary)
if(METHOD == 7):
	decode_7bit(binary)



