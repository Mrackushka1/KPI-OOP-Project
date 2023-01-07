from logic.game import *
from logic.game_account import *
from logic.game_stuff import *
from logic.game_saver import *
from logic.db import *


def handler():
    pass


class BaseHandler:
    
    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        self._frame_switcher(
                main_window.current_main_frame,
                new_main_frame,
                main_window.current_navigation_frame,
                new_navigation_frame
        )
        if not new_main_frame.previous_main_frame:
            new_main_frame.previous_main_frame = main_window.current_main_frame
        if not new_navigation_frame.previous_navigation_frame:
            new_navigation_frame.previous_navigation_frame = main_window.current_navigation_frame
        main_window.current_main_frame = new_main_frame
        main_window.current_navigation_frame = new_navigation_frame

    def _frame_switcher(self, old_main_frame, new_main_frame, old_navigation_frame, new_navigation_frame):
        if new_main_frame:
            old_main_frame.grid_forget()
            new_main_frame.grid(row=0, padx=40, pady=(40, 20))
            new_main_frame.grid_propagate(False)
        if new_navigation_frame:
            old_navigation_frame.grid_forget()
            new_navigation_frame.grid(row=1, padx=40, pady=(20, 40))
            new_navigation_frame.grid_propagate(False)


class new_game_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)


class resume_saved_game_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)
        try:
            last_game = instance_loader()
            main_window.current_game = last_game
        except FileNotFoundError:
            main_window.current_main_frame.previous_main_frame.no_saved_game_found()


class game_history_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)
        
        new_main_frame.game_results = self.get_game_results()
        if hasattr(new_main_frame, 'textbox'):
            del new_main_frame.textbox
        new_main_frame.create_textbox()

    def get_game_results(self):
        string_results = []
        for row in GameResultsDB().read():
            GAME_ID, PLAYER_1_ID, PLAYER_1_NAME, PLAYER_2_ID, PLAYER_2_NAME, WINNER_ID, WINNER_NAME = row
            if not WINNER_NAME:
                WINNER_NAME = 'draw'
                WINNER_ID = ''
            string_row = f"{GAME_ID:^37}"\
                         f"{PLAYER_1_ID:^37}"\
                         f"{PLAYER_1_NAME:^14}"\
                         f"{PLAYER_2_ID:^37}"\
                         f"{PLAYER_2_NAME:^14}"\
                         f"{WINNER_ID:^37}"\
                         f"{WINNER_NAME:^14}\n"
            string_results.append(f'{string_row}')
        return string_results


class settings_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)


def exit_button_handler(main_window):
    main_window.destroy()


class game_vs_bot_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)
        GameData.GAME_TYPE = game_type.GAME_VS_BOT


class two_player_game_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)
        GameData.GAME_TYPE = game_type.TWO_PLAYER_GAME


class start_game_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame, player_names, user_field_size):
        try:
            field_size = tuple(map(int, user_field_size))
            self._validate_player_names(player_names)
            self._validate_field_size(field_size)
        except (TypeError, ValueError):
            main_window.current_main_frame.incorrect_input()
            print('return')
            return

        GameData.PLAYER_1 = GameAccount(player_names[0])
        if GameData.GAME_TYPE is game_type.GAME_VS_BOT:
            GameData.PLAYER_2 = GameBot()
        else:
            GameData.PLAYER_2 = GameAccount(player_names[1])

        GameData.FIELD_SIZE = FieldSize(*field_size)
        main_window.game_frame.update_game_field_size(*field_size)

        super().__init__(main_window, new_main_frame, new_navigation_frame)

        current_game = Game(GameData)
        main_window.current_game = current_game
        current_player_name = main_window.current_game.get_current_player_name()
        current_player_mark = main_window.current_game.get_current_player_mark()
        main_window.current_main_frame.change_current_player_label_text(current_player_name)
        
        if isinstance(main_window.current_game._current_player, GameBot):
            current_player = main_window.current_game._current_player
            game_field = main_window.current_game._game_field
            game_field_button_handler(main_window, *current_player.make_move(game_field))
    
    def _validate_player_names(self, player_names):
        for name in player_names:
            if name is not None:
                if not 3 <= len(name) <= 10:
                    print('name error')
                    raise TypeError('Player names must be str and be from 3 to 10 chars in length')

    def _validate_field_size(self, field_size):
        if not 3 <= field_size[0] <= 8:
            raise TypeError('Number of rows must be in [3; 8]')
        if not 3 <= field_size[1] <= 21:
            raise TypeError('Number of rows must be in [3; 21]')


class game_field_button_handler(BaseHandler):

    def __init__(self, main_window, button_row, button_column):
        self._main_window = main_window
        self._current_game = main_window.current_game
        self._game_field = main_window.current_game._game_field
        self._main_frame = self._main_window.current_main_frame

        self._get_current_player_info()
        self._set_new_mark(int(button_row), int(button_column), self._current_player_mark)
        is_winner = self._current_game.is_current_player_winner()
        print(f'{self._current_player.player_name} won: {is_winner}')
        if is_winner:
            self._end_game(self._current_player)
        else:
            self._current_game.change_current_player()
            self._get_current_player_info()

            self._main_frame.change_current_player_label_text(self._current_player_name)

            if self._check_draw():
                self._end_game()
            elif isinstance(self._current_player, GameBot):
                game_field_button_handler(self._main_window, *self._current_player.make_move(self._game_field))

    def _get_current_player_info(self):
        self._current_player = self._current_game._current_player
        self._current_player_name = self._current_game.get_current_player_name()
        self._current_player_mark = self._current_game.get_current_player_mark()

    def _set_new_mark(self, row, column, mark):
        print(f'{self._current_player_name} pressed button {row}:{column}')
        self._current_game.set_new_mark(CellCoords(row, column))
        self._main_window.current_main_frame.set_mark_on_field(row, column, mark)

    def _check_draw(self):
        is_draw = self._current_game._game_field.is_full
        print(f'Is draw: {is_draw}')
        return is_draw

    def _end_game(self, winner=None):
        self._current_game.end_game(winner)
        self._main_window.current_main_frame.disable()
        self._main_window.current_main_frame.declare_game_result(winner)


class back_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        current_main_frame = main_window.current_main_frame
        current_navigation_frame = main_window.current_navigation_frame

        super().__init__(main_window, new_main_frame, new_navigation_frame)

        if hasattr(current_main_frame.previous_main_frame, 'try_to_resume_last_game'):
            current_main_frame.previous_main_frame.try_to_resume_last_game()

        current_main_frame.previous_main_frame = None
        current_navigation_frame.previous_navigation_frame = None

        GameData.PLAYER_1 = None
        GameData.PLAYER_2 = None
        GameData.FIELD_SIZE = None

class save_game_button_handler(BaseHandler):

    def __init__(self, current_game):
        current_game.save()
        instance_saver(current_game)

