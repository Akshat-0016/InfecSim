from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from engine.network_map import draw_world

import tkinter as tk


class MapPanel:

    def __init__(self, parent):

        self.node_positions = {}

        self.on_state_selected = None

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

        self.canvas.mpl_connect(
            "button_press_event",
            self.on_click
        )
        self.canvas.mpl_connect(
            "button_press_event",
            self.on_click
        )

    def update_map(
        self,
        states,
        routes
    ):

        self.node_positions = draw_world(
            self.ax,
            states,
            routes
        )

        self.canvas.draw()

    def on_click(self, event):

        if event.xdata is None:
            return

        if event.ydata is None:
            return

        for node, (x, y) in self.node_positions.items():

            distance = (
                (event.xdata - x) ** 2 +
                (event.ydata - y) ** 2
            ) ** 0.5

            if distance < 0.4:

                if self.on_state_selected:
                    self.on_state_selected(node)
                    print(f"clicked: {node}")

                break