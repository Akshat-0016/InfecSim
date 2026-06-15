from govt.government import Government


class Technocracy(Government):

    def __init__(self, ai=None):

        super().__init__(
            "technocracy",
            ai
        )

        self.legitimacy = 100

        self.expert_recommendation = None

        self.research_bonus = 1.5

    def check_collapse(self):

        if self.legitimacy < 20:

            self.collapsed = True

            self.lockdown_strength = 0
            self.political_capital = 0