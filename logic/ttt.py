from enum import Enum, auto


class Field:

    class field_type(Enum):
        NUMBERED = auto()
        UNNUMBERED = auto()

    class marks(Enum):

        DEFAULT = '   '
        X = ' X '
        O = ' O '

        @staticmethod
        def NUMBER(num):
            return f'{num:^3}'

    FIELD_TYPE: field_type
    mark_list = [marks.DEFAULT] * 9

    def __init__(self, field_type: field_type = field_type.NUMBERED):
        self.field_type = field_type

    def add_mark_to_cell(self, mark: marks, cell_number: int):
        self.rebuild()

    def rebuild(self):
        pass

    ROW = '+---+'
    




class Player:
    pass


class Game:
    pass


def choose_game_mode():
    pass


def main():
    pass


if __name__ == '__main__':
    main()

