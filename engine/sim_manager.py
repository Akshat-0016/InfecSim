from engine.sim import simulate_day, travel_spread
from engine.events_log import EventLog
from engine.game_manager import GameManager


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

        # =====================
        # CHECK WIN / LOSS
        # =====================

        self.game.update(
            self.states
        )

        if self.game.game_over:

            self.running = False

            self.event_log.add(
                f"GAME OVER: "
                f"{self.game.reason}"
            )