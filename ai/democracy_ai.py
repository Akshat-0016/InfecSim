from ai.government_ai import GovernmentAI


class DemocracyAI(GovernmentAI):

    def choose_action(
        self,
        government,
        state
    ):

        infected_ratio = state.count_infected()

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

            projected_support = (
                government.public_support
                - action * 10
            )

            score = (
                projected_gdp
                + projected_support * 2
                - projected_infections * 100
            )

            if score > best_score:
                best_score = score
                best_action = action

        return best_action