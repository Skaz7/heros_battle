import time
from classes import *


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)


def print_one_line_in_frame(text):
    print("+" + "-" * (len(text) + 4) + "+")
    print("|  " + text + "  |")
    print("+" + "-" * (len(text) + 4) + "+")


def print_player_stats(player):
    print()
    print_one_line_in_frame("Hero Stats:")
    slow_print(f"    Name:       {player.name}")
    slow_print(f"\n    Level:      {player.level}")
    slow_print(f"\n    Experience: {player.experience}")
    slow_print(f"\n    Race:       {player.race}")
    slow_print(f"\n    Max Health: {player.max_health}")
    slow_print(f"\n    Health:     {player.health}")
    slow_print(f"\n    Strength:   {player.strength}")
    slow_print(f"\n    Dexterity:  {player.dexterity}")
    slow_print(f"\n    Mana:       {player.mana}")
    slow_print(f"\n    Gold:       {player.gold}")
    slow_print(f"\n    Status:     {player.status}")
    slow_print(f"\n    Inventory:  {player.inventory}\n")


def print_enemy_stats(enemy):
    print()
    print_one_line_in_frame("Enemy Stats:")
    slow_print(f"\n    Race:       {enemy.race}")
    slow_print(f"\n    Level:      {enemy.level}")
    slow_print(f"\n    Attack:     {enemy.attack}")
    slow_print(f"\n    Health:     {enemy.health}")
    slow_print(f"\n    Armor:      {enemy.armor}")
    slow_print(f"\n    XP:         {enemy.xp}")
    slow_print(f"\n    Gold:       {enemy.gold}")
    slow_print(f"\n    Status:     {enemy.status}\n")


sword1 = Weapon("Excalibur", "Sword", 50, 5)
staff1 = Weapon("Ice Blizzard", "Staff", 40, 4)
hammer1 = Weapon("Destroyer", "Hammer", 10, 1)
bow1 = Weapon("Elvish Eyes", "Bow", 20, 3)
spear1 = Weapon("Long Spear", "Spear", 15, 4)

player = Hero("Jimi Hendrix", 2, 0, "Gnome", 150, 27, 12, 8, 21, 129, "Sick", [])
enemy = Enemy("Goblin", 1, 10, 20, 0, 10, 10, "Alive")

# print_player_stats(player)
# print_enemy_stats(enemy)

inventory = Inventory()

inventory.add_item_to_inventory(sword1)
inventory.add_item_to_inventory(staff1)
inventory.add_item_to_inventory(hammer1)
inventory.add_item_to_inventory(bow1)
inventory.add_item_to_inventory(spear1)

inventory.show_inventory()

inventory.remove_item_from_inventory(staff1)

inventory.show_inventory()
