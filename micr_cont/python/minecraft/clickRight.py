import pydirectinput

import time

################################
sleep_time = 1.50
################################

def click_left():
    pydirectinput.mouseDown(button="right")
    time.sleep(sleep_time)
    pydirectinput.mouseUp(button="right")

if __name__ == '__main__':
    click_left()