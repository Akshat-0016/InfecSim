from policies.policy import Policy


class EmergencyPowers(Policy):

    def __init__(self):

        super().__init__(
            "Emergency Powers",
            45
        )

    def apply(self, state):

        state.government.emergency_powers = True

        state.government.public_support -= 15

        state.government.political_capital -= 25

        state.compliance += 0.3

        state.government.public_support -= 1

        state.government.protest_risk += 0.5

    def remove(self, state):

        state.government.public_support -= 20 * state.government.support_decay