import time
from classes import *
from battle import Battle
from decorators import slow_print, print_one_line_in_frame


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
    slow_print(f"\n    Armor:      {player.armor}")
    slow_print(f"\n    Gold:       {player.inventory.gold}")
    slow_print(f"\n    Status:     {player.status}")
    slow_print(f"\n    Gold:       {player.inventory.gold}")
    slow_print(f"\n    Inventory:")
    player.inventory.show_inventory()


def print_enemy_stats(enemy):
    print()
    print_one_line_in_frame("Enemy Stats:")
    slow_print(f"\n    Name:       {enemy.name}")
    slow_print(f"\n    Level:      {enemy.level}")
    slow_print(f"\n    Experience: {enemy.experience}")
    slow_print(f"\n    Race:       {enemy.race}")
    slow_print(f"\n    Max Health: {enemy.max_health}")
    slow_print(f"\n    Health:     {enemy.health}")
    slow_print(f"\n    Attack:     {enemy.strength}")
    slow_print(f"\n    Dexterity:  {enemy.dexterity}")
    slow_print(f"\n    Armor:      {enemy.armor}")
    slow_print(f"\n    Weakness:   {enemy.weakness}")
    slow_print(f"\n    Resistance: {enemy.resistance}")
    slow_print(f"\n    Status:     {enemy.status}\n")
    slow_print(f"\n    Gold:       {enemy.inventory.gold}")
    slow_print(f"\n    Inventory:")


# Create Hero and Enemy
player = Hero("Jimi Hendrix", 1, 0, "Human", 110, 94, 20, 8, 15, "Sick", None, 10)
enemy = Enemy(
    "Azog", 1, 0, "Goblin", 70, 70, 10, 5, 10, "Alive", None, "Cold", "Fire"
)

# Create weapons
excalibur = Weapon("Excalibur", "Great Sword", 50, 1, 15, 15, "Human", 2, "Slash", 15)
iceblizzard = Weapon("Ice Blizzard", "Staff", 40, 1, 10, 15, "Human", 30, "ice", 15)
thorshammer = Weapon("Destroyer", "Hammer", 10, 1, 20, 10, "Dwarf", 50, "blunt", 20)
elvisheyes = Weapon("Elvish Eyes", "Bow", 20, 1, 15, 15, "Elf", 30, "stab", 12)
longspear = Weapon("Long Spear", "Spear", 15, 2, 10, 15, "Human", 35, "stab", 15)

silver_plate = Armor(
    "Silver Plate", "Great Armor made of silver.", 30, 2, 20, 0, "Human", 15, "Blunt", 20
)
# Create inventory and add some items
player.inventory = Inventory()
enemy.inventory = Inventory()

player.inventory.add_item_to_inventory(excalibur)
player.inventory.add_item_to_inventory(iceblizzard)
player.inventory.add_item_to_inventory(thorshammer)
player.inventory.add_item_to_inventory(elvisheyes)
player.inventory.add_item_to_inventory(longspear)

player.inventory.show_inventory()
player.inventory.remove_item_from_inventory(iceblizzard)
player.inventory.show_inventory()

# Check taking damage
player.take_damage(4)
print_player_stats(player)
print_enemy_stats(enemy)
print(f"\nIs player alive? -> {player.is_alive()}\n")


# check if weapon named Excalibur is in inventory
# if it is, print it's stats
def check_if_weapon_in_inventory(weapon_name):
    for weapon in player.inventory.items:
        if weapon.name == weapon_name:
            print(weapon)


# Checking if item is in inventory
check_if_weapon_in_inventory("Destroyer")
check_if_weapon_in_inventory("Ice Blizzard")
check_if_weapon_in_inventory("Elvish Eyes")
check_if_weapon_in_inventory("Long Spear")


# Health Bar creation and drawing
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


# Equipping weapon and armor to increase creature statistics
player.equip_weapon(excalibur)
player.equip_armor(silver_plate)
print_player_stats(player)
print(excalibur.is_equipped, silver_plate.is_equipped)
player.unequip_weapon(excalibur)
player.unequip_armor(silver_plate)
print_player_stats(player)
print(excalibur.is_equipped, silver_plate.is_equipped)
excalibur.degrade()
excalibur.degrade()
print(excalibur.name)
print(excalibur.damage)
