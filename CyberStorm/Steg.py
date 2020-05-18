# -*- coding: utf-8 -*-
###############################################################################
#Name: Linh Nguyen
#Assignment: Steg
#Python Ver: 3.7
###############################################################################

# import libraries usage
import os
from sys import stdout, argv

# read in from command line
commands = list(argv)
# delete the first item in the command line
del commands[0]
# create the SENTINEL
global SENTINEL
# it will contain 00 ff 00 00 ff 00 in hex
SENTINEL = bytearray.fromhex('00 ff 00 00 ff 00')
  
# extract functino take in the command list and extract
def extract(commands):
    # initiates variables for read ins
    FUNC = ""
    MODE = ""
    WRAPPER_FILE = ""
    HIDDEN_FILE = ""
    # offset default value is set to 0
    OFFSET = 0
    # interval default value is set to 1
    INTERVAL = 1
    # check for attributes in command line
    for c in commands:
        if c[0:2] == '-s':
            FUNC = 'store'
        elif c[0:2] == '-r':
            FUNC = 'retrieve'
        elif c[0:2] == '-b':
            MODE = 'bit'
        elif c[0:2] == '-B':
            MODE = 'byte'
        elif c[0:2] == '-o':
            # check for input offset value
            if c[2:].isnumeric():
                # if it's all numeric, convert it into int
                OFFSET = int(c[2:])
            # if it's not then report error
            else:
                print("OFFSET VALUE IS INVALID, USING DEFAULT")
                
        elif c[0:2] == '-i':
            # check for input interval value
            if c[2:].isnumeric():
                # if it's all numveric, convert it into int
                INTERVAL = int(c[2:])
            # if it's not then report error
            else:
                print("INTERVAL VALUE IS INVALID, USING DEFAULT")
                
        elif c[0:2] == '-w':
            WRAPPER_FILE = c[2:]
        elif c[0:2] == '-h':
            HIDDEN_FILE = c[2:]
        # in case the command is not found
        else:
            # print out the error message
            print("COMMAND NOT FOUND: {}".format(c))
    
    # in case the function wasn't specified
    if FUNC == "":
        print("FUNCTION NOT FOUND (either -s or -r)")
    # in case the mode wasn't specified
    if MODE == "":
        print("MODE NOT FOUND (either -b or -B)")
    # wrapper file is required for any mode so check for it
    if WRAPPER_FILE == "":
        print("NO WRAPPER FILE INPUT")
    # in case there is wrapper file input
    if WRAPPER_FILE != "":
        # check for its availability
        if os.path.exists(WRAPPER_FILE):
            pass
        # if it doesn't exist then report
        else:
            print("WRAPPER FILE NOT FOUND")
    # with store function, both wrapper file and hidden file
    if FUNC == "store":
        # in case the hidden file is not input
        if HIDDEN_FILE == "":
            # report the error
            print("NO HIDDEN FILE INPUT")
        # in case the hidden file is input
        else:
            # check for its availability
            if os.path.exists(HIDDEN_FILE):
                pass
            # if it doesn't exist
            else:
                # report the error
                print("HIDDEN FILE NOT FOUND")
    # if function is retrieve the hidden file is not required
    if FUNC == 'retrieve' and HIDDEN_FILE != "":
        # report the error
        print("NO HIDDEN FILE ON RETRIEVE MODE")
    # return all the variables
    return FUNC, MODE, WRAPPER_FILE, HIDDEN_FILE, OFFSET, INTERVAL

# readin function read in file as bytearray
def readin(filepath):
    with open(filepath, 'r') as f:
        # buffer read in
        content = f.buffer.read()
        # and then convert it into bytearray
        content_arr = bytearray(content)
    # then return the bytearray
    return content_arr

