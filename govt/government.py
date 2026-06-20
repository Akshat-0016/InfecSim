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
        self.research_bonus = 1.0
        self.vaccine_unlocked = False

        self.testing_level = 0
        self.travel_restriction = 0
        self.emergency_powers = False

        self.technologies = []

        self.rapid_testing = False
        self.better_treatment = False
        self.vaccine_prototype = False
        self.vaccine_unlocked = False

        self.support_decay = 1.0
        self.protest_multiplier = 1.0

        self.testing_bonus = 1.0
        self.treatment_bonus = 1.0

        self.lockdown_bonus = 1.0
        self.travel_ban_bonus = 1.0

        self.economic_resilience = 1.0

        self.emergency_power_bonus = 1.0
        

    def decide(self, state):

        if self.collapsed:
            return

        action = self.ai.choose_action(
            self,
            state
        )

        self.impose_lockdown(action)

    def impose_lockdown(self, strength):

        self.lockdown_strength = max(
            0.0,
            min(
                1.0,
                self.lockdown_strength + strength
            )
        )

        self.public_support = max(
            0,
            min(
                100,
                self.public_support - strength * 2
            )
        )

        self.political_capital = max(
            0,
            min(
                100,
                self.political_capital - abs(strength) * 5
            )
        )

    def improve_healthcare(self, amount):

        cost = amount * 10

        if self.economy.healthcare_budget >= cost:

            self.healthcare_boost += amount

            self.economy.healthcare_budget -= cost

    def effective_lockdown(self):

        bonus = 1.0

        if self.emergency_powers:
            bonus = 1.3

        return (
            self.lockdown_strength *
            self.compliance *
            bonus *
            self.lockdown_bonus
        )

    def daily_update(self):

        self.fatigue += self.lockdown_strength

        self.compliance = max(
            0.3,
            1 - self.fatigue * 0.001
        )

        self.public_support -= (
            self.lockdown_strength
            * 0.1
            * self.support_decay
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
            0.05
        )

        self.check_technologies()

        if self.research_progress >= 100:
            self.vaccine_unlocked = True

    def check_technologies(self):

        if (
            self.research_progress >= 20
            and
            not self.rapid_testing
        ):

            self.rapid_testing = True

        if (
            self.research_progress >= 40
            and
            not self.better_treatment
        ):

            self.better_treatment = True

        if (
            self.research_progress >= 70
            and
            not self.vaccine_prototype
        ):

            self.vaccine_prototype = True

        if (
            self.research_progress >= 100
            and
            not self.vaccine_unlocked
        ):

            self.vaccine_unlocked = True

    def check_collapse(self):
        pass

    def is_collapsed(self):
        return self.collapsed