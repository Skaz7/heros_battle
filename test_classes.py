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
