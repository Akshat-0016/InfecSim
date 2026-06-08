from models.economy import Economy

from ai.democracy_ai import DemocracyAI


class Government:

    def __init__(
        self,
        ai=None
    ):

        self.lockdown_strength = 0.0

        self.healthcare_boost = 1.0

        self.public_support = 100.0

        self.fatigue = 0.0

        self.compliance = 1.0

        self.economy = Economy()

        self.ai = ai or DemocracyAI()

    def decide(self, state):

        action = self.ai.choose_action(
            self,
            state
        )

        self.impose_lockdown(action)

        infected_ratio = state.count_infected()

        if infected_ratio > 0.50:

            self.improve_healthcare(
                0.5
            )

        elif infected_ratio > 0.25:

            self.improve_healthcare(
                0.2
            )

        self.healthcare_boost = min(
            3.0,
            self.healthcare_boost
        )
    def impose_lockdown(
        self,
        strength
    ):

        self.lockdown_strength = strength

        self.public_support -= (
            strength * 2
        )

    def improve_healthcare(
        self,
        amount
    ):

        cost = amount * 10

        if (
            self.economy.healthcare_budget
            >= cost
        ):

            self.healthcare_boost += amount

            self.economy.healthcare_budget -= cost

    def effective_lockdown(self):

        return (
            self.lockdown_strength
            * self.compliance
        )

    def daily_update(self):

        self.fatigue += (
            self.lockdown_strength
        )

        self.compliance = max(
            0.3,
            1 - self.fatigue * 0.001
        )

        self.public_support -= (
            self.lockdown_strength
            * 0.1
        )

        self.economy.daily_update(
            self.lockdown_strength
        )