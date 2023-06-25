import pytest
from classes import *


def test_creature_creation():
    creature = Creature()
    assert creature.name == "Hero"
    assert creature.level == 1
    assert creature.experience == 0
    assert creature.race == None
    assert creature.health == 100
    assert creature.strength == 10
    assert creature.dexterity == 10
    assert creature.armor == 10
    assert creature.gold == 10
    assert creature.status == None
    assert creature.inventory == None


def test_hero_creation():
    hero = Hero()
    assert hero.name == "Hero"
    assert hero.level == 1
    assert hero.experience == 0
    assert hero.race == None
    assert hero.health == 100
    assert hero.strength == 10
    assert hero.dexterity == 10
    assert hero.armor == 10
    assert hero.gold == 10
    assert hero.status == None
    assert hero.inventory == None
    assert hero.max_health == 100
    assert hero.mana == 10


def test_enemy_creation():
    enemy = Enemy()
    assert enemy.name == "Hero"
    assert enemy.level == 1
    assert enemy.experience == 0
    assert enemy.race == None
    assert enemy.health == 100
    assert enemy.strength == 10
    assert enemy.dexterity == 10
    assert enemy.armor == 10
    assert enemy.gold == 10
    assert enemy.status == None
    assert enemy.inventory == None
    assert enemy.weakness == None
    assert enemy.resistance == None
