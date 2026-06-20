from policies.policy import Policy


class Lockdown(Policy):

    def __init__(self):

        super().__init__(
            "Lockdown",
            15
        )

    def apply(self, state):

        state.government.lockdown_strength += 0.3

    def daily_effect(self, state):

        state.government.economy.gdp -= 0.3

        state.government.public_support -= 0.2

    def remove(self, state):

        state.government.lockdown_strength -= 0.3

        state.government.lockdown_strength = max(
            0,
            state.government.lockdown_strength
        )