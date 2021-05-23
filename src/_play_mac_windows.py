import sys

from playsound import playsound

'''Standalone python program to play a sound file on mac/windows'''

if __name__ == "__main__":
    playsound(sys.argv[1])
