import os
import sys

arg = sys.argv[1]

def sendPing(arg):
    response = os.system("ping -c 1 " + arg)
    return response

print(sendPing(arg))