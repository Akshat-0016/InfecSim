class Virus:
    def __init__(self, name, infectivity, mortality, recovery):
        self.name = name
        self.infectivity = infectivity
        self.mortality = mortality
        self.recovery = recovery
        self.mutations = []

    def add_mutation(self, mutation):

        mutation.apply(self)
        self.infectivity = min(
            1,
            max(0, self.infectivity)
        )

        self.mortality = min(
            1,
            max(0, self.mortality)
        )

        self.recovery = min(
            1,
            max(0, self.recovery)
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