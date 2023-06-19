import time
from classes import *


def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.003)


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
    slow_print(f"\n    Name:       {enemy.name}")
    slow_print(f"\n    Level:      {enemy.level}")
    slow_print(f"\n    Attack:     {enemy.strength}")
    slow_print(f"\n    Health:     {enemy.health}")
    slow_print(f"\n    Armor:      {enemy.armor}")
    slow_print(f"\n    XP:         {enemy.xp}")
    slow_print(f"\n    Gold:       {enemy.gold}")
    slow_print(f"\n    Weakness:   {enemy.weakness}")
    slow_print(f"\n    Resistance: {enemy.resistance}")
    slow_print(f"\n    Status:     {enemy.status}\n")


excalibur = Weapon("Excalibur", "Sword", "slash", 50, 15)
iceblizzard = Weapon("Ice Blizzard", "Staff", "ice", 40, 15)
thorshammer = Weapon("Destroyer", "Hammer", "blunt", 10, 20)
elvisheyes = Weapon("Elvish Eyes", "Bow", "stab", 20, 12)
longspear = Weapon("Long Spear", "Spear", "stab", 15, 15)

player = Hero(
    name="Jimi Hendrix",
    level=1,
    experience=0,
    race="Human",
    max_health=150,
    health=27,
    strength=10,
    dexterity=8,
    armor=5,
    mana=15,
    gold=129,
    status="Sick",
    inventory=None,
)
enemy = Enemy(
    name="Goblin",
    level=1,
    strength=10,
    health=30,
    armor=10,
    xp=0,
    gold=10,
    weakness=None,
    resistance=None,
    status="Alive",
)

# print_player_stats(player)
# print_enemy_stats(enemy)

player.inventory = Inventory()

player.inventory.add_item_to_inventory(excalibur)
player.inventory.add_item_to_inventory(iceblizzard)
player.inventory.add_item_to_inventory(thorshammer)
player.inventory.add_item_to_inventory(elvisheyes)
player.inventory.add_item_to_inventory(longspear)

player.inventory.show_inventory()

player.inventory.remove_item_from_inventory(iceblizzard)

player.inventory.show_inventory()

battle = Battle(player, enemy)

print_player_stats(player)
print_enemy_stats(enemy)

while True:
    battle.player_turn()
    print_player_stats(player)
    print_enemy_stats(enemy)
    battle.enemy_turn()
    print_player_stats(player)
    print_enemy_stats(enemy)
