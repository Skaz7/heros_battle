from classes import Dice, Status, HealthBar, Quest
from characters import *
from items import Inventory, Item, Weapon, Armor, Consumable
from spellbook import SpellBook
from world import Area
from infos import *
from cli import print_game_menu
from battle import Battle
from objects import *
from data import areas, town
from decorators import *
from collections import OrderedDict
import os
import time


def examine(area) -> None:
    print("\nWhat do you want to do?\n")

    activities = list_area_activities(area)

    for key, value in activities.items():
        print(f"{key}. {value}")

    choice = int(input(" > "))
    examine_handler(choice, area, activities)


def list_area_activities(area) -> dict:
    activities_dict = {
        1: "Show inventory",
        2: "Stop examining area",
    }
    activities_list = []
    if area.enemies is not None:
        activities_list.append("Fight Enemy")
    if area.treasures is not None:
        activities_list.append("Open chest")
    if area.npcs is not None:
        activities_list.append("Talk to NPC")

    activities_dict.update(
        {i: activity for i, activity in enumerate(activities_list, start=3)}
    )
    return activities_dict


def examine_handler(choice, area, activities_dict) -> None:
    if choice not in activities_dict.keys():
        print_red("Invalid choice!")
        time.sleep(0.5)
        examine(area)
    else:
        result = activities_dict[choice]
        if result == "Show inventory":
            player.inventory.show()
            input()
            examine(area)
        elif result == "Stop examining area":
            return
        elif result == "Fight Enemy":
            battle = Battle(player, enemy)
            battle.start_battle()
        elif result == "Open chest":
            player.open_chest(area.treasures)
        elif result == "Talk to NPC":
            npc = area.npcs.talk()
            print()


def explore_area(area) -> None:
    print_one_line_in_frame(f"You are in {area.name}")
    area.visited = True

    print("\nYou can go to the following areas: ")
    for direction in area.available_directions:
        print(direction)

    print("\nYou can see the following enemies: ")
    if area.enemies is not None:
        for enemy in area.enemies:
            print(enemy)

    print("\nYou can see the following treasures: ")
    if area.treasures is not None:
        print(area.treasures.name)

    print("\nYou can see the following npcs: ")
    if area.npcs is not None:
        print(area.npcs.name)
    print()

    for number, next_area in enumerate(area.available_directions, start=1):
        print(f"{number}. Go to {next_area}.")

    print(f"{number+1}. Examine {area.name}.")
    print("0. OPTIONS.")

    choice = int(input("\n > "))
    explore_area_choice_handler(number, choice, area)
    explore_area(area)


def explore_area_choice_handler(number, choice, area):
    if 1 <= choice <= (len(area.available_directions)):
        next_area = areas.get(area.available_directions[choice - 1])
        explore_area(next_area)

    elif choice == (number + 1):
        examine(area)
    elif choice == 0:
        print_game_menu()
        choice = input(" > ")
        game_menu_handler(choice)
        explore_area(area)


def game_menu_handler(choice):
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
        game_menu_handler(choice)


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
    player.spellbook.add_spell(fireball)
    player.spellbook.add_spell(freeze)
    player.spellbook.add_spell(reveal)

    player_healthbar = HealthBar(player)
    enemy_healthbar = HealthBar(enemy)


if __name__ == "__main__":
    os.system("clear")
    main()
    explore_area(town)
