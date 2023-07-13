from dataclasses import dataclass
from items import Inventory
from spellbook import SpellBook
from decorators import print_one_line_in_frame, slow_print


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
    spellbook: SpellBook = SpellBook()

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

    def print_battle_stats(self):
        print()
        print_one_line_in_frame(f"{self.name} Stats:")
        slow_print(f"    Health : {self.health}/{self.max_health}\n")
        slow_print(f"    Experience : {self.experience}\n")
        slow_print(f"    Level : {self.level}\n\n")


@dataclass
class Hero(Creature):
    max_mana: int = 20
    mana: int = 10

    @property
    def max_mana(self):
        return self._max_mana

    @property
    def mana(self):
        return self._mana

    @max_mana.setter
    def max_mana(self, new_max_mana):
        self._max_mana = new_max_mana

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
        if self.health + consumable.heal > self.max_health:
            self.health = self.max_health
        else:
            self.heal(consumable.heal)

        if self.mana + consumable.mana > self.max_mana:
            self.mana = self.max_mana
        else:
            self.mana += consumable.mana

        self.strength += consumable.strength

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
