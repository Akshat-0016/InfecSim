import tkinter as tk

from ui.screens.menu_screen import MenuScreen
from ui.screens.new_game_screen import (
    NewGameScreen
)

from ui.screens.game_screen import (
    GameScreen
)

from ui.screens.end_game_screen import (
    EndScreen
)
from engine.sim import Simulation
from engine.sim_manager import (
    SimulationManager
)

from ui.main_window import (
    MainWindow
)
from models.virus import Virus
from world.world_generator import WorldGenerator
from data.difficulty import DIFFICULTIES


class App:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "InfecSim"
        )
        self.root.geometry(
            "1200x800"
        )
        self.container = tk.Frame(
            self.root
        )

        self.container.pack(
            fill="both",
            expand=True
        )

        self.show_menu()

    def clear(self):

        for widget in (
            self.container
            .winfo_children()
        ):
            widget.destroy()

    def show_menu(self):

        self.clear()

        MenuScreen(
            self.container,
            self
        ).frame.pack(
            fill="both",
            expand=True
        )

    def run(self):

        self.root.mainloop()

    def start_game(
        self,
        num_states,
        difficulty,
        government
    ):

        settings = DIFFICULTIES[
            difficulty
        ]

        virus = Virus(
            "zvirus",

            settings["infectivity"],

            settings["mortality"],

            settings["recovery"]
        )

        states, routes = (
            WorldGenerator.generate(
                num_states,
                1000,
                government
            )
        )
        simulation = Simulation()

        manager = SimulationManager(
            simulation,
            states,
            virus,
            routes
        )

        self.clear()

        game = MainWindow(
            self.container,
            manager,
            self
        )

        game.selected_state = states[0]

        game.state_panel.update_state(
            states[0]
        )

        game.map_panel.update_map(
            states,
            routes
        )

        game.start()

        print(
            difficulty,
            settings
        )


    def show_end_screen(
        self,
        reason
    ):

        self.clear()

        EndScreen(

            self.container,

            self,

            reason

        ).frame.pack(
            fill="both",
            expand=True
        )

    def show_new_game(self):

        self.clear()

        screen = NewGameScreen(
            self.container,
            self
        )

        screen.frame.pack(
            fill="both",
            expand=True
        )

    