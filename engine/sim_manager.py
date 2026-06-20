import random

from engine.sim import simulate_day, travel_spread
from engine.events_log import EventLog
from engine.game_manager import GameManager
from events.events import EVENTS
from engine.research_manager import ResearchManager
from policies.active_policies import ActivePolicy

class SimulationManager:

    def __init__(
        self,
        simulation,
        states,
        virus,
        routes
    ):

        self.game = GameManager()

        self.simulation = simulation

        self.states = states
        self.virus = virus
        self.routes = routes

        self.event_log = EventLog()

        self.running = False

        self.speed = 1000

        self.day = 0

    def play(self):

        print("PLAY PRESSED")

        self.running = True

    def pause(self):

        self.running = False

    def set_speed(
        self,
        milliseconds
    ):

        self.speed = milliseconds

    def tick(self):

        if not self.running:
            return

        if self.game.game_over:
            return

        self.day += 1

        self.update_policies()

        for state in self.states:

            govt = state.government

            if state.is_player:

                unlock = ResearchManager.update(
                    govt
                )

                if unlock:

                    self.event_log.add(
                        f"Research Breakthrough: "
                        f"{unlock}"
                    )
        for state in self.states:

            simulate_day(
                state,
                self.virus
            )

            if (
                state.government.collapsed
                and
                not getattr(
                    state.government,
                    "collapse_logged",
                    False
                )
            ):

                self.event_log.add(
                    f"Day {self.day}: "
                    f"{state.name} government collapsed"
                )

                state.government.collapse_logged = True

        travel_spread(
            self.routes
        )

        if random.random() < 0.02:

            event = random.choice(
                EVENTS
            )

            result = event.apply(
                self.states,
                self.virus
            )

            if result:

                self.event_log.add(
                    f"Day {self.day}: {result}"
                )

        # =====================
        # CHECK WIN / LOSS
        # =====================

        self.game.update(
            self.states
        )

        if self.game.game_over:

            self.running = False

            if hasattr(
                self,
                "game_over_callback"
            ):

                self.game_over_callback(
                    self.game.reason
                )

            self.event_log.add(
                f"GAME OVER: "
                f"{self.game.reason}"
            )

    def get_player(self):

        for state in self.states:

            if state.is_player:
                return state

        return None
    
    def increase_lockdown(self):

        player = self.get_player()

        if not player:
            return

        if player.government.political_capital < 10:
            return

        player.government.impose_lockdown(
            0.1
        )

        self.event_log.add(
            f"Day {self.day}: Lockdown Increased"
        )

    def decrease_lockdown(self):

        player = self.get_player()

        if not player:
            return

        player.government.impose_lockdown(
            -0.1
        )

        self.event_log.add(
            f"Day {self.day}: Lockdown Decreased"
        )

    def fund_research(self):

        player = self.get_player()

        if not player:
            return

        if player.government.political_capital < 15:
            return

        player.government.update_research()

        player.government.political_capital = max(
            0,
            min(100, player.government.political_capital - 15)
        )

        self.event_log.add(
            f"Day {self.day}: Research Funded"
        )

    def boost_healthcare(self):

        player = self.get_player()

        if not player:
            return

        player.government.improve_healthcare(
            0.1
        )

        self.event_log.add(
            f"Day {self.day}: Healthcare Boost"
        )

    def mass_testing(self):

        player = self.get_player()

        if player.government.political_capital < 10:
            return

        player.government.testing_level += 1

        player.government.political_capital -= 10

        self.event_log.add(
            f"Day {self.day}: Mass Testing Expanded"
        )

    def stimulus_package(self):

        player = self.get_player()

        if player.government.political_capital < 15:
            return

        player.government.economy.gdp += 5

        player.government.public_support += 5

        player.government.political_capital -= 15

        self.event_log.add(
            f"Day {self.day}: Stimulus Package Passed"
        )

    def travel_ban(self):

        player = self.get_player()

        if player.government.political_capital < 20:
            return

        player.government.travel_restriction = min(
            1.0,
            player.government.travel_restriction + 0.25
        )

        player.government.political_capital -= 20

        self.event_log.add(
            f"Day {self.day}: Travel Restrictions Increased"
        )

    def emergency_powers(self):

        player = self.get_player()

        if player.government.political_capital < 25:
            return

        player.government.emergency_powers = True

        player.government.public_support -= 2

        self.event_log.add(
            f"Day {self.day}: Emergency Powers Declared"
        )

    def vaccine_rollout(self):

        player = self.get_player()

        if not player.government.vaccine_unlocked:
            return
        
    def enact_policy(
        self,
        policy
    ):

        player = self.get_player()

        if not player:
            return

        for active in player.active_policies:

            if active.policy.name == policy.name:
                return

        policy.apply(player)

        player.active_policies.append(
            ActivePolicy(policy)
        )

        self.event_log.add(
            f"Day {self.day}: "
            f"{policy.name} enacted"
        )

    def update_policies(self):

        player = self.get_player()

        if not player:
            return

        expired = []

        for active in player.active_policies:

            active.policy.daily_effect(
                player
            )

            active.remaining_days -= 1

            if active.remaining_days <= 0:

                active.policy.remove(
                    player
                )

                expired.append(active)

        for active in expired:

            player.active_policies.remove(
                active
            )

            self.event_log.add(
                f"Day {self.day}: "
                f"{active.policy.name} expired"
            )