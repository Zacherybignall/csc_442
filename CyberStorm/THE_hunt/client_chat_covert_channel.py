################################################################################
## name: ZAB : Zachery Bignall
## title:Chat (Timing) Covert Channel
#version : python 3.6.9
################################################################################

#####___imports__############
import socket
from sys import stdout
from time import time
import binascii 

# enables debugging output, prints timeing and the binary its gets.
DEBUG = True;

######################____VARIABLES_____(THAT MAY NEED TO CHANGE)##############
# set the server's IP address and port
#ip = 'jeangourd.com'
#port = 31337
ip='138.47.99.163';
port=12321
# bin for the cover message
covert_bin=''

#data for cathing convert
#and give room for error (slower or faster: on the bigger number)
# no need for a zero :/
#.1
#.15
#.2
ZERO = .1#0.2#0.1
ONE = .15#0.1#0.2

######start program############
# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
s.connect((ip, port))

# have two main one for if ONE is bigger and another is ZERO is bigger
########main#######
if(ZERO < ONE): 
        #way one delta >= ONE
        # receive data until EOF ie reading the data as it comes
        data = s.recv(4096).decode('ascii');
        while (data.rstrip("\n") != "EOF"):
                # output the data
                stdout.write(data)
                stdout.flush()
                # start the "timer", get more data, and end the "timer"
                t0 = time()
                # gets next latter must decode 
                data = s.recv(4096).decode('ascii')
                t1 = time()
                # calculate the time delta (and output if debugging)
                delta = round(t1 - t0, 3)
                # checking if 1 or 0
                if (delta >= ONE):
                        covert_bin += "1";
                else:
                        covert_bin += "0";
                if (DEBUG):
                        stdout.write(" {}\n".format(delta))
                        stdout.flush()
                        #print(covert_bin);
else:
        #way one delta >= ZERO
        # receive data until EOF ie reading the data as it comes
        data = s.recv(4096).decode('ascii');
        while (data.rstrip("\n") != "EOF"):
                # output the data
                stdout.write(data)
                stdout.flush()
                # start the "timer", get more data, and end the "timer"
                t0 = time()
                # gets next latter must decode 
                data = s.recv(4096).decode('ascii')
                t1 = time()
                # calculate the time delta (and output if debugging)
                delta = round(t1 - t0, 3)
                # checking if 0 or 1
                if (delta >= ZERO):
                        covert_bin += "0";
                else:
                        covert_bin += "1";
                if (DEBUG):
                        stdout.write(" {}\n".format(delta))
                        stdout.flush()
                        
# close the connection to the server
s.close()
if DEBUG:
        print("covert_bin",covert_bin);

# serect message printing  goes here.
covert = '';
i = 0
while (i < len(covert_bin)):
        # process one byte at a time
        b = covert_bin[i:i + 8]
        # convert it to ASCII
        n = int("0b{}".format(b),2);
        # checks if n is in normal ascii table ie english letters 
        if 33 <= n >= 127 :
                covert += "?";
        else:
                covert += chr(n)
        i += 8;
        #TODO: stop at the string "EOF"
        if covert.find('EOF') != (-1):
                #remove the EOF from covert
                covert = covert[:-3];
                break;
# output the covert message
stdout.write('\nCovert message: {} \n'.format(covert))
