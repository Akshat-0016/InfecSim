import random
from models.status import Status
from data.mutation import MUTATIONS
from engine.travel import travel_spread

def simulate_day(state, virus):

    state.government.decide(state)

    state.government.daily_update()

    print(
    f"{state.name} lockdown: "
    f"{state.government.lockdown_strength}"
)

    infected_people = [
        h for h in state.population
        if h.status == Status.INFECTED
    ]

    for human in infected_people:

        human.infected_days += 1
        contacts = int(
            10 * (
                1 - state.government.effective_lockdown()
            ) * state.density
        )

        contacts = max(1, contacts)

        for _ in range(contacts):

            if random.random() < virus.infectivity:

                target = random.choice(state.population)

                if target.status == Status.HEALTHY:
                    target.infect()

        effective_recovery = (
            virus.recovery *
            state.government.healthcare_boost
        )   * state.density
        if random.random() < virus.mortality:
            human.die()

        elif random.random() < effective_recovery:
            human.recovery()

class Simulation:

    def run(self, states, virus, routes, days):
        for day in range(days):

            travel_spread(routes)

            print(f"\n===== Day {day+1} =====")
            for state in states:
            
                simulate_day(state, virus)

            for state in states:


                state.stats()

            if random.random() < 0.05:

                mutation = random.choice(MUTATIONS)

                virus.add_mutation(mutation)