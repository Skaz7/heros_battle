import time
from classes import *
from battle import Battle
from decorators import slow_print, print_one_line_in_frame
from dataclasses import fields


def print_all_stats(creature):
    print()
    print_one_line_in_frame(f"{creature.name} Stats:")
    for key, value in creature.__dict__.items():
        slow_print(f"    {key[1:].title():10} : {value}\n")
    creature.inventory.show()

def print_battle_stats(creature):
    print()
    print_one_line_in_frame(f"{creature.name} Stats:")
    creature.inventory.show()
    slow_print(f"    Health : {creature.health}\n")
    slow_print(f"    Experience : {creature.experience}\n")
    slow_print(f"    Level : {creature.level}\n")

# Create Hero and Enemy
player = Hero(
    "Jimi Hendrix",
    1,
    0,
    "Human",
    110,
    94,
    20,
    8,
    15,
    "Sick",
    None,
    True,
    10,
)
enemy = Enemy(
    "Azog The Defiler",
    1,
    0,
    "Orc",
    70,
    70,
    10,
    5,
    10,
    "Stunned",
    None,
    True,
    "Cold",
    "Fire",
)

# Create weapons
excalibur = Weapon(
    "Excalibur",
    "Great Sword",
    50,
    1,
    15,
    15,
    "Human",
    2,
    "Slash",
    15,
)
iceblizzard = Weapon(
    "Ice Blizzard",
    "Staff",
    40,
    1,
    10,
    15,
    "Human",
    30,
    "ice",
    15,
)
thorshammer = Weapon(
    "Destroyer",
    "Hammer",
    10,
    1,
    20,
    10,
    "Dwarf",
    50,
    "blunt",
    20,
)
elvisheyes = Weapon(
    "Elvish Eyes",
    "Bow",
    20,
    1,
    15,
    15,
    "Elf",
    30,
    "stab",
    12,
)
longspear = Weapon(
    "Long Spear",
    "Spear",
    15,
    2,
    10,
    15,
    "Human",
    35,
    "stab",
    15,
)
silver_plate = Armor(
    "Silver Plate",
    "Great Armor made of silver.",
    30,
    2,
    20,
    0,
    "Human",
    15,
    "Blunt",
    20,
)

# Create inventory and add some items
player.inventory = Inventory([], 20, 20)
enemy.inventory = Inventory([], 5, 5)
player.inventory.add_item(excalibur)
player.inventory.add_item(iceblizzard)
player.inventory.add_item(thorshammer)
player.inventory.add_item(elvisheyes)
player.inventory.add_item(longspear)
enemy.inventory.add_item(silver_plate)

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
# battle = Battle(player, enemy)
# battle.start_battle()


# print_all_stats(player)
# print_all_stats(enemy)
# print_battle_stats(player)
# print_battle_stats(enemy)

# player.inventory.show()