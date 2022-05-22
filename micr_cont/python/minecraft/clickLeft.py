import pydirectinput

import time

################################
sleep_time = 0.01
################################

def click_left():
    pydirectinput.mouseDown(button="left")
    time.sleep(sleep_time)
    pydirectinput.mouseUp(button="left")

if __name__ == '__main__':
    click_left()