from models.status import Status

class Human:

    def __init__(self):
        self.status = Status.HEALTHY
        self.infected_days = 0

    def infect(self):
        self.status = Status.INFECTED

    def recovery(self):
        self.status = Status.HEALTHY
        self.infected_days = 0

    def die(self):
        self.status = Status.DEAD