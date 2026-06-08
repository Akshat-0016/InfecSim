class human:

    def __init__(self,name,age,health):
        self.name = name
        self.age = age
        self.health = health

    def speak(self):
        print(f"My name is {self.name}")

    def eat(self):
        self.health += 5
        print(f"{self.name} has eaten")
    
    def dmg(self, dmg):
        self.health -= dmg
        print(f"{self.name} has takne dmg")
    
    def display(self):
        print(f"My name is {self.name} of age {self.age} with health {self.health}")

# country part
    def spread_between_states(self):
        inf_states = 0
        for state in self.states:
            if State.count_infected(state) > 0.5:
                inf_states += 1
        if len(self.states) == 0:
            return 0
        
        return inf_states / len(self.states)
    
# continent part

    def spread_between_countries(self):
        inf_countries = 0
        for country in self.countries:
            if Country.spread_between_states(country) > 0.5:
                inf_countries += 1
        if len(self.countries) == 0:
            return 0
        
        return inf_countries / len(self.countries)
