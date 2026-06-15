import tkinter as tk

class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Pandemic Government Simulator"
        )

        self.root.geometry(
            "1200x800"
        )

    def run(self):

        self.root.mainloop()