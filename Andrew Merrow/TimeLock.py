##################################################################
#Andrew Merrow
#5/7/20
#Timelock assignment
#Python 2.7
#This program takes a specified epoch time from the command line
#then produces a code based on the amount of seconds between
#the two times
##################################################################


from  hashlib import md5
import sys
import datetime 
import pytz

DEBUG = False

#setup timezone for converting to utc
tz = pytz.timezone('America/Chicago')
utc = pytz.timezone('UTC')



#read the provided epoch from stdin
epoch = raw_input()

#hard coded current time for debugging
#current_time = datetime.datetime(2017, 03, 23, 18, 02, 06)

#get current time and convert to utc
current_time = datetime.datetime.now()
current_tz = tz.normalize(tz.localize(current_time))
current_time = current_tz.astimezone(utc)

if(DEBUG):
	print("current: " + str(current_time))


#format the epoch time and convert to utc
epoch = epoch.split(" ")
epoch = map(int, epoch)

if(DEBUG):
	print ("epoch after split: " + str(epoch))

epoch_time = datetime.datetime(epoch[0], epoch[1], epoch[2], epoch[3], epoch[4], epoch[5])
epoch_tz = tz.normalize(tz.localize(epoch_time))
epoch_time = epoch_tz.astimezone(utc)

if(DEBUG):
	print ("epoch time: " + str(epoch_time))

#calculate time difference
final_time = int((current_time - epoch_time).total_seconds())

if(DEBUG):
	print ("final time: " + str(final_time))


#change to the beginning of the 60 seconds interval
interval = final_time % 60
final_time = final_time - interval

if(DEBUG):
	print ("final time after interval: " + str(final_time))

###############################hash and extract#########W#################################################

#perform the double hash
hashish = md5(str(final_time))
hashish = hashish.hexdigest()
if(DEBUG):
	print ("hash1: " + str(hashish))

hashish = md5(str(hashish))
secret = hashish.hexdigest()
if(DEBUG):
	print "hash2: " + str(secret)


password = ""
#extract the first two letters
counter1 = 0
for i in secret:
	if(ord(i) > 65):
		password += i
		counter1 += 1
	if (counter1 == 2):
		break

#reverse the string then extract the first two numbers
backwards = secret[::-1]
counter2 = 0
for i in backwards:
	if(ord(i) <= 57):
		password += i
		counter2 += 1
	if(counter2 == 2):
		break
#print out the passowrd
print password
