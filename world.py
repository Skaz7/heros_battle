from dataclasses import dataclass, field
from items import Item, Inventory


class Store:
    name: str = ""
    description: str = ""
    stock: Inventory = Inventory()
    discount: int = 0

    def show_stock(self):
        pass


@dataclass
class Shop(Store):
    def show_stock(self):
        for i, item in enumerate(self.stock.items, start=1):
            print(f"{i}. {item.name} - ${item.price}")


@dataclass
class Temple(Store):
    def show_stock(self):
        for i, item in enumerate(self.stock.items, start=1):
            print(f"{i}. {item.name} - ${item.price}")

    def heal_player(self, player):
        player.health = player.max_health

    def learn_spell(self, spell):
        if spell.required_level <= player.level:
            player.spellbook.add_spell(spell)


@dataclass
class Blacksmith(Store):
    def show_stock(self):
        for i, item in enumerate(self.stock.items, start=1):
            print(f"{i}. {item.name} - ${item.price}")

    def repair_weapon(self, weapon):
        repair_cost = int(weapon.value * 0.25)
        weapon.durability = weapon.max_durability

    def repair_armor(self, armor):
        repair_cost = int(armor.value * 0.25)
        armor.durability = armor.max_durability


@dataclass
class Area:
    name: str = ""
    description: str = ""
    available_directions: list = field(default_factory=list)
    enemies: list = field(default_factory=list)
    treasures: list = field(default_factory=list)
    npcs: list = field(default_factory=list)
    store: Store = Store()
    visited: bool = False
