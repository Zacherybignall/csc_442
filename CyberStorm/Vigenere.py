##################################################
#Andrew Merrow
#Vigenere Cipher
#3/29/20
#Python 2.7
##################################################


from sys import stdin, argv

#function for encrypting data
def encrypt(plaintext, key):
	#upper flag used to track if the letter is uppercase or not
	UPPER = True
	ciphertext = ""
	for i in range(0,len(plaintext)):
		#test for upper or lowercase, then convert to A = 0
		#if the letter is < 65, it is a space, exclamation mark, etc.
		if(ord(plaintext[i]) < 65):
			ciphertext = ciphertext + plaintext[i]
			continue

		#lowercase	(lowercase a = 97 in ascii, so convert to a = 0)
		if(ord(plaintext[i]) > 90):
			Pi = ord(plaintext[i]) - 97 
			UPPER = False
		#uppercase	(uppercase A = 65 in ascii)
		else:
			Pi = ord(plaintext[i]) - 65
			UPPER = True

		#make key's index wrap around so its not out of range
		j = i
		#if the index is out of range, go back to the start of key
		if (j>len(key)-1):
			while(j>len(key)-1):
				j = j - len(key)
		#convert upper and lowercase for the key
		if (ord(key[j]) > 90):
			Ki = ord(key[j]) - 97
		else:
			Ki = ord(key[j]) - 65
		
		
		#here we convert the number we get back to a letter
		if(UPPER == True):
			new = chr(((Pi+Ki)%26)+65)
		else:
			new = chr(((Pi+Ki)%26)+97)

		#add leter to the text
		ciphertext = ciphertext + new
	
	return ciphertext

def decrypt(ciphertext, key):
	#upper keeps track of what case the letter is
	UPPER = True
	plaintext = ""
	for i in range(0,len(ciphertext)):
		#not a letter
		if(ord(ciphertext[i]) < 65):
			plaintext = plaintext + ciphertext[i]
			continue
		#lowercase
		elif(ord(ciphertext[i]) > 90):
			Ci = ord(ciphertext[i]) - 97
			UPPER = False
		#uppercase
		else:
			Ci = ord(ciphertext[i]) - 65
			UPPER = True

		 #make key's index wrap around so its not out of range
                j = i
                if (j>len(key)-1):
                        while(j>len(key)-1):
                                j = j - len(key)
                #
		#convert the number back to its ascii value, based on its case
                if (ord(key[j]) > 90):
                        Ki = ord(key[j]) - 97
                else:
                        Ki = ord(key[j]) - 65
		
		#convert ascii to a letter
                if(UPPER == True):
                        new = chr(((26+Ci-Ki)%26)+65)
                else:
                        new = chr(((26+Ci-Ki)%26)+97)
		
		#add letter to text
		plaintext = plaintext + new
	return plaintext

######################################################################

#retrieve mode and key from stdin
mode = argv[1]
key = argv[2]
text = stdin.read().rstrip("\n")

#create a list of all the lines entered
text_list = text.split("\n")


cipher = ""
plain = ""

#encode mode
if (mode == "-e"):
	#encode each item in the list and print them on a new line
	for thing in text_list:
		cipher = cipher + encrypt(thing, key) + "\n"
	print cipher

#decode mode
elif (mode == "-d"):
	#decode each item in the list and print them on a new line
	for thing in text_list:
		plain  = plain + decrypt(thing, key) + "\n"
	print plain
