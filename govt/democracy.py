from govt.government import Government


class Democracy(Government):

    def __init__(self, ai=None):

        super().__init__(
            "democracy",
            ai
        )

        self.research_bonus = 1.1

        self.support_decay = 0.8
        self.protest_multiplier = 1.5

        self.testing_bonus = 1.1
        self.economic_resilience = 1.1

    def check_collapse(self):

        if self.public_support < 15:

            self.days_unstable += 1

        else:

            self.days_unstable = 0

        if self.days_unstable >= 15:

            if not self.collapsed:

                if self.days_unstable >= 15:

                    self.collapsed = True

                    self.lockdown_strength = 0
                    self.political_capital = 0

                    print(
                        "democracy has collapsed"
                    )