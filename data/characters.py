from creatureclass import Hero, Enemy, Npc
from data.quests import find_dog
from inventory import Inventory, Weapon, Armor
from spellbook import SpellBook
from data.statuses import *

# Create Hero and Enemy
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
    statuses=[],
    inventory=Inventory(),
    is_alive=True,
    spellbook=SpellBook(),
    max_mana=20,
    mana=10,
)
enemy = Enemy(
    name="Azog The Defiler",
    level=1,
    experience=20,
    race="Orc",
    max_health=70,
    health=70,
    strength=10,
    dexterity=5,
    defense=10,
    statuses=[],
    inventory=Inventory(),
    is_alive=True,
    spellbook=SpellBook(),
    weakness="Cold",
    resistance="Fire",
)

thomas = Npc(
    name="Thomas",
    description="Town merchant",
    quest=find_dog,
)
