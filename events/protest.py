from events.event import Event

class Protest(Event):

    def __init__(self):

        super().__init__(
            "Protest"
        )

    def apply(
        self,
        states,
        virus
    ):

        affected = []

        for state in states:

            if (
                state.government.lockdown_strength
                > 0.7
            ):

                state.government.public_support -= 10

                affected.append(
                    state.name
                )

        if affected:

            return (
                "Protests in "
                + ", ".join(affected)
            )

        return None