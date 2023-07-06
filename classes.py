import random
from dataclasses import dataclass
import time
from dataclasses import field


@dataclass
class Dice:
    """Simulates a dice roll of n-sides."""

    def roll(self, sides):
        return random.randint(1, sides)


class Inventory:
    def __init__(self, items: list = [], slots: int = 10, gold: int = 20):
        self.items = items
        self.slots = slots
        self.gold = gold  # gold is not an item and takes no slot space

    def __reppr__(self):
        return f"Inventory: {self.items}"

    def show(self):
        """Prints all items from inventory."""
        print(f"\n    Items in your inventory:")
        for i, item in enumerate(self.items, start=1):
            print(f"\t\t\t    {i}. {item.name} - {item.description}")

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
    status: str = None
    inventory: Inventory = Inventory()
    is_alive: bool = True

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
    def status(self):
        return self._status

    @property
    def inventory(self):
        return self._inventory
    
    @property
    def is_alive(self):
        return self._is_alive

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

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @inventory.setter
    def inventory(self, new_inventory):
        self._inventory = new_inventory
    
    @is_alive.setter
    def is_alive(self, new_is_alive):
        self._is_alive = new_is_alive

    def heal(self, additional_health):
        self.health += additional_health

    def take_damage(self, damage):
        if damage > 0:
            self.health -= damage
        if self.health < 0:
            self.health = 0
            self.is_alive = False


@dataclass
class Hero(Creature):
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

    def equip_weapon(self, weapon):
        """Equips a weapon to the hero."""
        self.strength += weapon.damage
        weapon.is_equipped = True

    def unequip_weapon(self, weapon):
        """Unequips a weapon from the hero."""
        self.strength -= weapon.damage
        weapon.is_equipped = False

    def equip_armor(self, armor):
        """Equips an armor to the hero."""
        self.armor += armor.protection
        armor.is_equipped = True

    def unequip_armor(self, armor):
        """Unequips an armor from the hero."""
        self.armor -= armor.protection
        armor.is_equipped = False

    def use_consumable(self, consumable):
        """Boosts player statistics based on item description."""
        if consumable.heal > 0:
            self.heal(consumable.heal)
        if consumable.mana > 0:
            self.mana += consumable.mana
        if consumable.strength > 0:
            self.strength += consumable.strength
        if consumable.dexterity > 0:
            self.dexterity += consumable.dexterity
        consumable.destroy()


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
