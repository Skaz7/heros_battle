from infos import *
from classes import *
from battle import Battle
from world import *
import time
from collections import OrderedDict


# Create Hero and Enemy
player = Hero(
    "Thorin Oakenshield",
    1,
    0,
    "Dwarf",
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
    25,
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

areas = {
    "Forest": forest,
    "Town": town,
    "Plains": None,
    "Ruins": None,
}


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
