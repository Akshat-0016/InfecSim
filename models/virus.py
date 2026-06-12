class Virus:
    def __init__(self, name, infectivity, mortality, recovery):
        self.name = name
        self.infectivity = infectivity
        self.mortality = mortality
        self.recovery = recovery
        self.mutations = []

    def add_mutation(self, mutation):

        mutation.apply(self)
        self.infectivity = max(
            0,
            min(1, self.infectivity)
        )

        self.mortality = max(
            0.001,
            min(1, self.mortality)
        )

        self.recovery = max(
            0,
            min(1, self.recovery)
        )

        self.mutations.append(mutation)

        print(
            f"{self.name} evolved: {mutation.name}"
        )

    def show_mutations(self):

        print("\nMutations:")

        for mutation in self.mutations:
            print(mutation.name)

    def report(self):

        print(f"""
Virus: {self.name}

Infectivity: {self.infectivity:.3f}
Mortality: {self.mortality:.3f}
Recovery: {self.recovery:.3f}
""")