# check function check for the size of the hidden and wrapper files for validity
def check(MODE, INTERVAL, OFFSET, HIDDEN_FILE, WRAPPER_SIZE):
    # get the size of the hidden file
    hidden_size = os.stat(HIDDEN_FILE).st_size
    # get the size of the wrapper file
    wrapper_size = os.stat(WRAPPER_SIZE).st_size
    # get the size of the sentinel
    sentinel_size = len(SENTINEL)
    # in case the mode is bit
    if MODE == 'bit':
        # the interval will be multiplied by 8
        INTERVAL = INTERVAL * 8
        # the same goes for sentinel size
        sentinel_size = sentinel_size * 8
    # calculate the check value
    check_value = (hidden_size*INTERVAL) + OFFSET + sentinel_size
    # if the wrapper size is greater than the check value
    if (wrapper_size >= check_value):
        # if it does, return True
        return True
    else:
        # if it doesn't, return False
        return False
    
# storage_byte function carry out the store function in byte mode
def storage_byte(INTERVAL, OFFSET, hidden_arr, wrapper_arr):
    # initiate variables for the bytearrays
    W = wrapper_arr
    H = hidden_arr
    # initiate i at 0
    i = 0
    # while there's still byte in the hidden file to go through
    while i < len(H):
        # replace the according byte in the wrapper with hidden
        W[OFFSET] = H[i]
        # and then increase the offset with the interval
        OFFSET += INTERVAL
        # at the same time increase the i by 1
        i += 1
    # reset the i to 0
    i = 0
    #the process is similar to that of the hidden file
    # except for this time is for the SENTINEL
    while i < len(SENTINEL):
        W[OFFSET] = SENTINEL[i]
        OFFSET += INTERVAL
        i += 1
    # return the new bytearray of the wrapper
    return W

# check_byte function 
def check_byte(INTERVAL, OFFSET, wrapper_arr):
    W = wrapper_arr
    check_arr = bytearray.fromhex('00')
    while (check_arr in SENTINEL) and (check_arr != SENTINEL):
        check_arr.append(W[OFFSET + INTERVAL])
    if check_arr == SENTINEL:
        return True
    else:
        return False
    
# extraction_byte function extracts the hidden byte from a wrapper file
def extraction_byte(INTERVAL, OFFSET, wrapper_arr):
    # initiates variables that store the bytearray from the wrapper file
    W = wrapper_arr
    # and then initiate a variable to store the bytearray of the hidden file
    H = bytearray()
    # create a check varialbe
    check = False
    # while there are still bytes to go through
    # and the sentinel hasn't been found yet
    while OFFSET < len(W) and check == False:
        # give the byte at offset position to b
        b = W[OFFSET]
        # and then append it to bytearray H
        H.append(b)
        # and then increase the OFFSET with the INTERVAL
        OFFSET += INTERVAL
        # check for the SENTINEL L in the HIDDEN bytearray when H is longer than 6
        if len(H) >= 6:
            # if the last 6 byte of the array matches the SENTINEL
            if H[-6:] == SENTINEL:
                # remove them
                H = H[:-6]
                # and change the check value to True to break out of the loop
                check = True
    # finaly, return the H bytearray
    return H

# storage_bit functiion carry out the store function in bit mode
def storage_bit(INTERVAL, OFFSET, hidden_arr, wrapper_arr):
    # initiate the variables for the bytearrays
    W = wrapper_arr
    H = hidden_arr
    # then initiate i at 0
    i = 0
    # while there are still byte in the hidden bytearray
    while i < len(H):
        # cycle through the 7 bits of that byte
        for j in range(7):
            # carry out the AND operation with 254
            W[OFFSET] & 254
            # and the OR operation
            W[OFFSET] | ((H[i] & 64) >> 7)
            # shift the byte of the hidden file one time to the left
            H[i] = (H[i] << 1) & (2**8 - 1)
            # then increase the OFFSET by the INTERVAL
            OFFSET += INTERVAL
        # when done with that byte, increase the i by 1 to move to the next byte
        i += 1
    
    # then reset the i to 0
    i = 0
    # do the same thing as above but with SENTINEL
    while i < len(SENTINEL):
        for j in range(7):
            W[OFFSET] & 254
            W[OFFSET] | ((SENTINEL[i] & 64) >> 7)
            SENTINEL[i] = (SENTINEL[i] << 1) & (2**8 - 1)
            OFFSET += INTERVAL
        i += 1
    
    #return the new bytearray of the wrapper 
    return W

