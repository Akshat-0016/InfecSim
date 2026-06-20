import tkinter as tk
from tkinter import ttk


class NewGameScreen:

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
            text="States"
        ).pack()

        self.states_var = tk.IntVar(
            value=5
        )

        self.difficulty_var = tk.StringVar(
            value="medium"
        )

        tk.Label(
            self.frame,
            text="Difficulty"
        ).pack()

        ttk.Combobox(
            self.frame,
            textvariable=
            self.difficulty_var,

            values=[
                "easy",
                "medium",
                "hard"
            ],

            state="readonly"
        ).pack()

        self.gov_var = tk.StringVar(
            value="democracy"
        )

        tk.Label(
            self.frame,
            text="Government"
        ).pack()

        ttk.Combobox(
            self.frame,
            textvariable=
            self.gov_var,

            values=[
                "democracy",
                "technocracy",
                "authoritarian"
            ],

            state="readonly"
        ).pack()

        tk.Spinbox(
            self.frame,
            from_=5,
            to=25,
            textvariable=
            self.states_var
        ).pack()

        tk.Button(
            self.frame,

            text="Start",

            command=lambda:
            app.start_game(
                self.states_var.get(),

                self.difficulty_var.get(),

                self.gov_var.get()
            )
        ).pack()
