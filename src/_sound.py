import os
import sys
import time
from sys import platform

from playsound import playsound

'''Standalone python program to play a sound file on linux or mac/windows'''

if __name__ == "__main__":
    print("started\t", time.time())
    if platform.startswith('linux'):
        os.system('aplay {}'.format(sys.argv[1]))
        pass
    else:
        playsound(sys.argv[1])
