import time

import win32gui
import win32con
import win32api
import pydirectinput

################################
game_name = 'Minecraft: Education Edition'
sleep_time = 0.05
################################

def init_camera_pos():
    init_x , init_y = get_initial_point()
    pydirectinput.moveTo(init_x , init_y)
    time.sleep(sleep_time)
#    print( "init後" , {init_x} , {init_y})

def get_initial_point():
    mcapp = win32gui.FindWindow(None,game_name)
    time.sleep(sleep_time)
    left, top, right, bottom = win32gui.GetWindowRect(mcapp)
#    print({left} , {top} , {right} , {bottom} )
    init_x , init_y = (int)((left + right) / 2 + 0.9) , (int)((top + bottom) /2 + 0.9 + 10)  #10はウィンドウのメニューバーのサイズ
    return init_x , init_y

def get_windows_rect():
    mcapp = win32gui.FindWindow(None,game_name)
    time.sleep(sleep_time)
    left, top, right, bottom = win32gui.GetWindowRect(mcapp)
    return left , top , right , bottom

if __name__ == '__main__':
    init_camera_pos()