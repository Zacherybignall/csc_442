###################################################################################
#Name: Linh Nguyen
#Assignment: Vigenere Cypher Program
#Python Ver: 2.7.17
###################################################################################

# from the sys library import stdin and argv to read in arguments from the terminal
from sys import stdin, argv
# import sys to use the sys.exit() function later
import sys

# from the terminal, the program will check for the inputs for the right format
# in case there are too many inputs
if len(argv) > 3:
    # print the message on the terminal
    print "Too many arguments!"
    # and exit
    sys.exit()
# in case there are not enough inputs
elif len(argv) < 3:
    # print the message on the terminal
    print "Not enough arguments!"
    # and exit
    sys.exit()
else:
    # the right format will have 2 input,
    # the first one would be the mode, either '-e' or '-d'
    mode = argv[1]
    # check for the mode right away:
    # if it is neither -e or -d 
    if (mode != "-e") and (mode != "-d"):
        # print the error message
        print "Input mode not recognized, enter -e for encryption and -d for decryption"
        # and exit
        sys.exit()
    # the second one would be the key to use
    key = argv[2]

# the alphabet_list will be initiate as a global variable
global alphabet_list
# and it will start off as a string
alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0987654321.,?!+='":;@#$%*"""
# and then turn into a list using the list function
alphabet_list = list(alphabet)

# the function pos_extract is used to extract the numerical values from the character
# and return the key as a list
def pos_extract(key):
    # initiate the list of the keys
    shift_list = []

    # to find the numerical values, go through each character in the key
    for character in key:
        # in case the key contains special characters
        if not character in alphabet_list:
            # those characters will be ignored as the requirement doesn't include them
            pass
        # in case the character is a letter
        else:
            # the alphabet_list only contains uppercase letters
            # so all character when checked for index would have to be uppercase
            # append the numerical values into the shift_list in the order of them being checked
            shift_list.append(alphabet_list.index(character))
    # finally return the shift_list
    return shift_list

# the function encrypt is used to encrypt the input according to the provided key
def encrypt(text):
    # initiate the cypher text as an empty string
    # as the program figure out the new character it will simply add to this string
    cypher_text = ""
    # key_counter variable is used to traverse the numerical value of the key list
    key_counter = 0
    # to encrypt the given string, we'll have to go through each character in it
    for character in text:
        # for the case of special characters, the case value will be False
        # in case the character read in is a special character
        # the program won't do any encryptions on them and just simply add to the result string
        if not character.upper() in alphabet_list:
            cypher_text += character
        # in case the character read in is a letter
        else:
            # the case variable is used to check for uppercase and lowercase of each character
            case = character.isupper()
            # the program will find the position of the new encrypted character
            # to do this, it simply take the position of the current character
            # add the key value to it
            # and mod the sum with 26
            # this will update the encrypted character position
            new_pos = (alphabet_list.index(character.upper()) + shift_list[key_counter]) % 26
            # next the program will check for the current character being lowercase or uppercase
            if case == True:
                # in case of uppercase, it adds the new character straight from the alphabet_list
                cypher_text += alphabet_list[new_pos]
            elif case == False:
                # in case of lowercase, it'll obtain the new character from the alphabet_list 
                current = alphabet_list[new_pos]
                # and then add the lowercase version of it to the string
                cypher_text += current.lower()

            # after dealing with the character, it will then check for the key values
            # with the key_counter is still smaller than the length of the shift_list
            if key_counter < (len(shift_list)-1):
                # the key_counter increments itself by one to move to the next key
                key_counter += 1
            # in case the key_counter is equal to the length of the shift_list
            else:
                # the key_counter will be reset to 0 to traverse from the beginning again
                key_counter = 0
    # finally return the cypher_text after going through all characters
    return cypher_text

# the function decrypt is used to decrypt the input according to the given key
def decrypt(text):
    # the idea is similar to that of the encryption process
    # the only difference would be the math to find the new character
    # the same variables will be initiated
    plain_text = ""
    key_counter = 0
    for character in text:
        # the same rule applies for special characters so in case they are found
        if not character in alphabet_list:
            # they are simpy added to the result string
            plain_text += character
        else:
            # to find the new character position in this case
            # the program will proceed to find the difference between the current character being checked
            # and assign it to variable a
            a = alphabet_list.index(character) - shift_list[key_counter]
            # the case variable is still used to check for uppercase and lowercase
            # now the variable a will be checked for its sign
            # in case it is negative
            if a < 0:
                # the new position will be updated as a + 26
                # this is basically a wrap around of the alphabet_list to avoid out of index error
                new_pos = a + 78
            # in case it is positive, or still in index
            else:
                # it basically the position of the new character
                new_pos = a
            plain_text += alphabet_list[new_pos]
            # the same check is carried out for the key_counter
            if key_counter < (len(shift_list)-1):
                key_counter += 1
            else:
                key_counter = 0
    # finally return the result text
    return plain_text

# since the key is given at the beginning, the program will exact the shift_list from it right away
shift_list = pos_extract(key)

# initiate the loop to keep the program running
try:
    while True:
        # the input can be typed in directly and the program will give the new string as user presses Enter
        text = raw_input("")
        # the program will check for the mode input
        # if it reads '-e' then it will use the encrypt function on the input text
        if mode == "-e":
            result = encrypt(text)
        # if it reads '-d' then it will use the decrypt function on the input text
        elif mode == "-d":
            result = decrypt(text)
        # and print the result right away
        print result
# while executing there are 2 potential system errors that will be caught
# the first one is the KeyboardInterrupt (Ctrl+C) from the user to break out of the loop
# the second one is the EOF (End of File) error,
# obtained from input a text file straight from the command line using '<'
except (KeyboardInterrupt,EOFError):
    # the program will simply pass and exit
    pass
