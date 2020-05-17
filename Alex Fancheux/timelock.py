############################
# Name: Alex Faucheux
# Date: 5/6/2020
# Language: Python 3.8.1
############################

from datetime import datetime, timezone
from hashlib import md5
from sys import stdin

DEBUG = False

# Set manual current time for debugging
MANUAL_CURRENT_TIME = "2017 03 23 18 02 06"
INTERVAL = 60

# Reads from standard input and strips the newline
txt = stdin.read().rstrip("\n")


# Create datetime object using input epoch time
try:
    epoch = datetime.strptime(txt, "%Y %m %d %H %M %S")

    # Convert epoch datetime to utc
    # (Method only works with python3.3 and later)
    local = epoch.astimezone()
    epoch_utc_dt = local.astimezone(timezone.utc).replace(tzinfo=None)

except ValueError:
    raise ValueError("Incorrect date format, should be YYYY mm dd HH MM SS")


# Get current datetime in utc
if DEBUG:
    curr_time = datetime.strptime(MANUAL_CURRENT_TIME, "%Y %m %d %H %M %S")
    local = curr_time.astimezone()
    curr_time = local.astimezone(timezone.utc).replace(tzinfo=None)

else:
    curr_time = datetime.utcnow()

# Calculates time differences in datetime objects
# Gets the seconds value using the timedelta object
dif = curr_time - epoch_utc_dt
seconds1 = int(dif.total_seconds())

# Calculates the interval time
seconds2 = seconds1 - (seconds1 % INTERVAL)

# Gets hash using seconds2
hsh = md5(repr(seconds2).encode('utf-8')).hexdigest()
hsh = md5(hsh.encode('utf-8')).hexdigest()

i = 0
code = ""

# Generate the characters for code
for char in hsh:
    if i == 2:
        i = 0
        break

    if char.isalpha():
        code += char
        i += 1

# Generate the numbers for the code
for n in range(1, len(hsh) + 1):
    if i == 2:
        break

    char = hsh[-n]

    if char.isdigit():
        code += char
        i += 1

code += hsh[int(len(hsh)/2)]

if DEBUG:
    print("Current (UTC): {}".format(curr_time))
    print("Epoch (UTC): {}".format(epoch_utc_dt))
    print("Seconds: " + str(seconds1))
    print("Seconds: " + str(seconds2))
    print("Hash: " + hsh)

print("Code: {}".format(code))
