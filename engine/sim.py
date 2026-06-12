import random
from models.status import Status
from data.mutation import MUTATIONS
from engine.travel import travel_spread
from engine.history import History
from world.world_graph import display_world 
from engine.network_map import generate_world_map
from events.events import EVENTS

def simulate_day(state, virus):

    state.government.decide(state)

    state.government.daily_update()

    '''print(
    f"{state.name} lockdown: "
    f"{state.government.lockdown_strength}"
)'''

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
            state.government.healthcare_boost *
            state.healthcare
        ) / state.density
        if random.random() < virus.mortality:
            human.die()

        elif random.random() < effective_recovery:
            human.recovery()

class Simulation:

    def run(self, states, virus, routes, days):
        history = History()

        display_world(routes)
        

        for day in range(days):

            for state in states:

                simulate_day(state, virus)

            travel_spread(routes)

            total_inf = 0
            total_dead = 0

            total_gdp = 0
            total_support = 0

            for state in states:

                healthy, infected, dead = state.get_stats()

                total_inf += infected
                total_dead += dead

                total_gdp += (
                    state.government.economy.gdp
                )

                total_support += (
                    state.government.public_support
                )

                history.store(
                    day + 1,
                    state.name,
                    healthy,
                    infected,
                    dead,
                    state.government.economy.gdp,
                    state.government.public_support
                )

            avg_gdp = total_gdp / len(states)

            avg_support = (
                total_support / len(states)
            )

            if random.random() < 0.05:

                virus.add_mutation(
                    random.choice(MUTATIONS)
                )

            if random.random() < 0.03:

                event = random.choice(
                    EVENTS
                )

                event.apply(
                    states,
                    virus
                )

            if (day + 1) % 15 == 0:
                for state in states:
                    '''bar = "█" * max(
                        1,
                        int(infected / 100)
                    ) if infected > 0 else ""


                    print(
                        f"{state.name}: "
                        f"{bar}"
                    )'''
                

                print(f"""
        =================================
        DAY {day+1}
        =================================

        Total Infected: {total_inf}
        Total Dead: {total_dead}

        Average GDP: {avg_gdp:.2f}
        Average Support: {avg_support:.2f}

        Virus Infectivity: {virus.infectivity:.3f}
        Virus Mortality: {virus.mortality:.3f}

        =================================
        """)
                for state in states:

                    healthy, infected, dead = (
                        state.get_stats()
                    )

                    pct = (
                        infected /
                        state.population_size
                        * 100
                        +
                        dead /
                        state.population_size
                        * 100
                    )

                    bar = (
                        "█" *
                        int(pct / 5)
                    )

                    gov_name = type(
                        state.government.ai
                    ).__name__

                    print(
                        f"""
                {state.name}

                {bar}

                Healthy  : {healthy}
                Infected : {infected}
                Dead     : {dead}

                GDP      : {state.government.economy.gdp:.1f}
                Support  : {state.government.public_support:.1f}

                Lockdown : {state.government.lockdown_strength:.1f}

                Government : {gov_name}
                """
                    )
        history.graph()

        history.gdp_graph()

        history.support_graph()

        generate_world_map(
            states,
            routes
        )
                