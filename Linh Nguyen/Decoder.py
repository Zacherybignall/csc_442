##########################################################
#Name: Linh Nguyen
#Assignment: Binary Decoder
#Python Ver: 2.7.17
##########################################################

# importing stdin from sys in order to read in the input file from terminal
from sys import stdin

# the decode function will read in the binary values and return the message
def decode(binary, n):
        # initiate the decoded message as an empty string
        text = ""
        # initiate the bit counter
        i = 0
        # the decode function will token the binary values up
        # according to what version they are translated in 7-bit or 8-bit
        # the number of bit will be n, which was given in the beginning
        while (i < len(binary)):
            # the byte variable will read in the binary value
            # from position ith to (i+n)th
            byte = binary[i:i+n]
            # and then translate it into base 2
            byte = int(byte, 2)
            # in case the backspace character is read in
            # which would be equal to 8 in base 2
            if byte == 8:
                # then the text string will remove the last character from itself
                text = text[:-1]
            # in case other character is read in    
            else:
                # the text string will add the characterized byte into itself    
                text += chr(byte)
            # finally, increment i by n so it can move to the next set of binary values    
            i += n
        # when i is equal to the length of the input file
        # return the translated text
        return text

# read in the binary values from the text file in and strip the Enter character
binary = stdin.read().rstrip('\n')

# this if statement is to check if the binary input is in 7-bit
if (len(binary) % 7 == 0):
        text = decode(binary, 7)
        # declare the version
        print "7-bit:"
        # and print the result
        print text

# this if statement is to check if the binary input is in 8-bit
if (len(binary) % 8 == 0):
        text = decode(binary, 8)
        # decalre the verion
        print "8-bit:"
        # and print the result
        print text

