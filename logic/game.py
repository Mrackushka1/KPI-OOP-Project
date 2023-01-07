from uuid import uuid4
from random import choice

from logic.game_field import *
from logic.game_stuff import *
from logic.db import PlayersDB, GameResultsDB


class Game:

    def __init__(self, game_data: GameData):
        print('Game started')
        self._game_id = uuid4()
        self._game_type = game_data.GAME_TYPE
        self._player_1 = GameData.PLAYER_1
        self._player_2 = game_data.PLAYER_2
        self._field_size = game_data.FIELD_SIZE
        self._game_field = GameField(self._field_size)
        self._first_player = self._current_player = self._choose_first_player()
        self._winner = None

    def set_new_mark(self, cell_coords: CellCoords):
        self._game_field[cell_coords] = self._current_player

    def is_current_player_winner(self):
        if self._game_field.check_winner(self._current_player):
            self._winner = self._current_player
            return True
        return False

    def change_current_player(self):
        if self._current_player is self._player_1:
            self._current_player = self._player_2
        else:
            self._current_player = self._player_1

    def get_current_player_name(self):
        return self._current_player.player_name

    def get_current_player_mark(self):
        return self._current_player.player_mark.value

    def end_game(self, winner=None):
        if winner:
            print(f'Game ended, winner - {winner.player_name}')
        else:
            print('Game ended, in a draw.')
        if winner is None:
            self.save()
        self.save_result()

    def save(self):
        print('Game saved')

    def save_result(self):
        for player in (self._player_1, self._player_2):
            players_db = PlayersDB()
            players_db.create()
            players_db.update(player._account_id, player.player_name)
            del players_db
        game_results_db = GameResultsDB()
        game_results_db.create()
        game_results_db.update(
                self._game_id,
                self._player_1._account_id,
                self._player_2._account_id,
                self._winner._account_id
        )
        del game_results_db
        print('Game result saved')

        game_results_db = GameResultsDB()
        for row in game_results_db.read():
            print(row)
        del game_results_db

    def _choose_first_player(self):
        players = [self._player_1, self._player_2]
        first_player = choice(players)
        first_player.player_mark = mark.X
        for player in players:
            if not player.player_mark:
                player.player_mark = mark.O
        return first_player
    
