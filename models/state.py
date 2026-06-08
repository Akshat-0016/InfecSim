from models.status import Status
from models.govt import Government

from ai.technocracy_ai import TechnocracyAI
from ai.authoritarian_ai import AuthoritarianAI
from ai.democracy_ai import DemocracyAI


class State:

    def __init__(
        self,
        name,
        population_size,
        government_type="democracy",
        density=1,
        healthcare=1,
        infrastructure=1
    ):

        self.name = name
        self.population = []

        self.population_size = population_size
        self.density = density
        self.healthcare = healthcare
        self.infrastructure = infrastructure

        self.infected_population = []

        if government_type == "democracy":
            self.government = Government(
                ai=DemocracyAI()
            )

        elif government_type == "authoritarian":
            self.government = Government(
                ai=AuthoritarianAI()
            )

        else:
            self.government = Government(
                ai=TechnocracyAI()
            )
    def daily_updates(self):
        print(f"{State.count_infected(self)}% number of ppl infected.")
        
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
