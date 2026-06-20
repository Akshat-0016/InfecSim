from policies.policy import Policy


class TravelBan(Policy):

    def __init__(self):

        super().__init__(
            "Travel Ban",
            20
        )

    def apply(self, state):

        state.government.travel_restriction += 0.5

    def daily_effect(self, state):

        state.government.economy.gdp -= 0.2

        state.government.public_support -= 0.1

    def remove(self, state):

        state.government.travel_restriction -= 0.5