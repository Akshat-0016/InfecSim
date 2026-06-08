class Sector:

    def __init__(
        self,
        name,
        value,
        workers,
        growth_rate,
        lockdown_sensitivity,
        tax_rate
    ):
        self.name = name
        self.value = value

        self.workers = workers

        self.growth_rate = growth_rate

        self.lockdown_sensitivity = (
            lockdown_sensitivity
        )

        self.tax_rate = tax_rate