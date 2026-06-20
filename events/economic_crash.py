from events.event import Event

class EconomicCrash(Event):

    def __init__(self):

        super().__init__(
            "Economic Crash"
        )

    def apply(
        self,
        states,
        virus
    ):

        for state in states:

            state.government.economy.gdp *= 0.95

        return "Global Economic Crash"