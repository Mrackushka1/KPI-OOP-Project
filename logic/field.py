from enum import Enum, auto, member
from dataclasses import dataclass


class field_type(Enum):

    NUMBERED = auto()
    UNNUMBERED = auto()


# VALIDATE
@dataclass
class field_size:

    ROWS: int
    COLUMNS: int


class mark(Enum):

    @staticmethod
    def _create_number_mark(number: int):
        return f'{number:^3}'

    DEFAULT = ' + '
    NUMBER = member(_create_number_mark)
    X = ' X '
    O = ' O '


# VALIDATE
@dataclass
class cell_coords:

    ROW: int
    COLUMN: int


class Field:

    FIELD_TYPE: field_type
    FIELD_SIZE: field_size
    mark_list: list[list[mark]]

    _default_mark: mark

    def __init__(self,
                 field_type: field_type = field_type.NUMBERED,
                 field_size: field_size = field_size(3, 3)):
        self.FIELD_TYPE = field_type
        self._set_default_mark()
        self.FIELD_SIZE = field_size
        self.mark_list = [[self._default_mark for _ in range (self.FIELD_SIZE.COLUMNS)]
                                              for _ in range (self.FIELD_SIZE.ROWS)]
    def set_field_type(self, field_type: field_type = field_type.UNNUMBERED):
        self.field_type = field_type
        self._set_default_mark()

    def add_mark_to_cell(self, mark: mark, cell_coords: cell_coords):
        self.mark_list[cell_coords.ROW][cell_coords.COLUMN] = mark

    def __str__(self):
        return self._create_field_string()

    def _set_default_mark(self):
        if self.FIELD_TYPE == field_type.UNNUMBERED:
            self._default_mark = mark.DEFAULT
        else:
            self._default_mark = mark.NUMBER

    def _create_field_string(self):
        field_string = ''
        row_separator_string = f"{'---+' * (self.FIELD_SIZE.COLUMNS - 1)}---\n"
        for row_number in range(self.FIELD_SIZE.ROWS):
            field_string += self._create_row_string(row_number)
            if row_number != self.FIELD_SIZE.ROWS - 1:
                field_string += row_separator_string
        return field_string

    def _create_row_string(self, row_number):
        row_string = ''
        column_separator_string = '|'
        row_end_string = '\n'
        for column_number in range(self.FIELD_SIZE.COLUMNS):
            row_string += self._get_data_from_field_cell(row_number, column_number)
            if column_number == self.FIELD_SIZE.COLUMNS - 1:
                row_string += row_end_string
            else:
                row_string += column_separator_string
        return row_string

    def _get_data_from_field_cell(self, row_number, column_number):
        match field_cell := self.mark_list[row_number][column_number]:
            case mark.NUMBER:
                cell_number = row_number * self.FIELD_SIZE.COLUMNS + column_number + 1
                cell_data = field_cell.value(cell_number)
            case _:
                cell_data = field_cell.value
        return cell_data

