class Policy:

    def __init__(
        self,
        name,
        duration
    ):

        self.name = name
        self.duration = duration

    def apply(self, state):
        pass

    def daily_effect(self, state):
        pass

    def remove(self, state):
        pass