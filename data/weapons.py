from inventory import Inventory, Weapon, Shield, Armor


# Create weapons
excalibur = Weapon(
    name="Excalibur",
    description="Great Sword",
    value=50,
    slot_size=1,
    required_strength=15,
    required_dexterity=15,
    allowed_race="Human",
    max_durability=5,
    durability=3,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    damage_type="Slash",
    damage=15,
)

iceblizzard = Weapon(
    name="Ice Blizzard",
    description="Staff",
    value=40,
    slot_size=1,
    required_strength=10,
    required_dexterity=15,
    allowed_race="Human",
    max_durability=10,
    durability=3,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    damage_type="ice",
    damage=10,
)

thorshammer = Weapon(
    name="Destroyer",
    description="Hammer",
    value=10,
    slot_size=1,
    required_strength=20,
    required_dexterity=10,
    allowed_race="Dwarf",
    max_durability=20,
    durability=3,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    damage_type="blunt",
    damage=20,
)

elvisheyes = Weapon(
    name="Elvish Eyes",
    description="Bow",
    value=20,
    slot_size=1,
    required_strength=15,
    required_dexterity=15,
    allowed_race="Elf",
    max_durability=25,
    durability=3,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    damage_type="stab",
    damage=12,
)

longspear = Weapon(
    name="Long Spear",
    description="Spear",
    value=15,
    slot_size=2,
    required_strength=10,
    required_dexterity=15,
    allowed_race="Human",
    max_durability=3,
    durability=10,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    damage_type="stab",
    damage=15,
)

oak_shield = Shield(
    name="Oak Shield",
    description="Basic shield, not too good..",
    value=15,
    slot_size=2,
    required_strength=10,
    required_dexterity=0,
    allowed_race="Human",
    max_durability=20,
    durability=20,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    resistance="Wind",
    protection=10,
)

silver_plate = Armor(
    name="Silver Plate",
    description="Great Armor made of silver.",
    value=30,
    slot_size=2,
    required_strength=20,
    required_dexterity=0,
    allowed_race="Human",
    max_durability=40,
    durability=3,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    resistance="Cold",
    protection=20,
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
    durability=3,
    inventory=Inventory,
    is_equipped=False,
    is_broken=False,
    resistance="Cold",
    protection=5,
)
