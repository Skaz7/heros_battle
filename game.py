from dataclasses import dataclass, field
from decorators import *
import os
import time

options_list = [
    "NEW GAME",
    "LOAD GAME",
    "SAVE GAME",
    "HERO INFO",
    "EXIT GAME",
]


def load_game(filename):
    with open(filename, "r") as file:
        game_data = file.readlines(end="")


def save_game(filename, gamedata):
    with open(filename, "wr") as file:
        file.write(gamedata)


def print_game_menu():
    print_one_line_in_frame("BEASTSLAYER CHRONICLES")


def exit_game() -> None:
    print_one_line_in_frame("ARE YOU SURE? (Y/N)")
    choice = input(" > ")
    if choice.lower() == "y":
        print_yellow("GOOD BYE...")
        time.sleep(1)
        exit()
    else:
        return


@dataclass
class GameMenu:
    options: list = field(default_factory=list[str])

    def show(self):
        os.system("clear")
        print_game_menu()
        print("Choose an option:")
        print()
        self.options = options_list
        for number, option in enumerate(self.options, start=1):
            print(f"{number}. {option}")
        choice = int(input(" > "))
        self.handle_options_choice(choice)

    def handle_options_choice(self, choice):
        if choice not in range(1, len(self.options) + 1):
            print_red("Invalid choice!")
            time.sleep(0.5)
            self.show()
        else:
            if choice == 1:
                pass
            elif choice == 2:
                print_green("Game loaded.")
                time.sleep(0.5)
                self.show()
            elif choice == 3:
                print_red("Game saved.")
                time.sleep(0.5)
                self.show()
            elif choice == 4:
                print_yellow("Hero info.")
                hero_info()
            elif choice == 5:
                exit_game()
