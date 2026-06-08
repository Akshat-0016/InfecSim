import random

from models.virus import Virus
from models.human import Human
from models.state import State
from world.route import Route

from data.mutation import MUTATIONS

from engine.sim import simulate_day, Simulation
from engine.travel import travel_spread

virus = Virus(
    "zvirus",
    0.05,
    0.01,
    0.05
)

states = []

for i in range(5):

    state = State(
        f"state_{i+1}",
        1000
    )

    for _ in range(1000):
        state.population.append(Human())

    states.append(state)

# Patient Zero
states[0].population[0].infect()

routes = [

    Route(states[0], states[1], 100),

    Route(states[1], states[2], 100),

    Route(states[2], states[3], 100),

    Route(states[3], states[4], 100)

]

simulation = Simulation()

days=100
simulation.run(states, virus, routes, days)

'''for day in range(100):

    print(f"\n===== Day {day+1} =====")

    for state in states:

        simulate_day(state, virus)

        travel_spread(routes)

        state.stats()

    if random.random() < 0.05:

        mutation = random.choice(MUTATIONS)

        virus.add_mutation(mutation)'''