"""
Name Zachery Bignall 
Tilte : FTP (Storage) Covert Channel ( homework three)
version of python : 3.6

note to Dr.goud{ if you read this} just wanted to let you know that python works different in winodows and linux from command line .
    #i did not know this. testing thigns in linux and in windows from now on, just wanted to say that 

"""
#_______________________needed lib's __________________________________
import re
import ftplib


#___________________GOABL var's___________________________
IP = 'jeangourd.com'
PORT = 21
USERNAME = 'anonymous'
PASSWORD = ' '
FOLDER = '7' # where you want to go in the sever 
# method can be 7(looks at last 7 bits and discard thigns that have the 1st 3 bits fulled
	#or 10 read all bits  
METHOD = 7


#_____________MY def________________________________

#took from hw_1 and modded it

#for getting permissions to binary 
def PtoB(string,M):
    returnbinary = "";
    if M == 7:
        # for not getting the 1st 3 bits 
        for n in range(len(string)):
            temp = re.findall('[a-z]',string[n])

            #takeing out nosie 
            if n <= 2 and (temp):
                break;
            #gets a 1 is not a {-}
            elif n > 2 and (temp):
                returnbinary += '1';
            elif n > 2 :
                returnbinary += '0';


    #for getting the 1st 3 bits
    else:
        for n in range(len(string)):
            #gets a 1 is not a {-}
            temp = re.findall('[a-z]',string[n])
            if temp:
                returnbinary += '1';
            else:
                returnbinary += '0';

    return returnbinary

# name says it 
def decoder(bit):
    letter = chr(int(bit, 2));
    return letter;



#________________________MAIN______________________
lines=[];# var for ftp connect (ie what it gets from sever)

#part 1 connecting to the sever and gettign data 
ftp = ftplib.FTP();     
ftp.connect(IP,PORT);# connect to host
ftp.login(user=USERNAME,passwd=PASSWORD);           # user anonymous, passwd anonymous@
ftp.cwd(FOLDER); 
ftp.dir(lines.append);
#cloes the connection to the sever 
ftp.quit();

#part 2 of hw3 parse thorught the data  and gettign 1's and 0's 
binary_permissions='';

#makes permissions into binary, for all files read
for i in range((len(lines))):
    permissions = lines[i].split(' ');
    #permissions[0] is the real permissions , while permissions is the whole line
    binary_permissions += PtoB(permissions[0],METHOD);


#part 3 the decodeing part , pulled from hw1 
binary_bits=[];#gets the binary into 7-bit length  and ready for the decoder
temp='';# what saves the numbers {1|0} and clears at the end of every 7 bit.or 8-bit is method 10 

#7bit
for bits in range(len(binary_permissions)):
    temp += binary_permissions[bits];
    if ((len(temp)%7) == 0 and bits !=0 ):
            binary_bits.append(temp);
            temp='';
BL7 = "";# 7-bit letter 
OP7 = "";# 7-bit output
# sends 7 1's and 0's at a time to the decoder to get changed into letters/numbers
for j in range(len(binary_bits)):
        BL7 = decoder(binary_bits[j]);
        OP7+=BL7;
print(OP7);# prints the message {if its in 7 bit that is}


# this is run if METHOD is 10 b/c that could be 7-bit or 8-bit
#8-bit
if METHOD == 10:
    binary_bits=[];
    temp_8='';
    # 8-bit things
    for bits in range(len(binary_permissions)):
        temp_8 += binary_permissions[bits];
        if ((len(temp_8)%8) == 0 and i !=0):
                    #print("temp_8",len(temp_78));
                    binary_bits.append(temp_8);
                    temp_8='';
    BL8 = "";# 8-bit letter
    OP8 = "";# 8-bit output
    for w in range(len(binary_bits)):
        BL8 = decoder(binary_bits[w]);
        OP8+=BL8;
    print("\nif message above is garbage try below\n");
    print(OP8);# prints the message {if its in 7 bit that is}

#kills the program
exit();
