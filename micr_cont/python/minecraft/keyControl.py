import sys
sys.path.append('.')
sys.path.append('./python/minecraft/')

from time import sleep
from moveCameraDown import CameraDown
from moveCameraLeft import CameraLeft
from moveCameraRight import CameraRight
from moveCameraUp import CameraUp
from moveCharacterBack import CharacterBack
from moveCharacterFowerd import CharacterFowerd
from moveCharacterJump import CharacterJump
from moveCharacterLeft import CharacterLeft
from moveCharacterRight import CharacterRight


class KeyController:
    def __init__(self) -> None:
        self.fps = 25.0
        self.camera = (
            CameraDown(),
            CameraLeft(),
            CameraRight(),
            CameraUp()
        )
        self.character = (
            CharacterBack(),
            CharacterFowerd(),
            CharacterJump(),
            CharacterLeft(),
            CharacterRight()
        )

    def get_file_data(self):
        f = open('control.txt', 'r', encoding='UTF-8')
        data = f.read()
        f.close()
        lines = data.split('\n')
        if len(lines) < 4:
            return (0, 0), (0, 0)
        else:
            return (int(lines[0]), int(lines[1])), (int(lines[2]), int(lines[3]))

    def main(self):
        camera_dir_old = (0, 0)
        character_dir_old = (0, 0)
        try:
            while True:
                camera_dir, character_dir = self.get_file_data()
                if camera_dir_old != camera_dir:
                    camera_dir_old = camera_dir
                    if camera_dir[0] == 1:
                        self.camera[2].control(True)
                        self.camera[1].control(False)
                    elif camera_dir[0] == -1:
                        self.camera[2].control(False)
                        self.camera[1].control(True)
                    else:
                        self.camera[2].control(False)
                        self.camera[1].control(False)
                        
                    if camera_dir[1] == 1:
                        self.camera[0].control(False)
                        self.camera[3].control(True)
                    elif camera_dir[1] == -1:
                        self.camera[0].control(True)
                        self.camera[3].control(False)
                    else:
                        self.camera[0].control(False)
                        self.camera[3].control(False)

                if character_dir_old != character_dir:
                    character_dir_old = character_dir
                    if character_dir[0] == 1:
                        self.character[1].control(True)
                        self.character[0].control(False)
                    elif character_dir[0] == -1:
                        self.character[1].control(False)
                        self.character[0].control(True)
                    else:
                        self.character[1].control(False)
                        self.character[0].control(False)
                        
                    if character_dir[1] == 1:
                        self.character[4].control(True)
                        self.character[3].control(False)
                    elif character_dir[1] == -1:
                        self.character[4].control(False)
                        self.character[3].control(True)
                    else:
                        self.character[4].control(False)
                        self.character[3].control(False)

                if camera_dir_old != camera_dir and character_dir_old != character_dir:
                    sleep(1.0/self.fps)
        except KeyboardInterrupt:
            print("KeyController Stopped")

    def __end_processing(self):
        f = open('control.txt', 'w', encoding='UTF-8')
        for i in range(4):
            f.write(str(0)+'\n')
        f.close()

    def __del__(self) -> None:
        del self.camera
        del self.character
        self.__end_processing()
        print("All Deleted !")
         

if __name__ == '__main__':
    KeyController().main()