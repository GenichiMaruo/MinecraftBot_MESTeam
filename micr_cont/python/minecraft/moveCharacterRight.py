from keyControlClass import KeyControl

################################
sleep_time = 0.135
################################

class CharacterRight(KeyControl):
    def __init__(self) -> None:
        super().__init__(key='d', sleep_time=sleep_time)

if __name__ == '__main__':
    CharacterRight().push()