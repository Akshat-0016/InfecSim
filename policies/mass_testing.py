from policies.policy import Policy


class MassTesting(Policy):

    def __init__(self):

        super().__init__(
            "Mass Testing",
            20
        )

    def apply(self, state):

        state.government.testing_level += 1

        state.recovery_bonus += 0.1

        state.government.political_capital -= 10

    def daily_effect(self, state):

        state.government.political_capital -= 0.2

    def remove(self, state):

        state.government.testing_level -= 1

        state.recovery_bonus -= 0.1