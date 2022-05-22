import sys
sys.path.append('.')

import init
import initCameraPos
import moveCameraRight
import moveCameraLeft
import moveCameraUp
import moveCameraDown
import clickLeft
import clickRight
import moveCharacterFowerd
import moveCharacterBack
import moveCharacterLeft
import moveCharacterRight
import setTime

init.init()
for i in range(36):
    print(i)
    moveCameraLeft.move_camera_left()
print("OK")
init.init()