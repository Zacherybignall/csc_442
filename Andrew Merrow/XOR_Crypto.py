##############################################################
#Andrew Merrow
#5/7/2020
#Python 2.7
#XOR Assignment
#This program reads a file then XORs it with another file
#named key in the current directory
##############################################################


import sys
from numpy import frombuffer,bitwise_xor,byte

DEBUG = False


#read the key from key file
with open("key","rb") as info:
	key = info.read()

#turn key into binary
key = key.rstrip('\n')
key = ''.join(format(ch, 'b') for ch in bytearray(key))
if(DEBUG):
	print("key after join: " + str(key))
	print("length: " + str(len(str(key))))


key = bin(int(key,2))
if(DEBUG):
	print ("key: " + str(key))
	print ("int key: " + str(int(key,2)))



#read plaintext/cyphertext from stdin
for line in sys.stdin:
	plain = line
plain = plain.rstrip('\n')

#turn plaintext/cypertext to binary
plain_bin = ''.join(format(ch, 'b') for ch in bytearray(plain))

if(DEBUG):
	print("plain after join: " + str(plain_bin))
	print("length: " + str(len(str(plain_bin))))

plain_bin = bin(int(plain_bin, 2))

if(DEBUG):
	print ("Pln: " + str(plain_bin))
	print("int Pln: " + str(int(plain_bin, 2)))


#XOR the key with the provided data
cipher = int(key,2) ^ int(plain_bin,2)
cipher = bin(cipher)

if(DEBUG):
	print("String key: " + str(key))
	print("String cipher: " + str(plain_bin))

#send result to stdout
print cipher

