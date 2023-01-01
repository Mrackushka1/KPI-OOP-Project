import customtkinter as tk
from random import choice
# import os
# from PIL import Image

from . import handlers


class MenuFrame(tk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.main_window = master
        self.previous_main_frame = None
        self._frame_width = 240
        self._frame_height = 310
        self._frame_color = 'transparent'
        self._label_font = tk.CTkFont(size=20)
        self._button_width = 160
        self._button_height = 40
        self._entry_width = 160
        self._entry_height = 40
        self._button_pady = 5

        # image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '.')
        # self.window_image = tk.CTkImage(Image.open(os.path.join(image_path, 'background.png')), size=(26, 26))
        # self.configure(image=self.window_image)
        
        self._set_configs()

    def _set_configs(self):
        self.configure(width=self._frame_width, height=self._frame_height, fg_color=self._frame_color)
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

    def _create_label(self, label_text):
        welcome_label = tk.CTkLabel(
                self,
                font=self._label_font,
                text=label_text
        ) 
        welcome_label.grid(pady=20)

    def _create_button(self, button_text, button_handler):
        button = tk.CTkButton(
                self,
                width=self._button_width,
                height=self._button_height,
                text=button_text,
                command=button_handler
        )
        button.grid(pady=self._button_pady)
        return button

    def _create_entry(self, entry_text):
        button = tk.CTkEntry(
                self,
                width=self._entry_width,
                height=self._entry_height,
                placeholder_text=entry_text,
        )
        button.grid(pady=self._button_pady)
        return button


class MainMenuFrame(MenuFrame):

    def __init__(self, master):
        super().__init__(master)

        self.welcome_label = self._create_label('Welcome to Tic-Tac-Toe')
        self.new_game_button = self._create_button(
                'New game',
                lambda: handlers.new_game_button_handler(
                    self.main_window,
                    self.main_window.game_type_menu_frame,
                    self.main_window.back_navigation_frame
                )
        )
        self.game_history_button = self._create_button(
                'Game history', 
                lambda: handlers.game_history_button_handler(
                    self.main_window,
                    self.main_window.game_history_frame,
                    self.main_window.back_navigation_frame
                )
        )
        self.settings_button = self._create_button(
                'Settings',
                lambda: handlers.settings_button_handler(
                    self.main_window,
                    self.main_window.settings_frame,
                    self.main_window.back_navigation_frame
                )
        )
        self.exit_button = self._create_button('Exit game', lambda: handlers.exit_button_handler(self.main_window))


class GameHistoryFrame(MenuFrame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.CTkLabel(self, text='Not Implemented')
        label.grid()


class SettingsFrame(MenuFrame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.CTkLabel(self, text='Not Implemented')
        label.grid()


class GameTypeMenuFrame(MenuFrame):

    def __init__(self, master):
        super().__init__(master)

        self.game_type_label = self._create_label('Choose game type')
        self.game_vs_bot = self._create_button(
                'VS bot',
                lambda: handlers.game_vs_bot_button_handler(
                    self.main_window,
                    self.main_window.game_vs_bot_frame,
                    self.main_window.back_start_game_navigation_frame
                )
        )
        self.two_player_game = self._create_button(
                'Two players',
                lambda: handlers.game_vs_bot_button_handler(
                    self.main_window,
                    self.main_window.two_player_game_frame,
                    self.main_window.back_start_game_navigation_frame
                )
        )

        
class GameVSBotMenuFrame(MenuFrame):

    def __init__(self, master):
        super().__init__(master)

        self.game_settings_label = self._create_label('Game Settings')
        self.player_name_entry = self._create_entry('Player name')
        self.player_name_entry = self._create_entry('Number of rows')
        self.player_name_entry = self._create_entry('Number of columns')


class TwoPlayerGameMenuFrame(MenuFrame):

    def __init__(self, master):
        super().__init__(master)

        self.game_settings_label = self._create_label('Game Settings')
        self.player_name_entry = self._create_entry('Player 1 name')
        self.player_name_entry = self._create_entry('Player 2 name')


class NavigationFrame(tk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.main_window = master
        self.previous_navigation_frame = None
        self._frame_color = 'transparent'
        self._buttons_font = tk.CTkFont()

        self._set_configs()
        self._create_button_templates()

    def _set_configs(self):
        self.configure(width=240, height=40, fg_color=self._frame_color)
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _create_button_templates(self):
        left_empty_frame = tk.CTkFrame(self, height=20, width=80, fg_color=self._frame_color)
        left_empty_frame.grid(row=0, column=0, padx=(0, 40))
        right_empty_frame = tk.CTkFrame(self, height=20, width=80, fg_color=self._frame_color)
        right_empty_frame.grid(row=0, column=1, padx=(40, 0))

    def _create_left_button(self, button_text, button_handler):
        left_button = tk.CTkButton(
                self,
                height=25,
                width=100,
                text=button_text,
                font=self._buttons_font,
                command=button_handler
        )
        left_button.grid(row=0, column=0, sticky='sw')
        return left_button

    def _create_right_button(self, button_text, button_handler):
        right_button = tk.CTkButton(
                self,
                height=25,
                width=100,
                text=button_text,
                font=self._buttons_font,
                command=button_handler
        )
        right_button.grid(row=0, column=1, sticky='se')
        return right_button


class EmptyNavigationFrame(NavigationFrame):
    pass


class BackNavigationFrame(NavigationFrame):

    def __init__(self, master):
        super().__init__(master)

        self._create_left_button(
                'Back',
                lambda: handlers.back_button_handler(
                    self.main_window,
                    self.main_window.current_main_frame.previous_main_frame,
                    self.main_window.current_navigation_frame.previous_navigation_frame
                )
        )


class BackStartGameNavigatinFrame(NavigationFrame):

    def __init__(self, master):
        super().__init__(master)

        self._create_left_button(
                'Back',
                lambda: handlers.back_button_handler(
                    self.main_window,
                    self.main_window.current_main_frame.previous_main_frame,
                    self.main_window.current_navigation_frame.previous_navigation_frame
                )
        )
        self._create_right_button(
                'Start game',
                lambda: handlers.start_game_button_handler(
                    self.main_window,
                    self.main_window.game_frame,
                    self.main_window.back_save_navigation_frame
                )
        )

class BackSaveNavigationFrame(NavigationFrame):

    def __init__(self, master):
        super().__init__(master)

        self._create_left_button(
                'Back',
                lambda: handlers.back_button_handler(
                    self.main_window,
                    self.main_window.current_main_frame.previous_main_frame,
                    self.main_window.current_navigation_frame.previous_navigation_frame
                )
        )
        self._create_right_button(
                'Save game',
                handlers.handler
        )


class GameFrame(tk.CTkFrame):
    
    def __init__(self, master, field_rows=3, field_columns=3):
        super().__init__(master)

        self.previous_main_frame = None

        self._frame_color = 'transparent'
        self._field_rows = field_rows
        self._field_columns = field_columns

        self._create_game_field_frame()
        self._create_game_header_frame()

        game_field_frame_width, game_field_frame_height = self._game_field_frame.get_game_field_frame_size()
        game_header_frame_height = self._game_header_frame.get_game_header_frame_height()
        self._frame_width = game_field_frame_width
        self._frame_height = game_field_frame_height + game_header_frame_height + 40
        if self._frame_height < 310:
            self._frame_height = 310

        self._set_configs()

    def _set_configs(self):
        self.configure(width=self._frame_width, height=self._frame_height, fg_color=self._frame_color)
        self.grid_propagate(False)

    def _create_game_header_frame(self):
        self._game_header_frame = GameHeaderFrame(self)
        self._game_header_frame.grid(row=0, column=0, pady=(0, 20))

    def _create_game_field_frame(self):
        self._game_field_frame = GameFieldFrame(self, self._field_rows, self._field_columns)
        self._game_field_frame.grid(row=1, column=0, pady=(20, 0))


class GameHeaderFrame(tk.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master)

        self._frame_width = 100
        self._frame_height = 60
        self._frame_color = 'transparent'
        self._current_player_name_label_color = '#008000'
        self._current_player_name_label_font = tk.CTkFont(size=30, weight='bold')
        self._current_player_label_color = ('#3B8ED0', '#1F6AA5')
        self._current_player_label_font = tk.CTkFont(size=30, weight='bold')

        self._set_configs()

        self._current_player_name_label = tk.CTkLabel(
                self,
                text='Player',
                text_color=self._current_player_name_label_color,
                font=self._current_player_name_label_font
        )
        self._current_player_label = tk.CTkLabel(
                self,
                text='\'s turn',
                text_color=self._current_player_label_color,
                font=self._current_player_label_font
        )
        self._current_player_name_label.grid(row=0, column=0)
        self._current_player_label.grid(row=0, column=1)

    def get_game_header_frame_height(self):
        return self._frame_height

    def _set_configs(self):
        self.configure(
                width=self._frame_width,
                height=self._frame_height,
                fg_color = self._frame_color
        )


class GameFieldFrame(tk.CTkFrame):

    def __init__(self, master, field_rows, field_columns):
        super().__init__(master)

        self._frame_color = 'transparent'
        self._field_rows = field_rows
        self._field_columns = field_columns
        self._button_width = 60
        self._button_height = 60
        self._button_color = 'transparent'
        self._button_text_color = ('#3B8ED0', '#1F6AA5') 
        self._button_font = tk.CTkFont(size=40, weight='bold')
        self._separator_thickness = 4
        self._separator_color = ('#3B8ED0', '#1F6AA5')
        self._field_width = self._field_columns * (self._button_width + self._separator_thickness) - self._separator_thickness
        self._field_height = self._field_rows * (self._button_height + self._separator_thickness) - self._separator_thickness
        self.buttons = []

        self._set_configs()
        self._create_game_field_widgets()

    def get_game_field_frame_size(self):
        return self._field_width, self._field_height

    def _set_configs(self):
        self.configure(width=self._field_width, height=self._field_height, fg_color=self._frame_color)
        self.grid_propagate(False)

    def _create_game_field_widgets(self):
        for row in range(self._field_rows):
            for column in range(self._field_columns):
                button = self._create_field_button(row, column)
                self.buttons.append(button)
                self._create_row_separator(row, column)
                self._create_column_separator(row, column)

    def _create_field_button(self, row, column):
        button = tk.CTkButton(
                self,
                width=self._button_width,
                height=self._button_height,
                text=f"{choice(['╳', '◯'])}",
                fg_color=self._button_color,
                text_color=self._button_text_color,
                font=self._button_font
        )
        button.grid(row=row * 2, column=column * 2)
        return button

    def _create_row_separator(self, row, column):
        if row < self._field_rows - 1:
            row_separator = tk.CTkFrame(
                    self,
                    width=self._button_width,
                    height=self._separator_thickness,
                    fg_color=self._separator_color
            )
            row_separator.grid(row=2 * row + 1, column=2 * column)

    def _create_column_separator(self, row, column):
        if column < self._field_columns - 1:
            column_separator = tk.CTkFrame(
                    self,
                    width=self._separator_thickness,
                    height=self._button_height,
                    fg_color=self._separator_color
            )
            column_separator.grid(row=2 * row, column=2 * column + 1)
