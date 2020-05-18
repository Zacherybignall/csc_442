# -*- coding: utf-8 -*-
###############################################################################
#Name: Linh Nguyen
#Assignment: XOR Crypto
#Pyython Ver: 3.7
###############################################################################

# import libraries for usage
# the cycle from itertools will help with cycling through the key
from itertools import cycle
from sys import stdin, stdout
# KET_PATH contains the name of the key file
KEY_PATH = 'key2'
# open the key file to read
with open(KEY_PATH, 'r') as f:
    # buffer read in as binary
    key_in = f.buffer.read()
    # convert the read in data to byte array
    key_arr = bytearray(key_in)
# the cipher text file will be read in from stdin
cipher_in = stdin.buffer.read()
# convert the content of ciphertext to byte array
cipher_arr = bytearray(cipher_in)
# initiate the decoded string
decoded = bytearray()
# carry out the xor process for each bit of the ciphertext and the key
for (x,y) in zip(cipher_arr, cycle(key_arr)):
    decoded.append(x^y)
# decode the message with into utf-8
message = decoded
# send the output to stdout
try:
    stdout.buffer.write(message)
# report TypeError
except TypeError:
    print("ERROR ENCODING")