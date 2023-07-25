from dataclasses import dataclass
import time


class Inventory:
    def __init__(self, items: list = [], slots: int = 10, gold: int = 20):
        self.items = items
        self.slots = slots
        self.gold = gold  # gold is not an item and takes no slot space

    def __reppr__(self):
        return f"Inventory: {self.items}"

    def show(self):
        """Prints all items from inventory."""
        print(f"\n    Items in inventory:")
        for i, item in enumerate(self.items, start=1):
            print(f"\t\t\t    {i}. {item.name} - {item.description}")
        print()

    def add_item(self, item):
        """Adds a new item to the inventory.
        If the inventory is full, which means that remain inventory slots is lower than item slot size, the item is not added.
        If the inventory is not full, the item is added to the inventory and the inventory slots are reduced by item slot size.
        """
        if self.slots < item.slot_size:
            print("You don't have enough space in your inventory inventory.")
            time.sleep(1)
            return
        self.slots -= item.slot_size
        item.set_inventory(self)
        self.items.append(item)

    def remove_item(self, item):
        """Removes an item from the inventory.
        Number of free slots in inventory is increased by item slot size.
        Item is removed from the inventory.
        """
        self.slots += item.slot_size
        self.items.remove(item)

    def upgrade(self, slots):
        """Upgrades number of inventory slots."""
        self.slots += slots


@dataclass
class Item:
    name: str
    description: str
    value: int
    slot_size: int
    required_strength: int
    required_dexterity: int
    allowed_race: str
    max_durability: int
    durability: int
    inventory: Inventory = None

    def set_inventory(self, inventory):
        self.inventory = inventory

    def degrade(self):
        self.durability -= 1
        if self.durability == 0:
            if isinstance(self, Weapon):
                print(f"Your {self.name} is broken down.")
                self.name = (
                    self.name + f" \033[0;31m(DESTROYED - can't be used.) \033[0m"
                )
                self.damage = 0
            elif isinstance(self, Armor):
                print(f"Your {self.name} is broken down.")
                self.protection = 0
            elif isinstance(self, Consumable):
                self.destroy()

    def destroy(self) -> None:
        self.inventory.remove_item(self)
        print(f"Your {self.name} has been destroyed.")
        return

    def repair(self) -> None:
        self.durability = self.max_durability
        print(f"Your {self.name} has been repaired.")
        return

    def use(self):
        if isinstance(self, Weapon):
            self.player.equip_weapon(self)
        elif isinstance(self, Armor):
            self.player.equip_armor(self)
        elif isinstance(self, Consumable):
            self.player.use_consumable(self)

    def info(self):
        print()
        for key, value in self.__dict__.items():
            if not "inventory" in key and not "is_equipped" in key:
                print(f"{key:19}: {value}".title().replace("_", " "))
        print()


@dataclass
class Weapon(Item):
    """Initializes a Weapon Item.
    Weapon can be used to increase player's attack.
    Weapon can be used to increase player's damage to a certain damage type."""

    damage_type: str = ""
    damage: int = 10
    is_equipped: bool = False


@dataclass
class Armor(Item):
    """Initializes a Armor Item.
    Armor can be used to increase player's defense.
    Armor can be used to increase player's resistance to a certain damage type."""

    resistance: str = ""
    protection: int = 0
    is_equipped: bool = False


@dataclass
class Consumable(Item):
    """Initializes a Consumable Item.
    Consuming one of this items will upgrade player statistics.
    Upgrade can be temporary or permanent, depending of the item."""

    heal: int = 0
    mana: int = 0
    strength: int = 0
    dexterity: int = 0
