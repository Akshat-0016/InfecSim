import tkinter as tk

from ui.state_panel import StatePanel
from ui.event_feed import EventFeed
from ui.control import ControlPanel
from ui.map_panel import MapPanel

class MainWindow:

    def __init__(self, manager):

        self.manager = manager

        self.root = tk.Tk()

        self.root.title(
            "Pandemic Government Simulator"
        )

        self.root.geometry(
            "1200x800"
        )

        self.create_layout()

    def create_layout(self):

        # =====================
        # MAP PANEL
        # =====================

        self.map_frame = tk.Frame(
            self.root,
            relief="solid",
            borderwidth=1
        )

        self.map_frame.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.map_panel = MapPanel(
            self.map_frame
        )

        #self.map_panel.draw_test()

        # =====================
        # MIDDLE SECTION
        # =====================

        self.middle_frame = tk.Frame(
            self.root
        )

        self.middle_frame.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        # Stats

        self.stats_frame = tk.Frame(
            self.middle_frame,
            relief="solid",
            borderwidth=1
        )

        self.stats_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        self.state_panel = StatePanel(
            self.stats_frame
        )

        # Events

        self.events_frame = tk.Frame(
            self.middle_frame,
            relief="solid",
            borderwidth=1
        )

        self.events_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=5
        )

        self.events_feed = EventFeed(
            self.events_frame
        )

        # =====================
        # CONTROL PANEL
        # =====================

        self.control_frame = tk.Frame(
            self.root,
            relief="solid",
            borderwidth=1
        )

        self.control_frame.pack(
            fill="x",
            padx=5,
            pady=5
        )

        self.control_panel = ControlPanel(
            self.control_frame,
            self.manager
        )

        # TEMP LABELS

        '''tk.Label(
            self.map_frame,
            text="MAP PANEL"
        ).pack()'''

        '''tk.Label(
            self.stats_frame,
            text="STATE STATS"
        ).pack()'''

        '''tk.Label(
            self.events_frame,
            text="EVENT FEED"
        ).pack()'''

        '''tk.Label(
            self.control_frame,
            text="CONTROLS"
        ).pack()''' 

    def update_loop(self):

        self.manager.tick()

        self.state_panel.update_state(
            self.manager.states[0]
        )

        self.map_panel.update_map(
            self.manager.states,
            self.manager.routes
        )

        self.events_feed.update_events(
            self.manager.event_log.latest()
        )

        self.root.after(
            self.manager.speed,
            self.update_loop
        )

    def run(self):

        self.update_loop()

        self.root.mainloop()
        