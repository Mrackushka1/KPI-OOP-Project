from abc import ABC, abstractmethod
import sqlite3

from logic.game_account import *


class Database(ABC):
    
    def __init__(self):
        self.connection = sqlite3.connect('game_history.db')

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def read(self):
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def delete(self):
        ...

    def __del__(self):
        self.connection.close()


class GameResultsDB(Database):

    def create(self):
        cursor = self.connection.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS game_history (
                    game_id text,
                    player_1_id text,
                    player_2_id text,
                    winner_id text
                );
        """)
        self.connection.commit()
        cursor.close()

    def read(self):
        cursor = self.connection.cursor()
        cursor.execute("""
                SELECT
                    gh.game_id,
                    gh.player_1_id,
                    p1.player_name,
                    gh.player_2_id,
                    p2.player_name,
                    gh.winner_id,
                    p3.player_name
                FROM game_history gh
                LEFT JOIN players p1 ON player_1_id = p1.player_id
                LEFT JOIN players p2 ON player_2_id = p2.player_id
                LEFT JOIN players p3 ON winner_id = p3.player_id
        """)
        return cursor.fetchall()

    def update(self, game_id, player_1_id, player_2_id, winner_id):
        cursor = self.connection.cursor()
        cursor.execute("""
                INSERT INTO game_history VALUES (
                    :game_id,
                    :player_1_id,
                    :player_2_id,
                    :winner_id
                );""", {
                    'game_id' : str(game_id),
                    'player_1_id' : str(player_1_id),
                    'player_2_id' : str(player_2_id),
                    'winner_id' : str(winner_id)
                }
        )
        self.connection.commit()
        cursor.close()

    def delete(self):
        ...


class PlayersDB(Database):

    def create(self):
        cursor = self.connection.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    player_id text,
                    player_name text
                );
        """)
        self.connection.commit()
        cursor.close()

    def read(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM players')
        return cursor.fetchall()

    def update(self, player_id, player_name):
        cursor = self.connection.cursor()
        cursor.execute("""
                INSERT INTO players VALUES (
                    :player_id,
                    :player_name
                );""", {
                    'player_id' : str(player_id),
                    'player_name' : player_name
                }
        )
        self.connection.commit()
        cursor.close()

    def delete(self):
        ...

