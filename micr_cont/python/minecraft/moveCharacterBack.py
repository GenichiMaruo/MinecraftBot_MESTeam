from keyControlClass import KeyControl

################################
sleep_time = 0.135
################################

class CharacterBack(KeyControl):
    def __init__(self) -> None:
        super().__init__(key='s', sleep_time=sleep_time)

if __name__ == '__main__':
    CharacterBack().push()