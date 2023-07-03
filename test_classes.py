import pytest
from classes import *


player = Hero(
    "Jimi Hendrix",
    1,
    0,
    "Human",
    150,
    27,
    10,
    8,
    5,
    129,
    "Sick",
    None,
    10,
)
enemy = Enemy(
    "Azog",
    1,
    0,
    "Goblin",
    70,
    70,
    10,
    5,
    10,
    21,
    "Alive",
    None,
    "Cold",
    "Fire",
)
excalibur = Weapon(
    "Excalibur",
    "Long Sword, good for Goblins",
    50,
    1,
    15,
    15,
    "Human",
    40,
    "Fire",
    10,
)
leather_armor = Armor(
    "Leather Jacket",
    "Good for Humans",
    30,
    1,
    5,
    0,
    "Human",
    15,
    "Cold",
    5,
)
quest = Quest(
    "Find Blueberries.",
    "Find 7 Blueberries in the Forest.",
    "Town Medic",
    (7, "Blueberry"),
    False,
)


# test for Hero class
def test_hero_creation():
    assert player.name == "Jimi Hendrix"
    assert player.level == 1
    assert player.experience == 0
    assert player.race == "Human"
    assert player.max_health == 150
    assert player.health == 27
    assert player.strength == 10
    assert player.dexterity == 8
    assert player.armor == 5
    assert player.gold == 129
    assert player.status == "Sick"
    assert player.inventory == None
    assert player.max_health == 150
    assert player.mana == 10


# test for Enemy class
def test_enemy_creation():
    assert enemy.name == "Azog"
    assert enemy.level == 1
    assert enemy.experience == 0
    assert enemy.race == "Goblin"
    assert enemy.max_health == 70
    assert enemy.health == 70
    assert enemy.strength == 10
    assert enemy.dexterity == 5
    assert enemy.armor == 10
    assert enemy.gold == 21
    assert enemy.status == "Alive"
    assert enemy.inventory == None
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
    excalibur.value += 12
    assert excalibur.value == 62


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


# test add weapon object to inventory
def test_add_weapon_to_inventory():
    inventory = Inventory([], 20)
    inventory.add_item_to_inventory(excalibur)
    inventory.add_item_to_inventory(leather_armor)
    inventory.upgrade_inventory(5)
    assert inventory.items == [excalibur, leather_armor]
    assert inventory.slots == 25
    assert excalibur in inventory.items
    assert leather_armor in inventory.items
    assert "Hammer" not in inventory.items


# test create and complete quest
def test_quest_creation():
    assert quest.name == "Find Blueberries."
    assert quest.description == "Find 7 Blueberries in the Forest."
    assert quest.giver == "Town Medic"
    assert quest.reward == (7, "Blueberry")
    assert quest.completed == False
    quest.complete_quest()
    assert quest.completed == True


# test weapon equip
def test_equip_weapon():
    assert player.strength == 10
    player.equip_weapon(excalibur)
    assert player.strength == 20
    player.unequip_weapon(excalibur)
    assert player.strength == 10


# test armor equip
def test_equip_armor():
    assert player.armor == 5
    player.equip_armor(leather_armor)
    assert player.armor == 10
    player.unequip_armor(leather_armor)
    assert player.armor == 5
