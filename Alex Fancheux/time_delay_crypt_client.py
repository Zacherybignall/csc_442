####################
# Name: Alex Faucheux
# Language: Python 3
####################

import socket
from sys import stdout
from time import time


# Binary decoder algorithm from previous program
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


# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.102.67"
port = 33333

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096).decode()

# receives delays between each character
delays = []
while data.rstrip("\n") != "EOF":
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    delays.append(delta)
    if DEBUG:
        stdout.write(" {}\n".format(delta))
        stdout.flush()

# close the connection to the server
s.close()

binary_msg = ""
binary_msg2 = ""

# Builds binary msgs
for time in delays:
    if time < 0.15:
        binary_msg += "0"

    elif 0.15 <= time:
        binary_msg += "1"

# Prints overt msg without EOF at the end
print("\nMessage 8-bit: " + decode(binary_msg, 8)[:-4])
