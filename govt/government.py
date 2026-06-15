from models.economy import Economy


class Government:

    def __init__(self, government_type, ai=None):

        self.government_type = government_type
        self.ai = ai

        # Common stats

        self.lockdown_strength = 0.0
        self.healthcare_boost = 1.0

        self.public_support = 100.0

        self.fatigue = 0.0
        self.compliance = 1.0

        self.corruption = 0.0

        self.political_capital = 100.0

        self.economy = Economy()

        self.total_deaths_seen = 0

        self.days_unstable = 0
        self.collapsed = False

        # Research

        self.research_progress = 0.0
        self.research_funding = 10
        self.vaccine_unlocked = False

    def decide(self, state):

        if self.collapsed:
            return

        action = self.ai.choose_action(
            self,
            state
        )

        self.impose_lockdown(action)

    def impose_lockdown(self, strength):

        self.lockdown_strength = strength

        self.public_support -= (
            strength * 2
        )

        self.political_capital -= (
            strength * 5
        )

        self.public_support = max(
            0,
            min(100, self.public_support)
        )

    def improve_healthcare(self, amount):

        cost = amount * 10

        if self.economy.healthcare_budget >= cost:

            self.healthcare_boost += amount

            self.economy.healthcare_budget -= cost

    def effective_lockdown(self):

        return (
            self.lockdown_strength *
            self.compliance
        )

    def daily_update(self):

        self.fatigue += self.lockdown_strength

        self.compliance = max(
            0.3,
            1 - self.fatigue * 0.001
        )

        self.public_support -= (
            self.lockdown_strength * 0.1
        )

        self.public_support = max(
            0,
            min(100, self.public_support)
        )

        self.political_capital = min(
            100,
            self.political_capital + 0.2
        )

        self.economy.daily_update(
            self.lockdown_strength
        )

        self.update_research()

        self.check_collapse()

    def update_research(self):

        self.research_progress += (
            self.research_funding *
            self.research_bonus *
            0.01
        )

        if self.research_progress >= 100:
            self.vaccine_unlocked = True

    def check_collapse(self):
        pass

    def is_collapsed(self):
        return self.collapsed