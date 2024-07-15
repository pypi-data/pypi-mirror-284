import signal
import sys

def save(ab,ac):
    if  ab % ac == 0: 
        with open("stop.txt", "w") as vv:
            vv.write(str(ab))
        print("The output has been saved in stop.txt")

def handler(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)


