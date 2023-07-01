import random
from dataclasses import dataclass
import time
from dataclasses import field


@dataclass
class Dice:
    """Simulates a dice roll of n-sides."""

    def roll(self, sides):
        return random.randint(1, sides)


@dataclass
class Creature:
    """Initializes a new instance of Creature class.
    Player & Enemy classes are a subclasses of Creature class."""

    name: str = "Hero"
    level: int = 1
    experience: int = 0
    race: str = None
    max_health: int = 100
    health: int = 100
    strength: int = 10
    dexterity: int = 10
    armor: int = 10
    gold: int = 10
    status: str = None
    inventory: list = field(default_factory=list)

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def experience(self):
        return self._experience

    @property
    def race(self):
        return self._race

    @property
    def max_health(self):
        return self._max_health

    @property
    def health(self):
        return self._health

    @property
    def strength(self):
        return self._strength

    @property
    def dexterity(self):
        return self._dexterity

    @property
    def armor(self):
        return self._armor

    @property
    def gold(self):
        return self._gold

    @property
    def status(self):
        return self._status

    @property
    def inventory(self):
        return self._inventory

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @level.setter
    def level(self, new_level):
        self._level = new_level

    @experience.setter
    def experience(self, new_experience):
        self._experience = new_experience

    @race.setter
    def race(self, new_race):
        self._race = new_race

    @max_health.setter
    def max_health(self, new_max_health):
        self._max_health = new_max_health

    @health.setter
    def health(self, new_health):
        self._health = new_health

    @strength.setter
    def strength(self, new_strength):
        self._strength = new_strength

    @dexterity.setter
    def dexterity(self, new_dexterity):
        self._dexterity = new_dexterity

    @armor.setter
    def armor(self, new_armor):
        self._armor = new_armor

    @gold.setter
    def gold(self, new_gold):
        self._gold = new_gold

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @inventory.setter
    def inventory(self, new_inventory):
        self._inventory = new_inventory

    def take_damage(self, damage):
        if damage > 0:
            self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


@dataclass
class Hero(Creature):
    max_health: int = 100
    mana: int = 10

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        self._mana = new_mana

    def level_up(self):
        print(f"\n{self.name} leveled up!\n")
        self.level += 1
        self.max_health += 10
        self.health += 10
        self.strength += 2
        self.dexterity += 2
        self.mana += 2


@dataclass
class Enemy(Creature):
    weakness: str = None
    resistance: str = None

    @property
    def weakness(self):
        return self._weakness

    @property
    def resistance(self):
        return self._resistance

    @weakness.setter
    def weakness(self, new_weakness):
        self._weakness = new_weakness

    @resistance.setter
    def resistance(self, new_resistance):
        self._resistance = new_resistance


class Inventory:
    def __init__(self, items: list = [], slots: int = 10):
        """Initializes a new inventory with 5 item slots.
        It is possible to upgrade number of slots to carry more items
        """
        self.items = items
        self.slots = slots

    def __reppr__(self):
        return f"Inventory: {self.items}"

    def show_inventory(self):
        """Prints all items from inventory."""
        print(f"\nItems in your inventory:\n")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.name}")

    def add_item_to_inventory(self, item):
        """Adds a new item to the inventory."""
        self.items.append(item)

    def remove_item_from_inventory(self, item):
        """Removes a item from the inventory."""
        self.items.remove(item)

    def upgrade_inventory(self, additional_slots: int = 0):
        """Upgrades number of inventory slots."""
        self.slots += additional_slots


@dataclass
class Item:
    """Initializes a Item.
    Item can be used to increase player's statistics.
    It can be Weapon, Armor or Consumable class.
    """

    name: str
    description: str
    value: int
    slot_size: int
    required_strength: int
    required_dexterity: int
    allowed_race: str


@dataclass
class Weapon(Item):
    """Initializes a Weapon Item.
    Weapon can be used to increase player's attack.
    Weapon can be used to increase player's damage to a certain damage type."""

    damage_type: str
    damage: int


@dataclass
class Armor(Item):
    """Initializes a Armor Item.
    Armor can be used to increase player's defense.
    Armor can be used to increase player's resistance to a certain damage type."""

    resistance: str
    armor: int


@dataclass
class Consumable(Item):
    """Initializes a Consumable Item.
    Consuming one of this items will upgrade player statistics.
    Upgrade can be temporary or permanent, depending of the item."""

    heal: int
    mana: int
    strength: int
    dexterity: int


class Spell:
    pass


class Status:
    def __init__(self, name: str, description: str, duration: int):
        self.name = name
        self.description = description
        self.duration = duration


class HealthBar:
    def __init__(self, creature):
        self.player = creature
        self.max_health = creature.max_health
        self.current_health = creature.health

    def draw_health_bar(self):
        self.max_health = self.player.max_health
        self.current_health = self.player.health

        if self.current_health >= self.max_health * 0.7:
            health_bar_color = "\033[0;32m"
        elif 0.7 * self.max_health > self.current_health >= self.max_health * 0.3:
            health_bar_color = "\033[0;33m"
        elif self.current_health < self.max_health * 0.3:
            health_bar_color = "\033[0;31m"

        health_size = int((self.current_health / self.max_health) * 100)

        print(
            f"Health: {health_bar_color}{self.current_health}/{self.max_health}  ",
            end="",
        )
        print(f"[{health_size * '█'}{(100- health_size) * '-'}] \033[0m")


@dataclass
class Quest:
    name: str = ""
    description: str = ""
    giver: str = ""
    reward: tuple = ()
    completed: bool = False

    def complete_quest(self):
        self.completed = True
