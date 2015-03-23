import time
import sys

def time_str(timestamp):
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

a = time_str(int(sys.argv[1]))
print a


