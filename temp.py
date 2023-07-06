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
    20,
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
    5,
    2,
    Inventory,
    "Slash",
    15,
    False,
)

iceblizzard = Weapon(
    "Ice Blizzard",
    "Staff",
    40,
    1,
    10,
    15,
    "Human",
    10,
    10,
    Inventory,
    "ice",
    10,
    False,
)

thorshammer = Weapon(
    "Destroyer",
    "Hammer",
    10,
    1,
    20,
    10,
    "Dwarf",
    20,
    20,
    Inventory,
    "blunt",
    20,
    False,
)

elvisheyes = Weapon(
    "Elvish Eyes",
    "Bow",
    20,
    1,
    15,
    15,
    "Elf",
    25,
    25,
    Inventory,
    "stab",
    12,
    False,
)

longspear = Weapon(
    "Long Spear",
    "Spear",
    15,
    2,
    10,
    15,
    "Human",
    10,
    10,
    Inventory,
    "stab",
    15,
    False,
)

silver_plate = Armor(
    "Silver Plate",
    "Great Armor made of silver.",
    30,
    2,
    20,
    0,
    "Human",
    40,
    40,
    Inventory,
    "Cold",
    "Blunt",
    False,
)

leather_armor = Armor(
    name="Leather Jacket",
    description="Good for Humans",
    value=30,
    slot_size=1,
    required_strength=5,
    required_dexterity=0,
    allowed_race="Human",
    max_durability=15,
    durability=10,
    inventory=Inventory,
    resistance="Cold",
    protection=5,
    is_equipped=False,
)

life_potion = Consumable(
    name="Life Potion",
    description="Restores 20 health.",
    value=20,
    slot_size=1,
    required_strength=0,
    required_dexterity=0,
    allowed_race="Human",
    max_durability=1,
    durability=1,
    inventory=Inventory,
    heal=20,
    mana=0,
    strength=0,
    dexterity=0,
)

boost_potion = Consumable(
    name="Boost Potion",
    description="Restores 10 health and 10 mana.",
    value=20,
    slot_size=1,
    required_strength=0,
    required_dexterity=0,
    allowed_race="Human",
    max_durability=1,
    durability=1,
    inventory=Inventory,
    heal=90,
    mana=10,
    strength=0,
    dexterity=0,
)

strength_potion = Consumable(
    name="Strenght Potion",
    description="Increases Strength by 20",
    value=20,
    slot_size=1,
    required_strength=0,
    required_dexterity=0,
    allowed_race="Human",
    max_durability=1,
    durability=1,
    inventory=Inventory,
    heal=0,
    mana=0,
    strength=15,
    dexterity=0,
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
player.inventory.add_item(life_potion)
player.inventory.add_item(boost_potion)
player.inventory.add_item(strength_potion)
player.inventory.add_item(leather_armor)

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
battle.start_battle()


# print_all_stats(player)
# print_all_stats(enemy)
# print_battle_stats(player)
# print_battle_stats(enemy)

# player.inventory.show()
