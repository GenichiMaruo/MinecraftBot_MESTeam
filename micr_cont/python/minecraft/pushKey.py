import pydirectinput

import time

import sys

################################
sleep_time = 0.02
################################

def push_key(key):
    pydirectinput.keyDown(key)
    time.sleep(sleep_time)
    pydirectinput.keyUp(key)

if __name__ == '__main__':
    push_key(sys.argv[1])