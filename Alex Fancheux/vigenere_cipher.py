#################################################
# Name: Alex Faucheux
# Date: 3/29/2020
# Program: Vigenere Cipher. NOTE: Uses python 3!
#################################################


from string import ascii_uppercase
import sys


# The Vigenere Cipher algorithm
# Encrypts if com == "-e" or decrypts if com == "-d"
def cipher(string, key, com):
    text = ""
    key_index = 0
    for msg_char in string:
        # Skips spaces in key.  Index resets to 0 if at end of string
        while key[key_index] == " ":
            key_index += 1
            if key_index == len(key):
                key_index = 0

        key_char = key[key_index]

        # Exception handling for incorrect characters
        if key_char.upper() not in ascii_uppercase:
            print("Invalid character in key:", key_char, end="")
            exit(0)

        # Retains symbols outside of alphabet
        if msg_char.upper() not in ascii_uppercase:
            text += msg_char
            continue

        key_int = ascii_uppercase.index(key_char.upper())
        msg_int = ascii_uppercase.index(msg_char.upper())

        # cipher_num is set to a number according to the command to encrypt or decrypt
        cipher_num = (msg_int + key_int) % 26 if com == '-e' else (26 + msg_int - key_int) % 26
        cipher_char = ascii_uppercase[cipher_num]

        # character of correct case is concatenated to text
        text += cipher_char if msg_char.isupper() else cipher_char.lower()

        # Increments if index < len(key)-1, otherwise resets to 0
        key_index = key_index + 1 if key_index < len(key) - 1 else 0

    return text


if __name__ == "__main__":
    # Validates correct number of arguments
    if len(sys.argv) >= 3:
        command = sys.argv[1]
        key = sys.argv[2]

        # Validates key and command input
        if key != " " and (command == '-e' or command == '-d'):
            message = sys.stdin.readline()
            while message != "":  # exits loop when CTRL-D is entered
                print(cipher(message.rstrip("\n"), key, command))
                message = sys.stdin.readline()

        else:
            print("Incorrect argument(s)")
    else:
        print("Incorrect # of arguments")
