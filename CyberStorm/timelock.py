
###############################################
#Name : Zachery Bignall 
#Tile : timelock
#Version of python : 3.6.9
################################################

####### import's ##########
from datetime import datetime
import time
from hashlib import  md5;
from sys import stdin
# for time zome change
import pytz
import re

#_debug mode 
DEBUG=False;
def main(input_date):
    #####################val's ###########################
    #setting time
    # for main run use " "  if not (e.g., 2015 01 01 00 01 30). 
    main_time='';
    INTERVAL=60;
    #setting  epoch_time (e.g., 1999 12 31 23 59 59). 
    epoch_time='';
    code='';

    ##MAIN##

    # if somethign from sidin override epoch_time
    if input_date:
        # just in case , remove '|" from the str input
        input_date = input_date.replace("'","");
        input_date = input_date.replace('"','');
        argumentList =  input_date.split();
        epoch_time =datetime(int(argumentList[0]),int(argumentList[1]),int(argumentList[2]),int(argumentList[3]),int(argumentList[4]),int(argumentList[5]));
    if main_time == '':
        main_time=datetime.now().replace(microsecond=0);
    else:
        main_time =  main_time.split();
        main_time =datetime(int(main_time[0]),int(main_time[1]),int(main_time[2]),int(main_time[3]),int(main_time[4]),int(main_time[5]));
    #make both times UTF times
    main_time = main_time.astimezone(pytz.utc)
    epoch_time= epoch_time.astimezone(pytz.utc)

    # get the diff in times
    diff = main_time-epoch_time;
    total_seconds = int(diff.total_seconds());
    if DEBUG:
        print("Current(UTC): ",main_time)
        print("Epoch(UTC): ",epoch_time);
        print("Seconds: ",total_seconds);

    # setting up interval checking
    remainder = total_seconds%INTERVAL;
    if remainder != 0 :
        total_seconds -= round(remainder)
    if DEBUG:
        print('fix for interval');
        print("Seconds: ",total_seconds);

    # hashing x2 and to match ouptu making it a int
    hash1 = md5(str(total_seconds).encode());
    hash2 = md5(hash1.hexdigest().encode());
    if DEBUG:
        print("hash 1 ",hash1.hexdigest());
        print("hash 2 ",hash2.hexdigest());

    # getting the hash code 
    main_str = str(hash2.hexdigest());


    # getting  first two letters ([a-f]) LtR
    letters = re.findall("[a-f]", main_str)
    code += letters[0]+letters[1];


    #getting two single-digit integers ([0-9]) RtL
    numbers = re.findall("[0-9]", main_str)
    code += numbers[-1]+numbers[-2];
    
    code += main_str[int(len(main_str)/2)]
    code += main_str[int(len(main_str)/2)+1]

    # the end is ni
    return code, main_time

# getts inpur from file or cmd 
date_input=''
for line in stdin:
        date_input +=(str(line));
code ,main_time = main(date_input);
print(code);
#print('\nCurrent system time:',main_time.strftime("%Y %m %d %I %M %S"));
