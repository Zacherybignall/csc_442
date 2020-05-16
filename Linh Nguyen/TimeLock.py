###################################################################################
#Name: Linh Nguyen
#Assignment: TimeLock
#Python Ver: 2.7.17
###################################################################################

#NOTE: Epoch time can be input from a file or directly from the command line
#      as long as it follows the format YY MM DD hh mm ss 

# import libraries for useage
#from sys import stdin, argv
import sys as sys
import hashlib
import time
from datetime import datetime
# pytz library is used to convert given time to UTC
import pytz
# initiate variables

# MANIPULATION ZONE
########################################################
# DEBUG mode
DEBUG = True
# time interval 
INTERVAL = 60
# MANUAL_TIME to set system time
#MANUAL_TIME = "2017 04 26 15 14 30"
MANUAL_TIME = ""
#########################################################

# OTHER VARIABLES 
# upon converting, the timezone of New York will be used
local_time = pytz.timezone("America/New_York")
# space for format manipulation
space = " "
# readin to store the stdin fromt the command line
readin = ""
# now to obtain system time
now = datetime.now()
# change the format accordingly
current_time = now.strftime("%Y %m %d %H %M %S")
# this will set the default system time to the current time
first_un = current_time

# EARLY CHECKING
# checing stdin from the command line
# if there are more than one file at a time
if len(sys.argv) > 1:
    # print a statement and exist
    print "Too many arguments!"
    sys.exit()
# if the given stdin is valid
else:
    readin = str(sys.stdin)

# FUNCTION ZONE
# validate function to check the format of the input time
def validate(date_text):
    try:
        # create variabla a to check for the correct format
        a = datetime.strptime(date_text, '%Y %m %d %H %M %S')
        # if it is right, the function shall yield no error
        # and return a as the appropriate 
        return a.strftime('%Y %m %d %H %M %S')
    # in case the input is in the wrong format
    except ValueError:
        # print a statement and return nothing
        print "Incorrect data format, should be YYY MM DD hh mm ss"
        return None


# hashing function to generate the required md5 hash from a value
def hashing(time_elapsed):
    # initiate the first hash with variable m
    m = hashlib.md5()
    # generate md5 hash from the given value first time
    m.update(str(time_elapsed))
    # turn the hash value into a string
    n = str(m.hexdigest())
    # initiate the second hash with variable a
    a = hashlib.md5()
    # generation md hash from the given value the second time
    a.update(n)
    # return the 2 md5 hashes generated from the given value
    return a.hexdigest(), n

# extract function to obtain the code from the hash value
def extract(hash_value):
    # initiate pointer to run from the beginning of the string
    start = 0
    # initiate pointer to run from the end of the string
    end = 1
    # get the length of the hash value
    length = len(hash_value)
    # initiate an extraction string to store the code
    extraction = ""
    # initiate head_counter and tail_counter
    # to obtain the appropriate numbers of characters
    head_counter = 0
    tail_counter = 0

    # first run from left to right
    # making sure the pointer doesn't go out of index
    # and the number of alphabetic characters doesn't exceed 2
    while start <= length and head_counter < 2:
        # check the current character to see if it's a letter
        if hash_value[start].isalpha() == True:
            # add the character to the code
            extraction += hash_value[start]
            # and increase the counter by 1
            head_counter += 1
        # increase the pointer position by 1
        start += 1

    # secondly run from right to left
    # making sure the pointer doesn't go out of index
    # and the number of numberic characters doesn't exceed 2
    while end <= length and tail_counter < 2:
        # check the current character to see if it's a number
        if hash_value[length-end].isdigit() == True:
            # add the character to the code
            extraction += hash_value[len(hash_value) - end]
            # and increase the counte by 1
            tail_counter += 1
        # increase the pointer position by 1
        end += 1

    # in the end, return the 4-character code
    return extraction

# time_extract function to find the difference between 2 periods of time in seconds
def time_extract(first, second):
    # split the strings of time into list
    # this will make it easier to access each components
    first_c = first.split()
    second_c = second.split()
    # turn the 2 lists back into datetime objects for calculating
    first_time = datetime(int(first_c[0]), int(first_c[1]), int(first_c[2]), int(first_c[3]), int(first_c[4]), int(first_c[5]))
    second_time = datetime(int(second_c[0]), int(second_c[1]), int(second_c[2]), int(second_c[3]), int(second_c[4]), int(second[5]))

    end = int(second_c[5])
    if end == 0:
        end = -1
    total = (first_time-second_time).total_seconds() - end
    # return the value
    return int(total)

# utc function to convert the given time to UTC time
def utc(local_datetime):
    import time
    import datetime as dt
    # read in the datetime and extract the information accordingly
    naive_datetime = datetime.strptime(local_datetime, "%Y %m %d %H %M %S")
    # obtain the converted local time by localizing it according to New York timezone
    local_datetime = local_time.localize(naive_datetime, is_dst=None)
    # and then obtain the converted datetime
    utc_datetime = local_datetime.astimezone(pytz.utc)
    # finally return the converted datetime
    return utc_datetime

##########################################################################################
# MAIN PART

# check stdin
# first to see if there's a file as an input
# if there's no file, assume the input will be typed manually
if readin.find("open file '<stdin>'") > 0 :
    # prompt for input
    info = raw_input("")
else:
    # read in the information
    info = stdin.read().rstrip('\n')
# check for the time format
status = validate(info)
# if the input is valid
if status != None:
    # give it the second_un variable
    second_un = status
# if not then exit
else:
    sys.exit()
# check for MANUAL_TIME
# in case it's not given then use the default system time
if MANUAL_TIME == "":
    pass
# if MANUAL_TIME is given
else:
    # give it to the first_un variable
    check = validate(MANUAL_TIME)
    if check != None:
        first_un = MANUAL_TIME
    else:
        sys.exit()

# convert the 2 time variables into UTC timezone
first_raw = utc(first_un)
second_raw = utc(second_un)
# convert the 2 UTC variables into the appropriate format ('%Y %m %d %H %M %S')
first = first_raw.strftime('%Y %m %d %H %M %S')
second = second_raw.strftime('%Y %m %d %H %M %S')
# extract the second difference between the 2 datetime objects
time_extraction_raw = time_extract(first, second)
# to make sure the code stays valid for 60 seconds
# first we check for the mod value of the total second and 60
# in case the value is different from 0
if (time_extraction_raw % INTERVAL) != 0:
    # we'll reset the total second to the value when the interval begins
    # it can be done by subtracting the mod value
    time_extraction = time_extraction_raw - (time_extraction_raw % INTERVAL)
# in case the value is right on the interval
else:
    # basically use the total second calculated
    time_extraction = time_extraction_raw
# get the hash values from the hashing function with the total second as input
hash_value2, hash_value1 = hashing(time_extraction)
# and obtain the code using the extract function
code = extract(hash_value2)

# in DEBUG mode
if DEBUG == True:
    # input the raw values into the debugging function to print out
    # print out the current time in UTC timezone
    print "Current (UTC): {}".format(first_raw)
    # print out the epoch time in UTC timezone
    print "Epoch (UTC): {}".format(second_raw)
    # print out the original second difference
    print "Seconds: {}".format(time_extraction_raw)
    # print out the reset second difference
    print "Seconds: {}".format(time_extraction)
    print "MD5 #1: {}".format(hash_value1)
    print "MD5 #2: {}".format(hash_value2)
    print "Code: {}".format(code)
else:
    # just print the code obtained
    print
    print code
    print
