import tkinter as tk

from policies.travel_ban import TravelBan
from policies.lockdown import Lockdown
from policies.mass_testing import MassTesting
from policies.emergency_power import EmergencyPowers

class ActionPanel:

    def __init__(
        self,
        parent,
        manager
    ):

        self.manager = manager

        self.frame = tk.Frame(parent)

        self.frame.pack()

        control_row = tk.Frame(
            self.frame
        )

        control_row.pack(
            pady=5
        )

        tk.Button(
            self.frame,
            text="Increase Lockdown",
            command=self.lockdown_up
        ).pack(side="left", padx=5)

        tk.Button(
            self.frame,
            text="Decrease Lockdown",
            command=self.lockdown_down
        ).pack(side="left", padx=5)

        tk.Button(
            self.frame,
            text="Fund Research",
            command=self.fund_research
        ).pack(side="left", padx=5)

        tk.Button(
            self.frame,
            text="Healthcare Boost",
            command=self.healthcare_boost
        ).pack(side="left", padx=5)

        tk.Button(
            control_row,
            text="Play",
            command=self.manager.play
        ).pack(side="left", padx=5)

        tk.Button(
            control_row,
            text="Pause",
            command=self.manager.pause
        ).pack(side="left", padx=5)

        tk.Button(
            control_row,
            text="1X",
            command=lambda:
            self.manager.set_speed(1000)
        ).pack(side="left", padx=5)

        tk.Button(
            control_row,
            text="5X",
            command=lambda:
            self.manager.set_speed(200)
        ).pack(side="left", padx=5)

        tk.Button(
            control_row,
            text="20X",
            command=lambda:
            self.manager.set_speed(50)
        ).pack(side="left", padx=5)

        tk.Button(
            self.frame,
            text="Travel Ban",
            command=self.travel_ban
        ).pack(side="left", padx=5)

        tk.Button(
            self.frame,
            text="Mass Testing",
            command=self.mass_testing
        ).pack(
            side="left",
            padx=5
        )

    def lockdown_down(self):

        self.manager.decrease_lockdown()

    def lockdown_up(self):

        self.manager.enact_policy(
            Lockdown()
        )

    def fund_research(self):

        self.manager.fund_research()

    def healthcare_boost(self):

        self.manager.boost_healthcare()

    def travel_ban(self):

        self.manager.enact_policy(
            TravelBan()
        )

    def mass_testing(self):

        self.manager.enact_policy(
            MassTesting()
        )