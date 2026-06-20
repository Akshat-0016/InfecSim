import random

from models.status import Status


def travel_spread(routes):

    for route in routes:

        restriction = max(
            route.source.government.travel_restriction,
            route.destination.government.travel_restriction
        )

        effective_travellers = int(
            route.daily_travellers *
            (1 - restriction)
        )

        source_ratio = (
            route.source.count_infected()
        )

        source_restriction = (
            route.source.government.travel_restriction
        )

        destination_restriction = (
            route.destination.government.travel_restriction
        )

        source_restriction *= (
            route.source
            .government
            .travel_ban_bonus
        )

        destination_restriction *= (
            route.destination
            .government
            .travel_ban_bonus
        )

        restriction = max(
            source_restriction,
            destination_restriction
        )

        chance = (
            source_ratio *
            (effective_travellers / 1000)
        )

        if random.random() < chance:

            healthy_people = [

                h for h in route.destination.population

                if h.status == Status.HEALTHY

            ]

            if healthy_people:

                random.choice(
                    healthy_people
                ).infect()