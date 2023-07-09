from characters import *
from world import Area
from battle import Battle
from objects import *
from decorators import print_one_line_in_frame
from collections import OrderedDict
import os
import time


### Health Bar creation and drawing
# player_healthbar = HealthBar(player)
# print()
# player_healthbar.draw_health_bar()
# player.take_damage(41)
# player_healthbar.draw_health_bar()
# player.take_damage(33)
# player_healthbar.draw_health_bar()
# print()
# enemy_healthbar = HealthBar(enemy)
# print()
# enemy_healthbar.draw_health_bar()
# enemy.take_damage(31)
# enemy_healthbar.draw_health_bar()
# enemy.take_damage(27)
# enemy_healthbar.draw_health_bar()
# print()


# Creating Battle with turns
battle = Battle(player, enemy)
# battle.start_battle()

# print_all_stats(player)
# print_all_stats(enemy)
# print_battle_stats(player)
# print_battle_stats(enemy)

# player.inventory.show()

forest = Area(
    name="Forest",
    description="A dark old forest.",
    available_directions=["Town", "Plains", "Ruins"],
    enemies=["Goblin", "Orc"],
    treasures=["Small chest"],
    npcs=["Old Man"],
    visited=False,
)
town = Area(
    name="Town",
    description="A Town with many people.",
    available_directions=["Forest", "Plains", "Ruins"],
    enemies=None,
    treasures=None,
    npcs=["Merchant"],
    visited=False,
)

# areas = {
#     "Forest": forest,
#     "Town": town,
#     "Plains": None,
#     "Ruins": None,
# }


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


# explore_area(town)


# def area_activity(area):
#     activities = [
#         "Show inventory",
#         "Leave area",
#         "Exit game",
#     ]
#     if area.enemies is not None:
#         activities.insert(0, "Fight")
#     if area.treasures is not None:
#         activities.insert(0, "Open chest")
#     if area.npcs is not None:
#         activities.insert(0, "Talk to NPC")

#     print("\nWhat do you want to do?\n")
#     for i, activity in enumerate(activities, start=1):
#         print(f"{i}. {activity}")
#     try:
#         choice = input(" > ")
#         if choice == "1":
#             area.inventory.show()
#     except (ValueError, IndexError):
#         print("Invalid choice!")
#         time.sleep(1)
#         area_activity(area)


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


area_activity(forest)
