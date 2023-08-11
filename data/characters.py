from creatureclass import Hero, Enemy, Npc
from data.quests import find_dog
from inventory import Inventory
from spellbook import SpellBook

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
    armor=5,
    status="Sick",
    inventory=Inventory(),
    is_alive=True,
    spellbook=SpellBook(),
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
    armor=10,
    status="Stunned",
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
