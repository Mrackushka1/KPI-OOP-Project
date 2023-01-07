import customtkinter as tk

from gui.frames import *


class _MainWindow(tk.CTk):

    def __init__(self):
        super().__init__()
        self._config_window()
        self._create_frames()
        self._place_frames()

        self.current_game = None

    def _config_window(self):
        tk.set_default_color_theme("blue")
        self.title("Tic-Tac-Toe")
        self.minsize(320, 470)
        self.resizable(False, False)

    def _create_frames(self):
        self.game_frame = GameFrame(master=self)
        self.main_menu_frame = MainMenuFrame(master=self)
        self.game_type_menu_frame = GameTypeMenuFrame(master=self)
        self.settings_frame = SettingsFrame(master=self)
        self.game_history_frame = GameHistoryFrame(master=self)
        self.game_vs_bot_frame = GameVSBotMenuFrame(master=self)
        self.two_player_game_frame = TwoPlayerGameMenuFrame(master=self)

        self.empty_navigation_frame = EmptyNavigationFrame(master=self)
        self.back_navigation_frame = BackNavigationFrame(master=self)
        self.back_start_game_navigation_frame = BackStartGameNavigatinFrame(master=self)
        self.back_save_navigation_frame = BackSaveNavigationFrame(master=self)

        self.current_main_frame = self.main_menu_frame
        self.current_navigation_frame = self.empty_navigation_frame

    def _place_frames(self):
        self.current_main_frame.grid(row=0, padx=40, pady=(40, 20))
        self.current_navigation_frame.grid(row=1, padx=40, pady=(20, 40))


def start_gui():
    _MainWindow().mainloop()

