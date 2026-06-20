from models.status import Status
from govt.democracy import Democracy
from govt.technocracy import Technocracy
from govt.authoritarian import Authoritarian

from ai.technocracy_ai import TechnocracyAI
from ai.authoritarian_ai import AuthoritarianAI
from ai.democracy_ai import DemocracyAI

from govt.democracy import Democracy


class State:

    def __init__(
        self,
        name,
        population_size,
        government_type="democracy",
        density=1,
        healthcare=1,
        infrastructure=1,
        is_player=False
    ):

        self.name = name
        self.population = []

        self.infected_population = []

        self.population_size = population_size
        self.density = density
        self.healthcare = healthcare
        self.infrastructure = infrastructure

        self.recovery_bonus = 1.0
        self.infection_resistance = 1.0

        self.is_player=is_player
        self.active_policies = []    

        if government_type == "democracy":

            self.government = Democracy(
                ai=DemocracyAI()
            )

        elif government_type == "authoritarian":

            self.government = Authoritarian(
                ai=AuthoritarianAI()
            )

        else:

            self.government = Technocracy(
                ai=TechnocracyAI()
            )


    def daily_updates(self):
        print(
        f"{self.count_infected() * 100:.1f}% infected"
    )
        
    def count_infected(self):

        self.infected_population = []

        inf = 0

        for h in self.population:
            if h.status == Status.INFECTED:
                self.infected_population.append(h)
                inf += 1

        return inf / len(self.population)
    
    def stats(self):

        healthy = 0
        infected = 0
        dead = 0

        for human in self.population:

            if human.status == Status.HEALTHY:
                healthy += 1

            elif human.status == Status.INFECTED:
                infected += 1

            elif human.status == Status.DEAD:
                dead += 1

        print(f"""
State : {self.name}

Healthy : {healthy}
Infected : {infected}
Dead : {dead}

Lockdown : {self.government.lockdown_strength:.2f}
Support : {self.government.public_support:.2f}
GDP : {self.government.economy.gdp:.2f}
""")
    
    def get_stats(self):

        healthy = 0
        infected = 0
        dead = 0

        for human in self.population:

            if human.status == Status.HEALTHY:
                healthy += 1

            elif human.status == Status.INFECTED:
                infected += 1

            elif human.status == Status.DEAD:
                dead += 1

        return healthy, infected, dead
    
    def infected_count(self):

        _, infected, _ = self.get_stats()

        return infected
    
    def dead_count(self):

        _, _, dead = self.get_stats()

        return dead