# Ross Piraino 5/8/2020
#made for python 3
from sys import stdin
from datetime import datetime
from hashlib import md5

DEBUG = True

interval = 60

now = datetime.now()

#reads input
inp = stdin.read().rstrip("\n")
#uses input to plug in as a datetime for use with other datetime functions later
epoch = datetime(int(inp[:4]), int(inp[5:7]), int(inp[8:10]), int(inp[11:13]), int(inp[14:16]), int(inp[17:19]))

#fins the seconds betweeen the two
seconds = int((now-epoch).total_seconds())
#removes the extra seconds that are not enough to hit the interval again
secvar = int(seconds / interval) * interval

md51 = md5(str(secondvar).encode()).hexdigest()
md52 = md5(md51.encode()).hexdigest()

#initialize some varaibles for code segment
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
mdletters = ""
mdnumbers = ""
code = ""
#counts the number of letters and numbers in md5
for i in md52:
    for l in alphabet:
        if i == l:
            mdletters += i
    for n in numbers:
        if i == n:
            mdnumbers += i

#adds to code string based on lengths of mdletters and mdnumbers
if len(mdletters) == 1:
    code += mdletters
    code += mdnumbers[len(mdnumbers) - 1]
    code += mdnumbers[len(mdnumbers) - 2]
    code += mdnumbers[len(mdnumbers) - 3]
elif len(mdletters) == 0:
    code += mdnumbers[len(mdnumbers) - 1]
    code += mdnumbers[len(mdnumbers) - 2]
    code += mdnumbers[len(mdnumbers) - 3]
    code += mdnumbers[len(mdnumbers) - 4]
elif len(mdnumbers) == 1:
    code += mdletters[:3]
    code += mdnumbers
elif len(mdnumbers) == 0:
    code += mdletters[:4]
else:
    code += mdletters[:2]
    code += mdnumbers[len(mdnumbers) - 1]
    code += mdnumbers[len(mdnumbers) - 2]

#prints nice looking values for debug mode or just the code for non-debug
if DEBUG == True:
    print("Current: {}".format(now))
    print("Epoch: {}".format(epoch))
    print("Seconds: {}".format(seconds))
    print("Secvar: {}".format(secvar))
    print("MD5 1: {}".format(md51))
    print("MD5 2: {}".format(md52))
    print("Code: {}".format(code))
else:
    print(code)
