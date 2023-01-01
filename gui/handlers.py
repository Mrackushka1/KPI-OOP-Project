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


class game_history_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)


class settings_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)


def exit_button_handler(main_window):
    main_window.destroy()


class game_vs_bot_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)


class two_player_game_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)


class start_game_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        super().__init__(main_window, new_main_frame, new_navigation_frame)


class back_button_handler(BaseHandler):

    def __init__(self, main_window, new_main_frame, new_navigation_frame):
        current_main_frame = main_window.current_main_frame
        current_navigation_frame = main_window.current_navigation_frame

        super().__init__(main_window, new_main_frame, new_navigation_frame)

        current_main_frame.previous_main_frame = None
        current_navigation_frame.previous_navigation_frame = None

