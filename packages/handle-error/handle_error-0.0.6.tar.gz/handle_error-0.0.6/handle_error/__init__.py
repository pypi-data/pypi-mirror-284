import signal
import sys

def save(loop,line):
    if  loop % line == 0: 
        with open("stop.txt", "w") as vv:
            vv.write(str(loop))
        print("The output has been saved in stop.txt")

def handler(signum, frame):
    global loop,line
    save(loop,line)
    sys.exit(0)

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)


