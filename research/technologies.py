class Technology:
    def __init__(self,
        name,
        cost
    ):

        self.name = name
        self.cost = cost

        self.unlocked = False

class RapidTesting(Technology):

    def __init__(self):

        super().__init__(
            "Rapid Testing",
            20
        )

class BetterTreatment(Technology):

    def __init__(self):

        super().__init__(
            "Better Treatment",
            40
        )

class VaccinePrototype(Technology):

    def __init__(self):

        super().__init__(
            "Vaccine Prototype",
            70
        )

class VaccineProduction(Technology):

    def __init__(self):

        super().__init__(
            "Vaccine Production",
            100
        )
        