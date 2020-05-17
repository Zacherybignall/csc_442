################################################
# Name: Alex Faucheux
# Date: 3/29/2020
# Program: Binary Decoder. NOTE: Uses python 3!
################################################

from sys import stdin


# Binary decoder algorithm
def decode(b_string, n):
    text = ""
    # Iterates through the string every nth character
    # n is a variable that represents number of bits
    for i in range(0, len(b_string), n):
        # Converts the binary string of set # of bits into a ASCII decimal
        decimal = int(b_string[i:i + n], 2)

        # ASCII 8 is a backspace. Deletes the last character
        if decimal == 8:
            text = text[:-1]

        # If the symbol is not a backspace,
        # add the ascii character to the text
        else:
            text += chr(decimal)

    return text


if __name__ == "__main__":
    # Reads from standard input and strips the newline
    txt = stdin.read().rstrip("\n")

    # If the length of the binary string is divisible by 7,
    # it's a 7 bit string
    if len(txt) % 7 == 0:
        print("7-bit:\n", decode(txt, 7))

    # If the length of the binary string is divisible by 8,
    # it's an 8 bit string
    if len(txt) % 8 == 0:
        print("8-bit:\n", decode(txt, 8))