# extraction_bit function extracts the bytes of the hidden file from the wrapper file in bit mode
def extraction_bit(INTERVAL, OFFSET, wrapper_arr):
    # initiate the W for the wrapper bytearray
    W = wrapper_arr
    # initiate a bytearray for the hidden file bytearray
    H = bytearray()
    # create the check variable and set it to False
    check = False
    # while there are still byte to go through in the wrapper bytearray
    # and the check value is still False
    while OFFSET < len(W) and check == False:
        # initiate b and set it to 0
        b = 0
        # cycle through the byte
        for j in range(8):
            # carry out the OR operation 
            b = b | (W[OFFSET] & 1)
            # if j is difference from 7
            # that means the byte is not done being cycled through yet
            if j != 7:
                # then shift it one bit to the left
                b = (b << 1) & (2**8 - 1)
            # then increase the OFFSET with the INTERVAL
            OFFSET += INTERVAL
        # then append the byte to the hidden file bytearray
        H.append((b))
        # check for the SENTINEL pattern when the length is greater than 6
        if len(H) > 6:
            # if the pattern is found
            if H[-6:] == SENTINEL:
                # change the check value to True
                check = True
                # and remove the last 6 byte from the hidden byteaary
                H = H[:-6]
    # then return the hidden bytearray
    return H

# create a variable for DEBUGGIN
DEBUG = False
# get the necessary variable from the extract function
FUNC, MODE, WRAPPER_FILE, HIDDEN_FILE, OFFSET, INTERVAL = extract(commands)

# if DEBUG mode is toggled on, print out the information
if DEBUG == True:
    print("Function: {}".format(FUNC))
    print("Mode: {}".format(MODE))
    print("Offset: {} {}".format(OFFSET, type(OFFSET)))
    print("Interval: {} {}".format(INTERVAL, type(INTERVAL)))
    print("Wrapper file: {}".format(WRAPPER_FILE))
    print("Hidden file: {}".format(HIDDEN_FILE))

# if the store function is called
if FUNC == "store":
    # first check for the file sizes compatibility
    check = check(MODE, INTERVAL, OFFSET, HIDDEN_FILE, WRAPPER_FILE)
    # with the check being True
    if check:
        # get the bytearray of the hidden file with the readin function
        hidden_arr = readin(HIDDEN_FILE)
        # get the bytearray of the wrapper file with the readin function
        wrapper_arr = readin(WRAPPER_FILE)
        # with the byte MODE input
        if MODE == 'byte':
            # run it through the storage_byte function
            new_arr = storage_byte(INTERVAL, OFFSET, hidden_arr, wrapper_arr)
        # with the bit MODE input
        elif MODE == 'bit':
            # run it through the storage_bit function
            new_arr = storage_bit(INTERVAL, OFFSET, hidden_arr, wrapper_arr)
        # and then write the new bytearray to stdout
        stdout.buffer.write(new_arr)
    # in case check is set to False
    else:
        # print out the error message
        print("HIDDEN FILE IS TOO LARGE TO BE CONTAINED IN THE WRAPPER FILE WITH THE CURRENT OFFSET AND INTERVAL")

# if the retrieve function is called
if FUNC == "retrieve":
    # get the bytearray of the wrapper file
    wrapper_arr = readin(WRAPPER_FILE)
    # with the byte MODE input
    if MODE == 'byte':
        # run it through the extraction_byte function
        extract = extraction_byte(INTERVAL, OFFSET, wrapper_arr)
    # with the bit MODE input
    elif MODE == 'bit':
        # runit through the extration_bit function
        extract = extraction_bit(INTERVAL, OFFSET, wrapper_arr)
    # and the print the message to stdout
    stdout.buffer.write(extract)

    
    