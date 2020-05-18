#Ross Piraino 5/8/2020
#made for python 3
from sys import stdin

#sets key to be whats in the key file
keyfile = open("key")
key = keyfile.read()

#saves input
plaintext = stdin.read().rstrip("\n")

#intialize output
output = ""

#repeats for each letter in plaintext
for i in range(len(plaintext)):
    currentinput = plaintext[i]
    #loops key if its shorter than input
    currentkey = key[i%len(key)]
    #XORs the character from input with character from key
    output += chr(ord(currentinput) ^ ord(currentkey))

print(output)
