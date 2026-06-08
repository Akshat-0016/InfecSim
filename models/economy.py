from models.sector import Sector

class Economy:

    def __init__(self):

        self.gdp = 100.0

        self.unemployment = 5.0

        self.inflation = 2.0

        self.business_confidence = 100.0

        self.market_index = 1000.0

        self.healthcare_budget = 100.0

        self.tax_revenue = 50.0

        self.sectors = {

            "tourism": Sector(
                "tourism",
                100,
                5000,
                0.01,
                3.0,
                0.15
            ),

            "manufacturing": Sector(
                "manufacturing",
                100,
                8000,
                0.02,
                1.5,
                0.20
            ),

            "tech": Sector(
                "tech",
                100,
                10000,
                0.04,
                0.5,
                0.25
            ),

            "healthcare": Sector(
                "healthcare",
                100,
                4000,
                0.03,
                -0.5,
                0.10
            )

        }       

    def daily_update(self, lockdown_strength):

        self.gdp -= lockdown_strength * 0.3

        self.gdp = max(
            0,
            self.gdp
        )

        self.unemployment += lockdown_strength * 0.1

        self.business_confidence -= lockdown_strength * 0.2

        self.market_index *= (
            1 - lockdown_strength * 0.01
        )

        self.tax_revenue = self.gdp * 0.5

        
        for sector in self.sectors.values():

            sector.value *= (
                1
                + sector.growth_rate
                - lockdown_strength
                * sector.lockdown_sensitivity
                * 0.01
            )

        for sector in self.sectors.values():

            sector.value = max(
                0,
                sector.value
            )

    def report(self):

        print(f"""
        GDP: {self.gdp:.2f}
        Unemployment: {self.unemployment:.2f}
        Inflation: {self.inflation:.2f}
        Market Index: {self.market_index:.2f}

        Technology: {self.sectors["tech"].value:.2f}
        Tourism: {self.sectors["tourism"].value:.2f}
        Manufacturing: {self.sectors["manufacturing"].value:.2f}
        Healthcare: {self.sectors["healthcare"].value:.2f}
        """)