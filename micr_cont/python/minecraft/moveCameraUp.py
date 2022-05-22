from keyControlClass import KeyControl

################################
sleep_time = 0.05
################################

class CameraUp(KeyControl):
    def __init__(self) -> None:
        super().__init__(key='up', sleep_time=sleep_time)

if __name__ == '__main__':
    CameraUp().push()