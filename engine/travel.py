import random

from models.status import Status


def travel_spread(routes):

    for route in routes:

        source_ratio = route.source.count_infected()

        chance = source_ratio * 0.2

        if random.random() < chance:

            healthy_people = [

                h for h in route.destination.population

                if h.status == Status.HEALTHY

            ]

            if healthy_people:

                random.choice(
                    healthy_people
                ).infect()