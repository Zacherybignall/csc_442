#####################DEF####################
#Name zachery Bignall
#title: steg
#verison:Python 2.7.17
#####################DEF byt ZAB####################

##### BTYE #######
#_____________________________________________________________________________________________

# i is for the sentienl , j is for the wrapper 
def check_sentinel(sentinel,wrapper,j,interval,i):
    #matchs to 6 b/c that means 5 was a match
    if (i == len(sentinel)):
        # match
        return 1;
    elif (j > len(wrapper)):
        print('thats not right, the number you are looking  for is outside the wrpper range');
        quit();
    #1st case only : gets next number , calling here already got 0
    elif (sentinel[i] == hex(wrapper[j])):
        # 1st case only :0 ,1 match check 2 next
        i+=1;
        j += interval;
        # note to self needs to return to its self , give the poath back 
        return check_sentinel(sentinel,wrapper,j,interval,i);
    # no match
    return 0;
#_____________________________________________________________________________________________

#for byte extraction {works}
def byte_extraction(sentinel,offset,interval,wrapper):
    # needs to read wrapper as binarty data is a file: bytearray
    f = open(wrapper,'rb');
    wrapper =  bytearray(f.read())
    f.close();
    # same with hidden
    hidden =  '';
    while offset < len(wrapper):
        #print(offset)
        b = (hex(wrapper[offset]));
        #print("s",sentinel[0]);
        if b == sentinel[0]:
            # checks for whole sentinel woth out messing up the hidden
            checker = check_sentinel(sentinel,wrapper,(offset+interval),interval,1);
            if checker == 1:
                #print('hello there im out');
                break;
        hidden += (chr(int(b,16)));
        offset += interval;
    # revel what was hidden;
    return (bytes(hidden));
#_____________________________________________________________________________________________

#for byte stroage {works} for small things(pic in pic) 49kb & 1163kb & i =20
def byte_stroage(sentinel,offset,interval,wrapper,hidden):
    #for byte stroage 
    # needs to read wrapper as binarty data is a file: bytearray
    f = open(wrapper,'rb');
    wrapper =  bytearray(f.read())
    f.close();
    # same with hidden
    f = open(hidden,'rb');
    hidden = bytearray(f.read())
    f.close();
    # storage the data 
    i = 0;
    while i < len(hidden):
        wrapper[offset] = hidden[i];
        offset += interval;
        i+=1;
    # storage the  sentinel
    i=0
    # needs to be right
    while i < len(sentinel):
        wrapper[offset] = ((int(sentinel[i],16)));
        offset += interval;
        i+=1;
    # give back with somethign new
    return wrapper;

##################### BIT #####################

#___________________________________________________________________________________________
# works but can see things on test_3 my be its the picture header?
def  bit_stroage(sentinel,offset,interval,wrapper,hidden):
    # needs to read wrapper as binarty data is a file: bytearray
    f = open(wrapper,'rb');
    wrapper =  bytearray(f.read())
    f.close();
    # same with hidden
    f = open(hidden,'rb');
    hidden = bytearray(f.read())
    f.close();
    # storage the data 
    i = 0;
    for i in hidden:
        for j in range(8):
            wrapper[offset] &= 11111110
            wrapper[offset] |= ((i & (1<<7)) >> 7)
            i = (i << 1) & (2 ** 8 - 1)
            offset += interval
        #i+=1;

    #i=0;
    for i in sentinel:
        for j in range(8):
            wrapper[offset] &= 11111110
            wrapper[offset] |= ((i & (1<<7)) >> 7)
            i= (i << 1) & (2 ** 8 - 1)
            offset += interval;
        #i+=1;
    return (wrapper);

#_________________________________________________________________________________________
def bit_extraction(sentinel,offset,interval,wrapper):
    # needs to read wrapper as binarty data is a file: bytearray
    f = open(wrapper,'rb');
    wrapper =  bytearray(f.read())
    f.close();
    # same with hidden
    hidden =  [];
    while offset < len(wrapper):
        b = 0;
        # gets 8 bits 
        for j in range(8): 
            if offset >= len(wrapper):
                continue;
            else:
            #works, python keeps track of it in int form but ite bin is right
                #b = (b << 1) & (2 ** 8 - 1);
                b |= (wrapper[offset] & 1);
            if j < 7:
                b = (b << 1) & (2 ** 8 - 1);
                offset += interval;
        # check sentinel
        if len(hidden)>=len(sentinel):
            if hidden[-len(sentinel):] == (sentinel):
                break;
        hidden.append(b);
        offset += interval;
    # remove the sentinel
    return bytearray(hidden[:-len(sentinel)])
##########################IMPORTS##########################
import sys;
########MAIN##################
#print(sys.argv);
SR = sys.argv[1]
mode = sys.argv[2]
#offset is when to start after the header
# interval  is set that number of bytle or bit ( mode) to skip till next pull number
# needs to be 0 by default
if sys.argv[3] == "-o":
    offset = 0;
else:
    offset = sys.argv[3].split('-o')
    offset = offset[1];

# sets up wrapper anad hidden file by mode
if "-s" in SR:
    if "-i" == sys.argv[4]:
        interval =1;
        wrapper = sys.argv[5].split('-w');
        wrapper = wrapper[1];
        hidden = sys.argv[6].split('-h');
        hidden = hidden[1];
        
    else:
        interval = sys.argv[4].split('-i');
        interval = interval[1];
        wrapper = sys.argv[5].split('-w');
        wrapper = wrapper[1];
        hidden = sys.argv[6].split('-h');
        hidden = hidden[1];
else:
    if "-i"== sys.argv[4]:
        interval =1;
        wrapper = sys.argv[5].split('-w');
        wrapper = wrapper[1];
    else:
        interval = sys.argv[4].split('-i');
        interval = interval[1];
        wrapper = sys.argv[5].split('-w');
        wrapper = wrapper[1];

####val#####
#save the sentinel is  0255002550 needs to be in hex for byte and int for bit 
z=(hex(0));
t = (hex(255));
sentinel=[z,t,z,z,t,z];
##############################################MAIN#########################################################

if "-s" in SR and '-B' in mode:
   wrapper = byte_stroage(sentinel,int(offset),int(interval),wrapper,hidden)
   sys.stdout.write(wrapper);
if "-r" in SR and '-B' in mode:
    hidden = byte_extraction(sentinel,int(offset),int(interval),wrapper)
    sys.stdout.write(hidden);
if "-s" in SR and '-b' in mode:
   wrapper = bit_stroage([0,255,0,0,255,0],int(offset),int(interval),wrapper,hidden)
   sys.stdout.write(wrapper);
if "-r" in SR and '-b' in mode:
    hidden = bit_extraction([0,255,0,0,255,0],int(offset),int(interval),wrapper)
    sys.stdout.write(hidden);
    

    
