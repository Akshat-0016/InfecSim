# this is a simple attempt to replicate plague inc game
import random

class Virus:
    def __init__(self, name, infectivity, mortality, recovery):
        self.name = name
        self.infectivity = infectivity
        self.mortality = mortality
        self.recovery = recovery

    def mutate(self, recov, inf_inc, mort_inc):
        self.recovery += recov
        self.infectivity += inf_inc
        self.mortality += mort_inc

class Human:
    def __init__(self):
        self.status = "healthy"
        self.infected_days = 0

    def infect(self):
        self.status = "infected"

    def recovery(self):
        self.status = "healthy"

    def die(self):
        self.status = "dead"

class State:
    def __init__(self, name):
        self.name = name
        self.population = []
        self.infected_population = []
    
    def daily_updates(self):
        print(f"{State.count_infected(self)}% number of ppl infected.")
        
    def count_infected(self):

        self.infected_population = []

        inf = 0

        for h in self.population:
            if h.status == "infected":
                self.infected_population.append(h)
                inf += 1

        return inf / len(self.population)
    
    def stats(self):

        healthy = 0
        infected = 0
        dead = 0

        for human in self.population:

            if human.status == "healthy":
                healthy += 1

            elif human.status == "infected":
                infected += 1

            elif human.status == "dead":
                dead += 1

        print(f"""
    State : {self.name}

    Healthy : {healthy}
    Infected : {infected}
    Dead : {dead}
    """)
    
class Country:
    def __init__(self, name):
        self.name = name
        self.states = []
    
    def spread_between_states(self):
        inf_states = 0
        for state in self.states:
            if State.count_infected(state) > 0.5:
                inf_states += 1
        if len(self.states) == 0:
            return 0
        
        return inf_states / len(self.states)

class Continent:
    def __init__(self, name):
        self.name = name
        self.countries = []

    def spread_between_countries(self):
        inf_countries = 0
        for country in self.countries:
            if Country.spread_between_states(country) > 0.5:
                inf_countries += 1
        if len(self.countries) == 0:
            return 0
        
        return inf_countries / len(self.countries)

class World:
    def __init__(self):
        self.continents = []
            

class Connection:
    def __init__(self, source, destination, probability):
        self.source = source
        self.destination = destination
        self.probability = probability

def simulate_day(state, virus):

    infected_people = [
        h for h in state.population
        if h.status == "infected"
    ]

    for human in infected_people:
        
        human.infected_days += 1

        for i in range(10):
            if random.random() < virus.infectivity + (human.infected_days/1000) ** 5:

                target = random.choice(state.population)

                if target.status == "healthy":
                    target.infect()

        if random.random() < virus.mortality + (human.infected_days/1000) ** 3:
            human.die()

        elif random.random() < virus.recovery - (human.infected_days/1000) ** 3:
            human.recovery()

def main():
    virus = Virus("zvirus", 0.05, 0.01, 0.05)

    state_1 = State("state_1")

    for i in range(1000):
        state_1.population.append(Human()) 
    
    state_1.population[0].infect()

    for day in range(100):

        simulate_day(state_1, virus)

        print(f"\nDay {day+1}")

        state_1.stats()

if __name__ == "__main__":
    main()