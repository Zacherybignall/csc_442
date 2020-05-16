##################################################################
#Name:Zachery Bignall 
#TItle:XORCypto
#version: python 3.6.9
#################################################################


######IMPORTT##########
import sys

#######################VAULES##################
# the name of your key goes here
key = '17_2';

###########MAIN#########
# reading from stin
ciphertest = sys.stdin.buffer.read();
ciphertestarray=bytearray(ciphertest);

#getting the key 
f=open(key,"rb")
keyarray=bytearray(f.read())
f.close()

binarydata=[]
# in case the key is too short
k=0;
for i in range(len(ciphertestarray)):
    temp= (keyarray[k]^ciphertestarray[i]);
    #note bin 'makes' it a binary number but its a str for humans not binary
    #print(bin(temp));
    binarydata.append(temp);
    k+=1;
    # resets the key 
    if k == len(keyarray):
        k =0;
binarydata= bytearray(binarydata);
#print(binarydata);
sys.stdout.buffer.write(binarydata);
