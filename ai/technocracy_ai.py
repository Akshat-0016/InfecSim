from ai.government_ai import GovernmentAI


class TechnocracyAI(GovernmentAI):

    def choose_action(
        self,
        government,
        state
    ):

        healthy, infected, dead = (
            state.get_stats()
        )

        infected_ratio = (
            infected /
            state.population_size
        )

        dead_ratio = (
            dead /
            state.population_size
        )

        actions = [0, 0.3, 0.6, 0.9]

        best_score = float("-inf")
        best_action = 0

        for action in actions:

            projected_infections = (
                infected_ratio *
                (1 - action)
            )

            projected_gdp = (
                government.economy.gdp
                - action * 5
            )

            score = (
                projected_gdp
                - projected_infections * 300
                - dead_ratio * 500
            )

            if score > best_score:
                best_score = score
                best_action = action

        return best_action