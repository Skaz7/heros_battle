from inventory import Inventory, Consumable


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
    inventory=Inventory(),
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
    inventory=Inventory(),
    heal=90,
    mana=10,
    strength=0,
    dexterity=0,
)

strength_potion = Consumable(
    name="Strength Potion",
    description="Increases Strength by 20",
    value=20,
    slot_size=1,
    required_strength=0,
    required_dexterity=0,
    allowed_race="Human",
    max_durability=1,
    durability=1,
    inventory=Inventory(),
    heal=0,
    mana=0,
    strength=15,
    dexterity=0,
)


