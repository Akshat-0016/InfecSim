class EventLog:

    def __init__(self):

        self.events = []

    def add(self, message):

        self.events.insert(
            0,
            message
        )

    def latest(self):

        return self.events[:20]