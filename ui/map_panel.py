from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from engine.network_map import draw_world

import tkinter as tk


class MapPanel:

    def __init__(self, parent):

        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.fig = Figure(
            figsize=(8, 4),
            dpi=100
        )

        self.ax = self.fig.add_subplot(
            111
        )

        self.canvas = FigureCanvasTkAgg(
            self.fig,
            master=self.frame
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def update_map(
        self,
        states,
        routes
    ):

        draw_world(
            self.ax,
            states,
            routes
        )

        self.canvas.draw()