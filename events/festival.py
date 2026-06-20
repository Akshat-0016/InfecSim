from events.event import Event

class Festival(Event):

    def __init__(self):

        super().__init__(
            "Festival"
        )

    def apply(
        self,
        states,
        virus
    ):

        target = max(
            states,
            key=lambda s:
            s.population_size
        )

        target.density *= 1.5

        return (
            f"Festival in {target.name}"
        )