from classes import *
from world import *
from infos import *
from battle import Battle
from decorators import slow_print, print_one_line_in_frame
from collections import OrderedDict
import os
import time


def area_activity(area):
    activities = OrderedDict()
    activities["Show inventory"] = player.inventory.show
    activities["Leave area"] = None
    activities["Exit game"] = exit

    if area.enemies is not None:
        activities["Fight"] = battle.start_battle
    if area.treasures is not None:
        activities["Open chest"] = None
    if area.npcs is not None:
        activities["Talk to NPC"] = None

    print("\nWhat do you want to do?\n")
    for i, activity in enumerate(activities.keys(), start=1):
        print(f"{i}. {activity}")
    try:
        choice = input(" > ")
        if choice == "1":
            activities["Show inventory"]()
        elif choice == "4":
            activities["Fight"]()
    except (ValueError, IndexError):
        print("Invalid choice!")
        time.sleep(1)
        area_activity(area)


def explore_area(area):
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
        for treasure in area.treasures:
            print(treasure)

    print("\nYou can see the following npcs: ")
    if area.npcs is not None:
        for npc in area.npcs:
            print(npc)
    print()

    for i, next_area in enumerate(area.available_directions, start=1):
        print(f"{i}. Go to {next_area} and explore.")

    try:
        choice = int(input("\n > "))
        next_area = areas.get(area.available_directions[choice - 1])
        if next_area is not None:
            explore_area(next_area)
        else:
            print("Invalid choice")
            explore_area(area)
    except (ValueError, IndexError):
        print("Invalid choice")
        explore_area(area)


if __name__ == "__main__":
    os.system("cls")
    pass
