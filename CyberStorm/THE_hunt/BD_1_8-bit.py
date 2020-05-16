#csc_442_hw1
# written in python 3.7.2
#ZAB: Zachery Bignall
################################################################################################
#the idea \/
"""
# this works for acsii 7-bit and 8-bit , reads it right when feed number of bits 
binary_string = '0100000'
print(int(binary_string, 2),chr(int(binary_string, 2)),int(binary_string, 2));
print(chr(int(binary_string, 2)));
from here : https://stackoverflow.com/questions/9509502/in-python-how-do-you-convert-8-bit-binary-numbers-into-their-ascii-characters
"""
# for command line Arguments
#!/usr/bin/python
import sys;
#input a list 7 long and returna one str of all things in list 
def bit_7(list):
    bit = "";
    for k in range(7):
        bit+=list[k];
    return bit;
#input a list 8 long and returna one str of all things in list 
def bit_8(list):
    bit = "";
    for i in range(8):
        bit+=list[i];
    return bit;
#this can take 7 or 8 bit, takers the string from input makes it a number then a char based off that number.
def decoder(bit):
    letter = chr(int(bit, 2));
    #print(letter);
    return letter;
#_________main()______
def main(input):
    data = [];  
    # saves  as a table just in case its not only one line of binary 
    for line in input:
        data.append((list(str(line))));
        #from here :https://stackoverflow.com/questions/1906717/splitting-integer-in-python
    #print('data[0]',data[0][0],type(data[0][0]));
    #print('len(data[0])',len(data[0]));# if past number stop loop
    #print(data);
    #holds bits in a list    
    bits_8 = [];
    bits_7 = [];
    # holders of bit of  nubmers for the for loop 
    temp_7 =[];
    temp_8 =[];
    #print(len(data[0]));
    i=8;
    while i < (len(data[0])):
        temp_7.append(data[0][i]);
        #temp_8.append(data[0][i]);
        if ((len(temp_7)%8) == 0 and i !=0 ):
            #print("temp_7",len(temp_78));\
            #print(temp_7);
            bits_7.append(bit_7(temp_7));
            temp_7.clear();
            i+=7;
        i+=1;
        #elif ((len(temp_8)%8) == 0 and i !=0):
            #print("temp_8",len(temp_78));
            #bits_8.append(bit_8(temp_8));
            #temp_8.clear();   
    BL8 = "";# 8-bit letter 
    BL7 = "";
    OP7 = []; # 7-bit ouput
    OP8 = "";
    #print('lenlen(bits_7)',len(bits_7))
    #print('lenlen(bits_8)',len(bits_8))
    # bits_8 and bits_7 are very differnt.....very.....
    for j in range(len(bits_7)):
        #print(bits_7[j]);
        BL7 = decoder(bits_7[j]);
        OP7.append(BL7);
    #for w in range(len(bits_8)):
        #BL8 = decoder(bits_8[w]);
        #OP8+=BL8;
    return OP7#,OP8;
#,OPF8
OPF7 = main(sys.stdin);
print("7 bit = ",OPF7);
#print("8 bit = ",OPF8);
