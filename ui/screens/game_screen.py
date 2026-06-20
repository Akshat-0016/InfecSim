import tkinter as tk

from ui.main_window import MainWindow


class GameScreen:

    def __init__(
        self,
        parent,
        manager
    ):

        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.window = MainWindow(
            manager,
            parent=self.frame
        )