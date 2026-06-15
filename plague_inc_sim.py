# this is a simple attempt to replicate plague inc game

def simulate_day(state, virus):

    infected_people = [
        h for h in state.population
        if h.status == "infected"
    ]

    for human in infected_people:
        
        human.infected_days += 1

        for i in range(10):
            if random.random() < virus.infectivity + (human.infected_days/1000) ** 5:

                target = random.choice(state.population)

                if target.status == "healthy":
                    target.infect()

        if random.random() < virus.mortality + (human.infected_days/1000) ** 3:
            human.die()

        elif random.random() < virus.recovery - (human.infected_days/1000) ** 3:
            human.recovery()

def main():
    virus = Virus("zvirus", 0.05, 0.01, 0.05)

    state_1 = State("state_1")

    for i in range(1000):
        state_1.population.append(Human()) 
    
    state_1.population[0].infect()

    for day in range(100):

        simulate_day(state_1, virus)

        print(f"\nDay {day+1}")

        state_1.stats()

if __name__ == "__main__":
    main()