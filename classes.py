import random
from dataclasses import dataclass
import time
from dataclasses import field


@dataclass
class Creature:
    """Initializes a new instance of Creature class.
    Player & Enemy classes are a subclasses of Creature class."""

    name: str = "Hero"
    level: int = 1
    experience: int = 0
    race: str = None
    health: int = 100
    strength: int = 10
    dexterity: int = 10
    armor: int = 10
    gold: int = 10
    status: str = None
    inventory: dict = None

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

    def level_up(self):
        print(f"\n{self.name} leveled up!\n")
        self.level += 1
        self.max_health += 10
        self.health += 10
        self.strength += 2
        self.dexterity += 2
        self.mana += 2

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
    def max_health(self):
        return self._max_health

    @property
    def mana(self):
        return self._mana

    @max_health.setter
    def max_health(self, new_max_health):
        self._max_health = new_max_health

    @mana.setter
    def mana(self, new_mana):
        self._mana = new_mana


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


class Battle:
    turn = 0

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_turn(self):
        print(f"\n{self.player.name} vs {self.enemy.name}\n")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Item")
        print("4. Flee")
        print("0. End Game")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.attack(self.player, self.enemy)
        elif choice == "2":
            self.defend(self.player)
        elif choice == "3":
            self.use_item()
        elif choice == "4":
            self.flee()
        elif choice == "0":
            self.end()
        else:
            print("Invalid choice!")
            time.sleep(2)
            self.player_turn()

    def enemy_turn(self):
        print(f"\n{self.enemy.name} vs {self.player.name}\n")
        self.attack(self.enemy, self.player)

    def attack(self, attacker, defender):
        """Attack method for both players.
        Damage dealt to defender is based on the attacker's strength and additional damage provided by equipped weapon.
        If the defender is defending, the damage dealt is reduced by the defender's armor.
        If the defender's health is reduced to 0 or below, the attacker wins.
        """
        base_attack = attacker.strength
        additional_attack = 0
        total_attack = base_attack + additional_attack
        damage = total_attack - defender.armor
        if damage < 0:
            damage = 0
        defender.health -= damage
        print(f"\n{attacker.name} attacks {defender.name} for {damage} damage!\n")
        if defender.health <= 0:
            self.win()

    def defend(self, defender):
        defender.armor = int(defender.armor * 1.5)
        print(f"\n{defender.name} is defending!\n")

    def use_item(self):
        self.player.inventory.show_inventory()
        choice = int(input("> "))
        equipped_weapon = self.player.inventory[choice - 1]

    def flee(self):
        flee_chance = random.randint(1, 10)
        if flee_chance <= 2:
            print(
                f"\n{self.player.name} get hurt while running from battle and failed to escape!\n"
            )
            self.player.health -= int(self.player.max_health / 20)
            return
        elif 2 < flee_chance <= 5:
            print(f"\n{self.player.name} failed to escape from the battlefield!\n")
            return
        elif 5 < flee_chance <= 10:
            print(f"\n{self.player.name} escaped from the battlefield!\n")
            exit()

    def win(self):
        pass

    def lose(self):
        pass

    def end(self):
        exit()


class Inventory:
    def __init__(self, inventory: list = [], slots: int = 5):
        """Initializes a new inventory with 5 item slots.
        It is possible to upgrade number of slots to carry more items
        """
        self.inventory = inventory
        self.slots = slots

    def show_inventory(self):
        """Prints all items from inventory."""
        print(f"\nItems in your inventory:\n")
        for i, item in enumerate(self.inventory, start=1):
            print(f"{i}. {item.name}")

    def add_item_to_inventory(self, item):
        """Adds a new item to the inventory."""
        self.inventory.append(item)

    def remove_item_from_inventory(self, item):
        """Removes a item from the inventory."""
        self.inventory.remove(item)

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
