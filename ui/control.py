import tkinter as tk

class ControlPanel:

    def __init__(self, parent, manager):

        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            self.frame,
            text="CONTROLS PANEL",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        self.play = tk.Button(
            self.frame,
            text="play",
            command=manager.play
        )

        self.play.pack(side="left", padx=5) 

        self.pause = tk.Button(
            self.frame,
            text="pause",
            command=manager.pause
        )

        self.pause.pack(side="left", padx=5) 

        self.normal_speed = tk.Button(
            self.frame,
            text="1X",
            command=lambda:
            manager.set_speed(1000)
        )

        self.normal_speed.pack(side="left", padx=5) 
        
        self.sped_up_5 = tk.Button(
            self.frame,
            text="5X",
            command=lambda:
            manager.set_speed(200)
        )

        self.sped_up_5.pack(side="left", padx=5) 

        self.sped_up_20 = tk.Button(
            self.frame,
            text="20X",
            command=lambda:
            manager.set_speed(50)
        )

        self.sped_up_20.pack(side="left", padx=5) 