import tkinter as tk

class StatePanel:

    def __init__(self, parent):

        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            self.frame,
            text="STATE STATS",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        self.state_name = tk.Label(
            self.frame,
            text="No State Selected"
        )

        self.state_name.pack()

        self.healthy = tk.Label(
            self.frame,
            text="Healthy: 0"
        )

        self.healthy.pack()

        self.infected = tk.Label(
            self.frame,
            text="Infected: 0"
        )

        self.infected.pack()

        self.dead = tk.Label(
            self.frame,
            text="Dead: 0"
        )

        self.dead.pack()

        self.gdp = tk.Label(
            self.frame,
            text="GDP: 0"
        )

        self.gdp.pack()

        self.support = tk.Label(
            self.frame,
            text="Support: 0"
        )

        self.support.pack()

    def update_state(self, state):

        healthy, infected, dead = (
            state.get_stats()
        )

        self.state_name.config(
            text=state.name
        )

        self.healthy.config(
            text=f"Healthy: {healthy}"
        )

        self.infected.config(
            text=f"Infected: {infected}"
        )

        self.dead.config(
            text=f"Dead: {dead}"
        )

        self.gdp.config(
            text=f"GDP: {state.government.economy.gdp:.1f}"
        )

        self.support.config(
            text=f"Support: {state.government.public_support:.1f}"
        )   