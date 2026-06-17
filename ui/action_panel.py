import tkinter as tk

class ActionPanel:

    def __init__(
        self,
        parent,
        manager
    ):

        self.manager = manager

        self.frame = tk.Frame(parent)

        self.frame.pack()

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
    def lockdown_up(self):

        player = self.get_player()

        if (
            player.government.political_capital
            < 10
        ):
            return

        player.government.political_capital -= 10

        player.government.lockdown_strength = min(
            1.0,
            player.government.lockdown_strength + 0.1
        )

        self.manager.event_log.add(
            f"Day {self.manager.day}: Lockdown Increased"
        )

    def lockdown_down(self):

        player = self.get_player()

        if (
            player.government.political_capital
            < 10
        ):
            return

        player.government.lockdown_strength = max(
            0,
            player.government.lockdown_strength - 0.1
        )

        self.manager.event_log.add(
            f"Day {self.manager.day}: Lockdown Decreased"
        )

    def fund_research(self):

        player = self.get_player()

        if player.government.political_capital < 15:
            return

        player.government.political_capital -= 15

        player.government.research_funding += 5

        self.manager.event_log.add(
            f"Day {self.manager.day}: Research Funded"
        )

    def healthcare_boost(self):

        player = self.get_player()

        if player.government.political_capital < 20:
            return

        player.government.political_capital -= 20

        player.government.healthcare_boost += 0.1

        self.manager.event_log.add(
            f"Day {self.manager.day}: Healthcare Boost"
        )

    def get_player(self):

        for state in self.manager.states:

            if state.is_player:
                return state