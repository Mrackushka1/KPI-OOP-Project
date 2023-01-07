from logic.game_stuff import *
from logic.game_account import GameAccount


class GameField:

    def __init__(self, field_size: FieldSize):
        self.field_size = field_size
        self.is_full = False
        self._cells_marked = 0
        self._marks_in_row_to_win = self._get_marks_in_row_to_win()
        self._mark_list = [[None for _ in range(self.field_size.COLUMNS)] for _ in range(self.field_size.ROWS)]
        self._mark_sequence = []

    def __getitem__(self, cell_coords):
        return self._mark_list[cell_coords.ROW][cell_coords.COLUMN]

    def __setitem__(self, cell_coords: CellCoords, player: GameAccount):
        self._mark_sequence.append(cell_coords)
        self._mark_list[cell_coords.ROW][cell_coords.COLUMN] = player
        self._cells_marked += 1
        self.is_full = self._check_if_field_is_full()

    def _check_if_field_is_full(self):
        return self._cells_marked == len(self._mark_list[0]) * len(self._mark_list)

    def _get_marks_in_row_to_win(self):
        min_side = min(self.field_size.ROWS, self.field_size.COLUMNS)
        match min_side:
            case 3:
                return 3
            case 4 | 5 | 6:
                return 4
            case _:
                return 5

    def check_winner(self, player):
        for row in range(self.field_size.ROWS - self._marks_in_row_to_win + 1):
            for column in range(self.field_size.COLUMNS - self._marks_in_row_to_win + 1):
                if self._check_lines(player, row, column) or self._check_diagonals(player, row, column):
                    return True
        return False

    def _check_lines(self, player, offset_row, offset_column):
        for row in range(offset_row, offset_row + self._marks_in_row_to_win):
            row_winner = column_winner = True
            for column in range(offset_column, offset_column + self._marks_in_row_to_win):
                row_winner &= self[CellCoords(row, column)] is player
                column_winner &= self[CellCoords(column + offset_row - offset_column, row - offset_row + offset_column)] is player
            if row_winner or column_winner:
                return True
        return False

    def _check_diagonals(self, player, offset_row, offset_column):
        rising_diagonal_winner = falling_diagonal_winner = True
        for i in range(self._marks_in_row_to_win):
            rising_diagonal_winner &= self[CellCoords(self._marks_in_row_to_win - i - 1 + offset_row, i + offset_column)] is player
            falling_diagonal_winner &= self[CellCoords(i + offset_row, i + offset_column)] is player
        if rising_diagonal_winner or falling_diagonal_winner:
            return True	
        return False 
    
