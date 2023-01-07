from dataclasses import dataclass
from enum import Enum, auto


class game_type(Enum):

    GAME_VS_BOT = auto()
    TWO_PLAYER_GAME = auto()


class mark(Enum):

    X = '╳'
    O = '◯'


@dataclass
class FieldSize:

    ROWS: int
    COLUMNS: int


@dataclass
class GameData:

    GAME_TYPE = None
    PLAYER_1 = None
    PLAYER_2 = None
    FIELD_SIZE = None


@dataclass
class CellCoords:

    ROW: int
    COLUMN: int

