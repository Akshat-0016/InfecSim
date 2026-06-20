from govt.government import Government


class Authoritarian(Government):

    def __init__(self, ai=None):

        super().__init__(
            "authoritarian",
            ai
        )

        self.fear = 100

        self.repression = 50

        self.lockdown_bonus = 1.4
        self.travel_ban_bonus = 1.4

        self.protest_multiplier = 0.5

        self.emergency_power_bonus = 1.5

        self.economic_resilience = 0.9
        self.support_decay = 0.3

    def check_collapse(self):

        if (
            self.public_support < 5
            and
            self.economy.gdp < 30
        ):

            self.days_unstable += 1

        else:

            self.days_unstable = 0

        if self.days_unstable >= 20:

            self.collapsed = True

            self.lockdown_strength = 0
            self.political_capital = 0