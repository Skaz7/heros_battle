from battle import Battle
from classes import Quest, TreasureChest
from creatureclass import Hero, Enemy
from inventory import *


player = Hero(
    name="Thorin Oakenshield",
    level=1,
    experience=0,
    race="Dwarf",
    max_health=150,
    health=100,
    strength=15,
    dexterity=8,
    defense=5,
    statuses="Sick",
    inventory=Inventory([]),
    is_alive=True,
    spellbook=None,
    max_mana=20,
    mana=10,
)

enemy = Enemy(
    name="Azog The Defiler",
    level=1,
    experience=0,
    race="Orc",
    max_health=70,
    health=70,
    strength=10,
    dexterity=5,
    defense=10,
    statuses="Stunned",
    inventory=Inventory(),
    is_alive=True,
    spellbook=None,
    weakness="Cold",
    resistance="Fire",
)
excalibur = Weapon(
    name="Excalibur",
    description="Long Sword, good for Goblins",
    value=50,
    slot_size=1,
    required_strength=15,
    required_dexterity=15,
    allowed_race="Human",
    max_durability=10,
    durability=2,
    inventory=Inventory,
    damage_type="Fire",
    damage=10,
    is_equipped=False,
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
quest = Quest(
    name="Find Blueberries.",
    description="Find 7 Blueberries in the Forest.",
    reward={"Blueberry": 7},
    completed=False,
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


# test for Hero class
def test_hero_creation():
    assert player.name == "Thorin Oakenshield"
    assert player.level == 1
    assert player.experience == 0
    assert player.race == "Dwarf"
    assert player.max_health == 150
    assert player.health == 100
    assert player.strength == 15
    assert player.dexterity == 8
    assert player.defense == 5
    assert player.statuses == "Sick"
    assert player.inventory.items == []
    assert player.max_mana == 20
    assert player.mana == 10


# test for Enemy class
def test_enemy_creation():
    assert enemy.name == "Azog The Defiler"
    assert enemy.level == 1
    assert enemy.experience == 0
    assert enemy.race == "Orc"
    assert enemy.max_health == 70
    assert enemy.health == 70
    assert enemy.strength == 10
    assert enemy.dexterity == 5
    assert enemy.defense == 10
    assert enemy.statuses == "Stunned"
    assert enemy.inventory.items == []
    assert enemy.weakness == "Cold"
    assert enemy.resistance == "Fire"


# test weapon creation
def test_weapon_creation():
    assert excalibur.name == "Excalibur"
    assert excalibur.description == "Long Sword, good for Goblins"
    assert excalibur.value == 50
    assert excalibur.slot_size == 1
    assert excalibur.required_strength == 15
    assert excalibur.required_dexterity == 15
    assert excalibur.allowed_race == "Human"
    assert excalibur.damage_type == "Fire"
    assert excalibur.damage == 10


# test armor creation
def test_armor_creation():
    armor = leather_armor
    assert armor.name == "Leather Jacket"
    assert armor.description == "Good for Humans"
    assert armor.value == 30
    assert armor.slot_size == 1
    assert armor.required_strength == 5
    assert armor.required_dexterity == 0
    assert armor.allowed_race == "Human"
    assert armor.resistance == "Cold"
    assert armor.protection == 5
    assert armor.is_equipped == False


# test create and complete quest
def test_quest_creation():
    assert quest.name == "Find Blueberries."
    assert quest.description == "Find 7 Blueberries in the Forest."
    assert quest.reward == {"Blueberry": 7}
    assert quest.completed == False
    quest.complete_quest()
    assert quest.completed == True


# test weapon equip
def test_equip_weapon():
    assert player.strength == 15
    player.equip_weapon(excalibur)
    assert excalibur.is_equipped == True
    player.unequip_weapon(excalibur)
    assert excalibur.is_equipped == False
    assert player.strength == 15


# test armor equip
def test_equip_armor():
    assert player.defense == 5
    player.equip_armor(leather_armor)
    assert leather_armor.is_equipped == True
    player.unequip_armor(leather_armor)
    assert leather_armor.is_equipped == False
    assert player.defense == 5


# test add to inventory, degrade, destroy, remove from inventory
def test_inventory_add_degrade_destroy():
    inventory = Inventory(slots=20)
    inventory.add_item(excalibur)  # takes up 1 slot
    inventory.add_item(leather_armor)  # takes up 1 slot
    inventory.upgrade(5)  # add 5 slots
    print(inventory.items)
    assert inventory.items == [excalibur, leather_armor]
    assert inventory.slots == 23
    assert excalibur in inventory.items
    assert leather_armor in inventory.items
    assert "Hammer" not in inventory.items
    excalibur.degrade(player)
    assert excalibur.durability == 1
    excalibur.destroy()
    assert inventory.items == [leather_armor]


# test taking damage by player and enemy
def test_take_damage():
    player.take_damage(enemy.strength)
    assert player.health == 90
    assert player.is_alive == True
    player.take_damage(enemy.strength)
    assert player.is_alive == True
    player.take_damage(enemy.strength + 80)
    assert player.is_alive == False


# test for battle system and die if health =< 0
def test_battle():
    player.health = 100
    enemy.health = 70
    battle = Battle(player, enemy)
    assert battle.turn == 0
    player.attack(enemy)
    assert enemy.health == 65
    enemy.attack(player)
    assert player.health == 95
    player.equip_weapon(excalibur)
    player.attack(enemy)


# test consumables
def test_consumables():
    inventory = Inventory([], 5, 20)
    inventory.add_item(life_potion)
    inventory.add_item(boost_potion)
    inventory.add_item(strength_potion)
    assert player.health == 95
    assert player.mana == 10
    assert player.strength == 25
    assert life_potion in inventory.items
    player.use_consumable(life_potion)
    assert player.health == 115
    assert inventory.items == [boost_potion, strength_potion]
    player.use_consumable(boost_potion)
    assert player.health == 150
    assert player.mana == 20
    assert inventory.items == [strength_potion]
    player.use_consumable(strength_potion)
    assert player.strength == 40
    assert inventory.items == []


# test treasure chest
def test_treasure_chest():
    chest = TreasureChest(items=[excalibur])
    assert chest.items == [excalibur]
