from events.event import Event

import random

from data.mutation import MUTATIONS

class MutationEvent(Event):

    def __init__(self):

        super().__init__(
            "Mutation Surge"
        )

    def apply(
        self,
        states,
        virus
    ):

        mutation = random.choice(
            MUTATIONS
        )

        virus.add_mutation(
            mutation
        )

        print(
            "\nEVENT: Mutation Surge"
        )