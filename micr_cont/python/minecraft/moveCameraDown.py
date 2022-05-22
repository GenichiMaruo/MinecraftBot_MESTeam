from keyControlClass import KeyControl

################################
sleep_time = 0.05
################################
class CameraDown(KeyControl):
    def __init__(self) -> None:
        super().__init__(key='down', sleep_time=sleep_time)

if __name__ == '__main__':
    CameraDown().push()