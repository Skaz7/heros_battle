import pytest
from classes import *
from temp import *


# test for Hero class
def test_hero_creation():
    player = Hero(
        "Jimi Hendrix", 1, 0, "Human", 27, 10, 8, 5, 129, "Sick", None, 150, 10
    )
    assert player.name == "Jimi Hendrix"
    assert player.level == 1
    assert player.experience == 0
    assert player.race == "Human"
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
    enemy = Enemy(
        "Azog", 1, 0, "Goblin", 70, 10, 5, 10, 21, "Alive", None, "Cold", "Fire"
    )
    assert enemy.name == "Azog"
    assert enemy.level == 1
    assert enemy.experience == 0
    assert enemy.race == "Goblin"
    assert enemy.health == 70
    assert enemy.strength == 10
    assert enemy.dexterity == 5
    assert enemy.armor == 10
    assert enemy.gold == 21
    assert enemy.status == "Alive"
    assert enemy.inventory == None
    assert enemy.weakness == "Cold"
    assert enemy.resistance == "Fire"


# test for Inventory class
def test_inventory_creation():
    pass


# test weapon creation
def test_weapon_creation():
    weapon = Weapon("Excalibur", "Long Sword, good for Goblins", 50, 1, "Fire", 10)
    assert weapon.name == "Excalibur"
    assert weapon.description == "Long Sword, good for Goblins"
    assert weapon.value == 50
    assert weapon.slot_size == 1
    assert weapon.damage_type == "Fire"
    assert weapon.damage == 10

    weapon.value += 12
    assert weapon.value == 62


# test armor creation
def test_armor_creation():
    armor = Armor("Leather", "Good for Humans", 30, 1, "Cold", 5)
    assert armor.name == "Leather"
    assert armor.description == "Good for Humans"
    assert armor.value == 30
    assert armor.slot_size == 1
    assert armor.resistance == "Cold"
    assert armor.armor == 5

    armor.armor += 10
    assert armor.armor == 15


# test add weapon object to inventory
def test_add_weapon_to_inventory():
    inventory = Inventory([], 20)
    excalibur = Weapon("Excalibur", "Long Sword, good for Goblins", 50, 1, "Fire", 10)
    leather_armor = Armor("Leather", "Good for Humans", 30, 1, "Cold", 5)
    inventory.add_item_to_inventory(excalibur)
    inventory.add_item_to_inventory(leather_armor)
    inventory.upgrade_inventory(5)
    print(inventory.inventory)
    assert inventory.inventory == [excalibur, leather_armor]
    assert inventory.slots == 25
    assert excalibur in inventory.inventory
    assert leather_armor in inventory.inventory
    assert "Hammer" not in inventory.inventory
    