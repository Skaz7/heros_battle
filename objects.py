from classes import *
from items import Inventory, Item, Weapon, Armor, Consumable


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
