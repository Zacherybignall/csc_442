#csc_442_hw2
# written in python 3.7.2
#ZAB: Zachery Bignall
######################################################################################################
# for command line Arguments
# note to self , cant to chr() b/c only using 26 letters not all of ascii
#!/usr/bin/python
import sys;
import string;
# need a list of A/z : from here:https://www.geeksforgeeks.org/python-ways-to-initialize-list-with-alphabets/
# using string  , for filling alphabets
THE_list = [];
THE_list = list(string.ascii_lowercase) 
def encryption (p,k):
    c = (p+k)%len(THE_list);
    #print("c in encryption",c);
    return THE_list[c];
    #exit();
def decryption (c,k):
    p = (len(THE_list)+c-k)%len(THE_list);
    #print("p in decryption",p);
    return THE_list[p];

def main (key,TM,argv):
    # what to tell if upper or lower case for output and key ,do all work in lower case and throw flag if it needs to be upper or lower case.
    UPcase_flag = 0 ;#flag that makes out put upper case or lower case
    if TM.isupper() == True:
        UPcase_flag =1;
        TM = TM.lower();
    output = "";
    KYI = 0;# value to restart the key if out of index
    if (len(sys.argv)) < 0  :
        print("Please only call me right")
        sys.exit();
    if argv == "-e":
        #encryption
        #p=plaintext,c=ciphertext,k=key
        #c=(P+K)
        for i in range (len(TM)):
            if KYI >= len(key):
                KYI = 0 ;
            if TM[i] == " ":
                output += " ";
            else:
                #print("THE_list.index(TM[i]),THE_list.index(key[KYI])",THE_list.index(TM[i]),THE_list.index(key[KYI]));
                c = (encryption(THE_list.index(TM[i]),THE_list.index(key[KYI])));
                #print(c);
                output += c;
            KYI+=1;
        #print("-e");
        if UPcase_flag ==1:
            output = output.upper();
        print(output);
    elif argv == "-d":
        #decryption
        #p=plaintext,c=ciphertext,k=key
        #p=(26 + (c-K))
        for i in range (len(TM)):
            #resets the key 
            if KYI >= len(key):
                KYI = 0 ;
            # adds spaceing to the message is there is any
            if TM[i] == " ":
                output += " ";    
            else:
                #print("THE_list.index(TM[i]),THE_list.index(key[KYI])",THE_list.index(TM[i]),THE_list.index(key[KYI]));
                p = (decryption(THE_list.index(TM[i]),THE_list.index(key[KYI])));
                #print(p);
                output += p;
            KYI+=1;
        #print("-d");
        if UPcase_flag ==1:
            output = output.upper();
        print(output);
    else:
        print("Only accepted arguments are -e, -d and {key you wish to use}")
        sys.exit();
key = sys.argv[2];
#removes whitespace 
key = key.replace(" ","");
#removes " from strat and end of key if there 
key = key.replace("'","");
# makes it lower case 
key = key.lower();
#TM = "HELLO";
argv = sys.argv[1];
# for command line interface , w/o the face 
# TODO : commands from a file throws error for input
while(True):
    # suppers an error i was getting for takeing input
    try:
        TM = input();
    except EOFError:
        break;
    # "\x04" is ctrl+D is ascii {I think}}
    if TM == "\x04":
        exit();
    main(key,TM,argv);
'''
# not goign to use but cool thigns
#from here :https://www.programiz.com/python-programming/examples/ascii-character
# ASCII
# char to number
print(ord('p'));
# number to char  
print(chr(112));
'''
'''   
print(sys.argv[0]);    
print(sys.argv[1]);
print(sys.argv[2]);
#print(sys.argv[3]);
'''
