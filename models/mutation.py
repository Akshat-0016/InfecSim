class Mutation:

    def __init__(
        self,
        name,
        infectivity_bonus,
        mortality_bonus,
        recovery_penalty
    ):
        self.name = name
        self.infectivity_bonus =  infectivity_bonus
        self.mortality_bonus = mortality_bonus
        self.recovery_penalty = recovery_penalty

    def apply(self, virus):

        virus.infectivity += self.infectivity_bonus

        virus.mortality += self.mortality_bonus

        virus.recovery -= self.recovery_penalty