from data.characters import player
from classes import Dice
from spellbook import SpellBook
from data.spells import *
from data.statuses import *
from data.characters import *
from data.weapons import *
from data.objects import *
from data.world import *
from collections import OrderedDict
from infos import *
from data.world import *
from cli import *
import time
import platform


# Creating Player inventory
player.inventory = Inventory()

# Creating Player spellbook
player.spellbook = SpellBook()
player.spellbook.add_spell(freeze)
# print(player.spellbook.spells)


# Create Shop and test buy method
shop = Shop()
shop.stock.append(life_potion)
shop.stock.append(thorshammer)
shop.stock.append(boost_potion)
shop.stock.append(strength_potion)
shop.stock.append(elvisheyes)
shop.stock.append(leather_armor)
shop.show_stock()
print()
for item in player.inventory.items:
    print(item.name)
print()
shop.buy_item(player, 2)
shop.buy_item(player, 4)
print()
shop.show_stock()
print()
print(f"Hero's inventory - {[item.name for item in player.inventory.items]}")
print()
shop.show_stock()

# Create Temple and test heal and learn spell methods
temple = Temple(
    name="Temple",
    description="A temple with many items.",
    stock=[freeze, fireball],
)
print()
print([spell.name for spell in player.spellbook.spells])
temple.show_stock()
temple.learn_spell(player, fireball)
print([spell.name for spell in player.spellbook.spells])


print(
    [
        (item.name, item.durability, item.max_durability)
        for item in player.inventory.items
    ]
)
thorshammer.durability -= 10
print(
    [
        (item.name, item.durability, item.max_durability)
        for item in player.inventory.items
    ]
)

player.repair_item(thorshammer)
print(
    [
        (item.name, item.durability, item.max_durability)
        for item in player.inventory.items
    ]
)


# CHECK PLAYER STATUS WITH DURATION
bleed = Status(
    name="Bleed",
    description="Causes bleeding for 3 turns",
    duration=3,
    attribute_to_change="health",
    modification_value=5,
)

poison = Status(
    name="Poison",
    description="Causes poison for 4 turns",
    duration=4,
    attribute_to_change="health",
    modification_value=2,
)

player.statuses.append(bleed)
print(player.health)
print([status.name for status in player.statuses])
player.handle_statuses()
print(player.health)
player.statuses.append(poison)
player.handle_statuses()
print([status.name for status in player.statuses])
print(player.health)
