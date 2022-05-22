from keyControlClass import KeyControl

################################
sleep_time = 0.1
################################

class CharacterJump(KeyControl):
    def __init__(self) -> None:
        super().__init__(key='space', sleep_time=sleep_time)

if __name__ == '__main__':
    CharacterJump().push()