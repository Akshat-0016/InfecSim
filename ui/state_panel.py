import tkinter as tk
from tkinter import ttk


class StatePanel:

    def __init__(self, parent):

        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="both",
            expand=True
        )

        # =====================
        # TITLE
        # =====================

        tk.Label(
            self.frame,
            text="STATE STATS",
            font=("Arial", 12, "bold")
        ).pack(
            pady=5
        )

        # =====================
        # NOTEBOOK
        # =====================

        self.notebook = ttk.Notebook(
            self.frame
        )

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        # =====================
        # TABS
        # =====================

        self.overview_tab = tk.Frame(
            self.notebook
        )

        self.government_tab = tk.Frame(
            self.notebook
        )

        self.research_tab = tk.Frame(
            self.notebook
        )

        self.notebook.add(
            self.overview_tab,
            text="Overview"
        )

        self.notebook.add(
            self.government_tab,
            text="Government"
        )

        self.notebook.add(
            self.research_tab,
            text="Research"
        )

        # =====================
        # TAB LABELS
        # =====================

        self.overview_label = tk.Label(
            self.overview_tab,
            justify="left",
            anchor="nw"
        )

        self.overview_label.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.government_label = tk.Label(
            self.government_tab,
            justify="left",
            anchor="nw"
        )

        self.government_label.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.research_label = tk.Label(
            self.research_tab,
            justify="left",
            anchor="nw"
        )

        self.research_label.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.policies_tab = tk.Frame(
            self.notebook
        )

        self.notebook.add(
            self.policies_tab,
            text="Policies"
        )

        self.policies_label = tk.Label(
            self.policies_tab,
            justify="left",
            anchor="nw"
        )

        self.policies_label.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def update_state(self, state):

        healthy, infected, dead = (
            state.get_stats()
        )

        # =====================
        # OVERVIEW TAB
        # =====================

        overview_text = f"""
State: {state.name}
Healthy: {healthy}
Infected: {infected}
Dead: {dead}
GDP: {state.government.economy.gdp:.1f}
"""

        # =====================
        # GOVERNMENT TAB
        # =====================

        government_text = f"""
Public Support: {state.government.public_support:.1f}
Political Capital: {state.government.political_capital:.1f}
Lockdown: {state.government.lockdown_strength:.1f}
Healthcare: {state.healthcare:.1f}
Testing Level: {state.government.testing_level}
Travel Restriction: {state.government.travel_restriction:.1f}
Emergency Powers: {state.government.emergency_powers}
"""

        # =====================
        # RESEARCH TAB
        # =====================

        research_text = f"""
Research Progress: {state.government.research_progress:.1f}
Research Funding: {state.government.research_funding}
Rapid Testing: {state.government.rapid_testing}
Treatment: {state.government.better_treatment}
Vaccine Prototype: {state.government.vaccine_prototype}
Vaccine: {state.government.vaccine_unlocked}
"""
        policies_text = "Active Policies\n\n"
        if state.active_policies:

            for active in state.active_policies:

                name = active.policy.name

                days = active.remaining_days

                policies_text += (
                    f"✓ {name}"
                    f" ({days}d)\n"
                )

        else:

            policies_text += "None"

        self.overview_label.config(
            text=overview_text
        )

        self.government_label.config(
            text=government_text
        )

        self.research_label.config(
            text=research_text
        )

        self.policies_label.config(
            text=policies_text
        )