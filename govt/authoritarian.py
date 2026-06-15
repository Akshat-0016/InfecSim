from govt.government import Government


class Authoritarian(Government):

    def __init__(self, ai=None):

        super().__init__(
            "authoritarian",
            ai
        )

        self.fear = 100

        self.repression = 50

        self.research_bonus = 0.9

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