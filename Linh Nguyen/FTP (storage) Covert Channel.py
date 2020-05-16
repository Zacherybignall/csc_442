##########################################################
#Name: Linh Nguyen
#Assignment: FTP Covert Channel
#Python Ver: 2.7.17
##########################################################

# import FTP from ftplib for starting connection
from ftplib import FTP

##########################
# globals (FTP specifics)
##########################
METHOD = 7              #
IP = "jeangourd.com"     # 
PORT = 21                #   
FOLDER = "7"            #   
##########################

# the file/folder contents
global contents
contents = []

# initiate connection with the FTP server ti fetcha file listing
# give the connection name ftp
ftp = FTP()
# connect to the server with the specified IP and PORT provided above
ftp.connect(IP, PORT)
# login into the server anonymously 
ftp.login()
# change working directory to the folder 
ftp.cwd(FOLDER)
# get all the content of the folder and add into the contents list
ftp.dir(contents.append)
# close the connection
ftp.quit()

# function extract gets the permission fields of each file and put it into a string
def extract(contents, METHOD):
    # initiate a string to store the permission fields
    info = ""
    # next the program will choose its way to extract the needed information according to METHOD
    # in case the specified METHOD is 7
    if METHOD == 7:
        # read in all the row in the contents list
        for row in contents:
            # check for the first 3 character of each row to see if they're all empty
            # if they're all empty (---) then its the valid permission field
            if row[0:3] == "---":
                # then the program will add the permission field
                # with its first 3 character left out to the info string
                info += row[3:10]
    # in case the specified METHOD is 10
    elif METHOD == 10:
        # read in all the row in the contents list
        for row in contents:
            # add the whole permission field to the info string
            info += row[0:10]
    # return the info string that contains a chain of permission fields
    return info

# function convert reads in the string contains a chain of permission fields and convert it to binary
def convert(info):
    # initiate a string to store the bits
    bits = ""
    # go through each character in the string
    for character in info:
        # if the character is empty
        if character == "-":
            # then add 0 to the bits string
            bits += "0"
        # if the character is anything else
        else:
            # then add 1 to the bits string
            bits += "1"
    # return the bits string
    return bits

# function decode will read in the bits string and decode the message
def decode(binary):
        # initiate the decoded message as an empty string
        text = ""
        # initiate the bit counter
        i = 0
        # the decode function will token the binary values up to 7-bits
        # since that's what the message is in
        # with the length of binary is not specified to be divisible by 7 (for the 10 method)
        # the program will check everytime it tokens the string 7-bits at a time
        # this will prevent it going out of index as well as ignoring the last few bits that doesn't add up
        while (i < len(binary) and ((i+7)<=len(binary))):
            # the byte variable will read in the binary value
            # from position ith to (i+7)th
            byte = binary[i:i+7]
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
            i += 7
        # repeat when it can't be tokened up anymore
        # return the translated text
        return text

# getting the permission field as a string
info = extract(contents, METHOD)
# convert the permission field string into bits
bits = convert(info)
# decode the message from the bits
message = decode(bits)
# and finally print out the message
print message
