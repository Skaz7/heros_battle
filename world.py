from dataclasses import dataclass, field
from items import Inventory
from objects import *
from cli import *


@dataclass
class Store:
    name: str = ""
    description: str = ""
    stock: Inventory = Inventory()
    discount: int = 0

    def show_stock(self) -> None:
        shop_menu(self)


@dataclass
class Shop(Store):
    def buy_item(self, player, item_index):
        item = self.stock.items[item_index - 1]
        player.inventory.add_item(item)
        self.stock.remove_item(item)
        print(f"You bought {self.stock}!")


@dataclass
class Temple(Store):
    def heal_player(self, player):
        player.health = player.max_health

    def learn_spell(self, player, spell):
        if spell.required_level <= player.level:
            player.spellbook.add_spell(spell)


@dataclass
class Blacksmith(Store):
    def repair_weapon(self, weapon):
        repair_cost = int(weapon.value * 0.25)
        weapon.durability = weapon.max_durability

    def repair_armor(self, armor):
        repair_cost = int(armor.value * 0.25)
        armor.durability = armor.max_durability

    def buy_item(self, player, item_index):
        item = self.stock.items[item_index - 1]
        player.inventory.add_item(item)
        self.stock.remove_item(item)
        print(f"You bought {item.name}!")


@dataclass
class Area:
    name: str = ""
    description: str = ""
    available_directions: list = field(default_factory=list)
    enemies: list = field(default_factory=list)
    treasures: Chest = Chest()
    npcs: list = field(default_factory=list)
    store: Store = Store()
    visited: bool = False
