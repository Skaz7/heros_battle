from classes import HealthBar
from data.characters import *
from data.weapons import *
from data.spells import *
from data.objects import *
from spellbook import SpellBook
from cli import print_game_menu
from data.world import areas, town
from decorators import *
from game import GameMenu
import os
import time
import platform


def clear_screen():
    # Get operating system name
    system = platform.uname()[0]
    # Set clear_screen proper for operating system
    if "linux" in system.lower():
        os.system("clear")
    elif "windows" in system.lower():
        os.system("cls")
    elif "macos" in system.lower():
        pass


def explore_area(area) -> None:
    print_one_line_in_frame(f"You are in {area.name}")
    area.visited = True

    print("\nYou can go to the following areas: ")
    for direction in area.available_directions:
        print(direction)

    print("\nYou can see the following enemies: ")
    if area.enemies is not None:
        for monster in area.enemies:
            print(monster)

    print("\nYou can see the following treasures: ")
    if area.treasure is not None:
        print(area.treasure.name)

    print("\nYou can see the following npcs: ")
    if area.npc is not None:
        print(area.npc.name)
    print()

    for number, next_area in enumerate(area.available_directions, start=1):
        print(f"{number}. Go to {next_area}.")

    print(f"{number + 1}. Examine {area.name}.")
    print("0. OPTIONS.")

    choice = int(input("\n > "))
    handle_area_choice(number, choice, area)
    explore_area(area)


def handle_area_choice(number, choice, area):
    if 1 <= choice <= (len(area.available_directions)):
        next_area = areas.get(area.available_directions[choice - 1])
        explore_area(next_area)

    elif choice == (number + 1):
        area.examine()
    elif choice == 0:
        game_menu(area)


def game_menu(area):
    print_game_menu()
    choice = input(" > ")
    handle_game_menu(choice)
    explore_area(area)


def handle_game_menu(choice):
    if choice == "1":
        player.inventory.show()
        print("Enter - Back")
        input()
        return
    elif choice == "2":
        print_green("Game loaded...")
    elif choice == "3":
        print_red("Game saved...")
    elif choice == "4":
        exit_game()
        return
    else:
        print_red("Invalid choice!")
        handle_game_menu(choice)


def exit_game() -> None:
    print_one_line_in_frame("ARE YOU SURE? (Y/N)")
    choice = input(" > ")
    if choice.lower() == "y":
        print_yellow("GOOD BYE...")
        time.sleep(1)
        exit()
    else:
        return


def talk_to_npc(npc) -> None:
    print("You talk to NPC")
    return


def main():
    # Create inventories and add some items
    player.inventory = Inventory([], 20, 20)
    enemy.inventory = Inventory([], 5, 5)
    player.spellbook = SpellBook([fireball, freeze])
    player.inventory.add_item(excalibur)
    player.inventory.add_item(iceblizzard)
    player.inventory.add_item(thorshammer)
    player.inventory.add_item(elvisheyes)
    player.inventory.add_item(longspear)
    enemy.inventory.add_item(silver_plate)
    player.inventory.add_item(life_potion)
    player.inventory.add_item(boost_potion)
    player.inventory.add_item(strength_potion)
    player.inventory.add_item(leather_armor)
    player.spellbook.add_spell(reveal)

    player_healthbar = HealthBar(player)
    enemy_healthbar = HealthBar(enemy)


menu = GameMenu()

if __name__ == "__main__":
    clear_screen()
    main()
    menu.show()
    explore_area(town)
