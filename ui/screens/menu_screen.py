import tkinter as tk


class MenuScreen:

    def __init__(
        self,
        parent,
        app
    ):

        self.frame = tk.Frame(
            parent
        )

        tk.Label(
            self.frame,
            text="INFECSIM",
            font=(
                "Arial",
                24,
                "bold"
            )
        ).pack(
            pady=20
        )

        tk.Button(
            self.frame,
            text="New Game",
            width=20,
            command=app.show_new_game
        ).pack(
            pady=10
        )

        tk.Button(
            self.frame,
            text="Exit",
            width=20,
            command=app.root.destroy
        ).pack(
            pady=10
        )