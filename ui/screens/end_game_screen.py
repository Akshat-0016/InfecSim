import tkinter as tk


class EndScreen:

    def __init__(
        self,
        parent,
        app,
        reason
    ):

        self.frame = tk.Frame(
            parent
        )

        tk.Label(

            self.frame,

            text=reason,

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

            text="Main Menu",

            command=app.show_menu

        ).pack(
            pady=10
        )

        tk.Button(

            self.frame,

            text="Exit",

            command=app.root.destroy

        ).pack(
            pady=10
        )