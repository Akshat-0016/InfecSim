import random

from models.state import State
from models.human import Human
from world.route import Route


class WorldGenerator:

    @staticmethod
    def generate(
        num_states=5,
        population=1000,
        player_government="democracy"
    ):

        states = []

        governments = [
            "democracy",
            "technocracy",
            "authoritarian"
        ]

        for i in range(num_states - 1):

            state = State(
                f"State_{i+1}",
                population,
                government_type=random.choice(
                    governments
                )
            )

            for _ in range(population):
                state.population.append(
                    Human()
                )

            states.append(state)

        player = State(
            f"State_{num_states}",
            population,
            government_type=player_government,
            is_player=True
        )

        for _ in range(population):
            player.population.append(
                Human()
            )

        states.append(player)

        states[0].population[0].infect()

        routes = []

        for i in range(len(states)):

            connections = random.randint(
                2,
                4
            )

            possible = [

                s for s in states

                if s != states[i]
            ]

            connected = random.sample(
                possible,
                min(
                    connections,
                    len(possible)
                )
            )

            for target in connected:

                routes.append(

                    Route(

                        states[i],

                        target,

                        random.randint(
                            50,
                            200
                        )

                    )
                )

        existing = set()
        routes = []

        for state in states:

            targets = random.sample(
                [s for s in states if s != state],
                min(
                    random.randint(2, 4),
                    len(states)-1
                )
            )

            for target in targets:

                key = tuple(
                    sorted(
                        [
                            state.name,
                            target.name
                        ]
                    )
                )

                if key in existing:
                    continue

                existing.add(key)

                routes.append(
                    Route(
                        state,
                        target,
                        random.randint(
                            50,
                            200
                        )
                    )
                )

        return states, routes