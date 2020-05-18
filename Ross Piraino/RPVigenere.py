# Ross Piraino 3/29/2020
from sys import stdin, argv

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#letnum function returns number of a letter in the alphabet string
def letnum(letter):
    temp = 0
    while True:
        if temp >= (len(alphabet)): #stops if we have checked everything
            temp = -1
            break
        if (letter == alphabet[temp]): #stops to return the number if we found a match
            break
        temp += 1
    return temp

def encrypt(plaintext, key):
    ciphertext = "" #initialize answer
    i = 0
    key = key.replace(" ", "") #removes all spaces from the key
    elem = 0
    while elem < len(text):
        key += key[elem]
        elem += 1
    while True:
        keynum = letnum(key[i]) #calls letnum in order to find the place in the alphabet for the key 
        textnum = letnum(plaintext[i]) #same as above for the current text letter
        if textnum == -1: #simply adds the current symbol of the input if its not a letter
            ciphertext += text[i]
            plaintext = plaintext[:i] + plaintext[i+1:]
        else:
            if ((keynum % 26) + (textnum % 26)) > 25: #if we go over the alphabet, we keep the casing
                ciphertext += alphabet[textnum - (26 - (keynum % 26))]
                i += 1
            else: #wihtout going over alphabet limit we can just add the mod since casing wouldnt change
                ciphertext += alphabet[textnum + (keynum % 26)]
                i += 1
        if i >= len(text): #stops once we reach the end
            break
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = "" #initialize answer
    i = 0
    key = key.replace(" ", "") #removes all spaces from the key
    elem = 0
    while elem < len(text):
        key += key[elem]
        elem += 1
    while True:
        keynum = letnum(key[i]) #calls letnum in order to find the place in the alphabet for the key
        #print(keynum)
        textnum = letnum(ciphertext[i]) #same as above for the current text letter
        #print(textnum)
        if textnum == -1: #simply adds the current symbol of the input if its not a letter
            plaintext += ciphertext[i]
            ciphertext = ciphertext[:i] + ciphertext[i+1:]
        else:
            if ((textnum % 26) - (keynum % 26)) < 0: #if we go under the alphabet, we keep the casing
                plaintext += alphabet[(textnum + 26) - (keynum % 26)]
                i += 1
            else: #wihtout going over alphabet limit we can just subtract the mod since casing wouldnt change
                plaintext += alphabet[textnum - (keynum % 26)]
                i += 1
        if i >= len(ciphertext): #stops once we reach the end
            break
    return plaintext


#collects mode and key from command line arguments
mode = argv[1]
key = argv[2]

text = stdin.read().rstrip("\n") #input

if (mode == "-e"):
    ciphertext = encrypt(text, key)
    print(ciphertext)
elif (mode == "-d"):
    plaintext = decrypt(text, key)
    print(plaintext)
else:
    print("must use commend line argument -e or -d for encryption or decryption")
