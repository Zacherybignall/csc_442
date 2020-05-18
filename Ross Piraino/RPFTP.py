#Ross Piraino 4/3/2020
#Python 3
from ftplib import FTP

########## DECODE SECTION COPIED FROM BINARY PROGRAM
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
##################################################

#FTP Globals
IP = "jeangourd.com"
PORT = 21
FOLDER = "7"

#MODE FOR NUMBER OF BITS
#7 for 7 bit, 10 for 10 bit, and -1 for both
MODE = -1

#initialize contents
contents = []

#connect to ftp with IP and PORT and fetch file listing then disconnect
ftp = FTP(IP)
ftp.connect(IP, PORT)
ftp.login()
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

#initialize 7 bit and 10 bit inputs
seveninput = ""
teninput = ""

#reads input and puts it into the seveninput and teninput strings
for row in contents:
    it = 0
    while it < 10:
        if row[it] == "-": #reads dashes as 0's
            inpt = "0"
        else: #if its not a dash, reads a 1
            inpt = "1"
        if it > 2: #skips the first 3 characters for the 7 digit input
            seveninput += inpt
        teninput += inpt
        it += 1

#decodes based on which value MODE is then prints output
if (MODE == 7) or (MODE == -1):
    sevenout = decode(seveninput, 7)
    print(sevenout)
if (MODE == 10) or (MODE == -1):
    tenout = decode(teninput, 10)
    print(tenout)
    
