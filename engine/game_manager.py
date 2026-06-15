class GameManager:

    def __init__(self):

        self.game_over = False
        self.winner = None
        self.reason = None

    def check_loss(self, states):

        total_infected = 0
        total_dead = 0
        total_healthy = 0

        for state in states:

            if (
                state.is_player
                and
                state.government.collapsed
            ):

                self.game_over = True

                self.reason = (
                    "Government Collapse"
                )

                return True

            healthy, infected, dead = (
                state.get_stats()
            )

            total_infected += infected
            total_dead += dead
            total_healthy += healthy
        
            dead_ratio = total_dead / (total_infected + total_dead + total_healthy )

            if (
                state.is_player
                and 
                dead_ratio > 0.50
            ):

                self.game_over = True

                self.reason = (
                    "Population Collapse"
                )

                return True
            
            if (
                state.is_player
                and
                state.government.economy.gdp <= 20
            ):
                self.game_over = True

                self.reason = (
                    "Economic Collapse"
                )

                return True

        return False
    
    def check_win(self, states):

        total_infected = 0
        total_dead = 0
        total_healthy = 0

        for state in states:

            healthy, infected, dead = (
                state.get_stats()
            )

            total_infected += infected
            total_dead += dead
            total_healthy += healthy
        
        dead_ratio = total_dead / (total_infected + total_dead + total_healthy )

        if total_infected == 0:

            self.game_over = True

            self.reason = (
                "Virus Eradicated"
            )

            return True

        return False
    
    def update(self, states):

        if self.check_loss(states):
            return

        if self.check_win(states):
            return