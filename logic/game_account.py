from uuid import uuid4
from random import choice
from logic.game_stuff import *


class GameAccount:

    def __init__(self, player_name):
        self._account_id = uuid4()
        self.player_name = player_name
        self.player_mark: mark | None = None


class GameBot(GameAccount):

    def __init__(self):
        self._account_id = uuid4()
        self.player_name = 'Bot'
        self.player_mark: mark | None = None

    def make_move(self, game_field):
        free_nodes = self._find_free_nodes(game_field)
        random_node = choice(free_nodes)
        return random_node.ROW, random_node.COLUMN

    def _find_free_nodes(self, game_field):
        free_nodes = []
        for row in range(game_field.field_size.ROWS):
            for column in range(game_field.field_size.COLUMNS):
                if not game_field[CellCoords(row, column)]:
                    free_nodes.append(CellCoords(row, column))
        return free_nodes

