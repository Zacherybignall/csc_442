##########################
# Name: Alex Faucheux
# Date: 4/2/2020
# Program: FTP Covert
# Language: Python 3.8
###########################
from ftplib import FTP

''' Constants '''
# Needs to be 7 or 10 or program won't run
METHOD = 10

# Constants for ftp server
HOST = "jeangourd.com"
PORT = 21
FOLDER = "%d" % METHOD


# Binary decoder algorithm from last assignment
def binary_decoder(b_string, n):
    txt = ""

    # Iterates through the string every nth character
    # n is a variable that represents number of bits
    for i in range(0, len(b_string), n):
        # Converts the binary string of set # of bits into a ASCII decimal
        decimal = int(b_string[i:i + n], 2)

        # ASCII 8 is a backspace. Deletes the last character
        if decimal == 8:
            txt = txt[:-1]

        # Add character to txt
        else:
            txt += chr(decimal)

    return txt


# Method 7
def method7(contents):
    byte = ""
    # Convert each row to an ascii character and append to msg
    for row in contents:
        # Skips any row that does not start with "---"
        if row[:3] == "---":
            # Convert row to binary
            for char in row[3:10]:
                if char != "-":
                    byte += "1"
                else:
                    byte += "0"
            # Add ascii character of byte to message
    msg = binary_decoder(byte, 7)

    return msg


# Method 10
def method10(contents):
    byte = ""

    # Convert each row to binary and append to byte
    for row in contents:
        for char in row[:10]:
            if char != "-":
                byte += "1"
            else:
                byte += "0"

    msgs = []

    # Append 7-bit msg to msgs
    if len(byte) % 7 == 0:
        msgs.append("7-bit:\n" + binary_decoder(byte, 7))

    # Append 8-bit msg to msgs
    if len(byte) % 8 == 0:
        msgs.append("8-bit:\n" + binary_decoder(byte, 8))

    return msgs


# Retrieves files from specified ftp server and logs in anonymously
# Files are put into a list and returned
def getFiles():
    contents = []
    ftp = FTP()
    ftp.connect(HOST, PORT)
    ftp.login()
    ftp.cwd(FOLDER)
    ftp.dir(contents.append)
    ftp.quit()
    return contents


if __name__ == "__main__":
    files = getFiles()
    if METHOD == 7:
        message = method7(files)
        print(message)

    elif METHOD == 10:
        messages = method10(files)
        for message in messages:
            print(message)

    else:
        print("Incorrect Method")
