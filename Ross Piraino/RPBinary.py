from sys import stdin

def decode(binary, n):
    #initialize variables
    text = ""
    i = 0
    while (i<len(binary)):
        byte = binary[i:i+n] #converts every n digits into a binary number
        byte = int(byte, 2) #converts the binary number into an int
        if (byte == 8):
            text = text[:-1] #removes the last output entry if the character is backspace
        else:
            text += chr(byte) #adds the int as its ASCII character to the current output
        i += n #begins next run on the next segment of input
    return text

#read from stdin and remove the new line to clean up input
binary = stdin.read().rstrip("\n")

#if the length of input is evenly divisible by 7 or 8 we know its that bit
#but if its evenly divisble by both we output both
if (len(binary) % 7 == 0):
    text = decode(binary, 7)
    print("7-bit:")
    print(text)
if (len(binary) % 8 == 0):
    text = decode(binary, 8)
    print("8-bit:")
    print(text)
