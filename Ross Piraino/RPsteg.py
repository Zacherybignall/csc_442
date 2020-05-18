#Ross Piraino 5/8/2020
#Made for python 3
from sys import stdin, argv

DEBUG = True

#default values for interval and offset
interval = 1
offset = 0

#reads the args and stores them as their variables
for arg in argv:
    if arg[1] == "s":
        mode = "s"
    elif arg[1] == "r":
        mode = "r"
    elif arg[1] == "b":
        bmode = "b"
    elif arg[1] == "B":
        bmode = "B"
    elif arg[1] == "o":
        offset = int(arg[2:])
    elif arg[1] == "i":
        interval = int(arg[2:])
    elif arg[1] == "w":
        wrapperfile = arg[2:]
    elif arg[1] == "h":
        hiddenfile = arg[2:]

if DEBUG:
    print("args: {}".format(argv))
    print("mode: {}".format(mode))
    print("bmode: {}".format(bmode))
    print("offset: {}".format(offset))
    print("interval: {}".format(interval))
    print("wrapperfile: {}".format(wrapperfile))
    print("hiddenfile: {}".format(hiddenfile))

wrappercontent = open(wrapperfile).read()
print(str(wrappercontent))
