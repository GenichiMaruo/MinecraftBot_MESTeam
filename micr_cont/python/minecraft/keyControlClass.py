import pydirectinput

import time

class KeyControl:
    # コンストラクタ（イニシャライザ）
    def __init__(self, key, sleep_time) -> None:
        if sleep_time == None:
            sleep_time = 0.135
        self.sleep_time = sleep_time
        self.key = key
        self.is_pressed = False

    # key_down() プライベートメソッド 外部参照禁止
    def __key_down(self):
        if self.is_pressed == False:
            pydirectinput.keyDown(self.key)
            self.is_pressed = True
    
    # key_up() プライベートメソッド 外部参照禁止
    def __key_up(self):
        if self.is_pressed == True:
            pydirectinput.keyUp(self.key)
            self.is_pressed = False

    # コントロール関数 True -> KeyDown, False -> KeyUp
    def control(self, input):
        if input == True:
            self.__key_down()
        elif input == False:
            self.__key_up()

    # 1回押し用関数
    def push(self):
        if self.is_pressed == True:
            pydirectinput.keyUp(self.key)
            self.is_pressed = False
        pydirectinput.keyDown(self.key)
        time.sleep(self.sleep_time)
        pydirectinput.keyUp(self.key)
    
    # デストラクタ
    def __del__(self) -> None:
        if self.is_pressed == True:
            pydirectinput.keyUp(self.key)
        print("Delete " + str(self.key))
    

