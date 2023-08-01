from classes import Dice, Status, HealthBar, Quest
from characters import *
from items import Inventory, Item, Weapon, Armor, Consumable
from spellbook import SpellBook
from world import Area
from infos import *
from battle import Battle
from objects import *
from data import areas, town
from decorators import *
from collections import OrderedDict
import os
import time


def examine(area):
    activities = OrderedDict()
    activities["Show inventory"] = player.inventory.show
    activities["Leave area"] = None
    activities["Exit game"] = exit

    if area.enemies is not None:
        battle = Battle(player, enemy)
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
        examine(area)


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
        print(f"{i}. Go to {next_area}.")

    print(f"{i+1}. Examine {area.name}.")

    try:
        choice = int(input("\n > "))
        if choice == i + 1:
            print(i + 1)
            examine(area)
        elif 1 <= choice <= (len(area.available_directions) + 1):
            next_area = areas.get(area.available_directions[choice - 1])
            explore_area(next_area)
        else:
            print("Invalid choice")
            explore_area(area)
    except (ValueError, IndexError):
        print("Invalid choice")
        explore_area(area)


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
    # area_activity(forest)
