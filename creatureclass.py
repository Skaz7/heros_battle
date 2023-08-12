from dataclasses import dataclass, field
from inventory import Inventory, Item, Weapon, Armor, Consumable
from spellbook import SpellBook
from decorators import *
from classes import Dice, Quest
from infos import print_full_stats


@dataclass
class Status:
    name: str
    description: str
    duration: int
    attribute_to_change: str
    modification_value: int

    def reset(self):
        duration = 0


@dataclass
class Creature:
    """Initializes a new instance of Creature class.
    Player & Enemy classes are a subclasses of Creature class."""

    name: str = "Creature"
    level: int = 1
    experience: int = 0
    race: str = None
    max_health: int = 100
    health: int = 100
    strength: int = 10
    dexterity: int = 10
    defense: int = 10
    statuses: list = field(default_factory=list[Status])
    inventory: Inventory = Inventory()
    is_alive: bool = True
    spellbook: SpellBook = SpellBook()

    # ####### Getters and setters ########

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
    def defense(self):
        return self._defense

    @property
    def statuses(self):
        return self._statuses

    @property
    def inventory(self):
        return self._inventory

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def spellbook(self):
        return self._spellbook

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

    @defense.setter
    def defense(self, new_defense):
        self._defense = new_defense

    @statuses.setter
    def statuses(self, new_statuses):
        self._statuses = new_statuses

    @inventory.setter
    def inventory(self, new_inventory):
        self._inventory = new_inventory

    @is_alive.setter
    def is_alive(self, new_is_alive):
        self._is_alive = new_is_alive

    @spellbook.setter
    def spellbook(self, new_spellbook):
        self._spellbook = new_spellbook

    # ####### Methods ########

    def heal(self, additional_health):
        self.health += additional_health

    def take_damage(self, damage):
        if damage > 0:
            self.health -= damage
        if self.health < 0:
            self.health = 0
            self.status = "dead"
            self.is_alive = False

    def attack(self, defender):
        """Attack method for both players.
        Damage dealt to defender is based on the attacker's strength and additional damage provided by equipped weapon.
        If the defender is defending, the damage dealt is reduced by the defender's armor.
        If the defender's health is reduced to 0 or below, the attacker wins.
        """
        for weapon in self.inventory.items:
            if isinstance(weapon, Weapon) and weapon.is_equipped:
                print_green(f"{self.name} is holding {weapon.name}")
                weapon.degrade(self)

        for armor in defender.inventory.items:
            if isinstance(armor, Armor) and armor.is_equipped:
                print_green(f"{defender.name} wears {armor.name}")
                additional_protection = armor.protection
                armor.degrade(self)

        damage = self.strength - defender.defense
        defender.take_damage(damage)
        print(f"\n{self.name} attacks {defender.name} for {damage} damage!\n")

    def defend(self):
        self.defense = int(self.defense * 1.5)
        print(f"\n{self.name} is defending!\n")
        print(f"{self.name}'s armor is now {self.defense}!\n")

    def use_magic(self, defender):
        """Use magic method for both players."""
        print(f"\nSpells in your spellbook: ")
        print("-------------------------")
        self.spellbook.show()
        choice = input("Which spell would you like to use?\n > ")
        self._use_magic_choice_handler(choice, defender)

    def _use_magic_choice_handler(self, choice, defender):
        if choice == "0":
            return
        else:
            spell = self.spellbook.spells[int(choice) - 1]
        if self.mana < spell.mana_cost:
            print_red(f"You don't have enough mana to cast {spell.name}!\n")
            self.use_magic(defender)
        else:
            spell.cast(self, defender)

    def flee(self):
        dice = Dice()
        flee_chance = dice.roll("1d10")
        print(f"You rolled {flee_chance}")
        if flee_chance <= 2:
            print_red(
                f"\n{self.name} get hurt while running from battle and failed to escape!\n"
            )
            self.health -= int(self.max_health / 20)
            return
        elif 2 < flee_chance <= 9:
            print(f"\n{self.name} failed to escape from the battlefield!\n")
            return
        elif 9 < flee_chance <= 10:
            print_green(f"\n{self.name} escaped from the battlefield!\n")
            exit()

    def handle_statuses(self):
        for status in self.statuses:
            if status.duration > 0:
                setattr(
                    self,
                    status.attribute_to_change,
                    max(
                        0,
                        getattr(self, status.attribute_to_change)
                        - status.modification_value,
                    ),
                )
                status.duration -= 1
                if status.attribute_to_change == "health" and self.health == 0:
                    self.is_alive = False

    def equip_armor(self, armor):
        """Equips an armor to the Creature."""
        armor.is_equipped = True
        self.defense += armor.protection

    def unequip_armor(self, armor):
        """Unequips an armor from the Creature."""
        armor.is_equipped = False
        self.defense -= armor.protection


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

    def equip_weapon(self, weapon):
        """Equips a weapon to the hero."""
        weapon.is_equipped = True
        self.strength += weapon.damage

    def unequip_weapon(self, weapon):
        """Unequips a weapon from the hero."""
        weapon.is_equipped = False
        self.strength -= weapon.damage

    def use_item(self):
        self.inventory.show()
        choice = int(input("> "))
        selected_item = self.inventory.items[choice - 1]
        selected_item.info()
        print(f"1 - Use {selected_item.name}?")
        print("0 - Go Back.\n")
        choice = int(input("> "))
        if choice == 1:
            # need to check if any other weapon is equipped, if so, unequip it and equip new one
            if isinstance(selected_item, Weapon):
                for weapon in self.inventory.items:
                    if isinstance(weapon, Weapon) and weapon.is_equipped:
                        self.unequip_weapon(weapon)
                if selected_item.durability <= 0:
                    print(f"{selected_item.name} is broken and can't be used!")
                    return
                else:
                    self.equip_weapon(selected_item)
            elif isinstance(selected_item, Armor):
                self.equip_armor(selected_item)
            elif isinstance(selected_item, Consumable):
                self.use_consumable(selected_item)
            return
        elif choice == 0:
            return
        else:
            print("Wrong choice! Please repeat.")
            self.use_item()

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

    def open_chest(self, chest):
        chest.opened = True
        choice = None
        while choice != 0:
            chest.show_items()
            choice = int(input(" > "))
            chest.choice_handler(choice, self.inventory)

    def put_item(self, item, chest):
        self.inventory.remove_item(item)
        chest.add_item(item)

    def level_up(self):
        if self.level % 5 == 0:
            points_to_spend = 8
        else:
            points_to_spend = 4
        self.level += 1
        self.max_health = int(self.max_health * 1.1)
        self.health += self.max_health
        while points_to_spend > 0:
            self._level_up_menu()
            print(f"\nYou have {points_to_spend} points to spend.")
            choice = int(input("\nWhich statistic do you want to increase?  -> "))
            self._level_up_choice_handler(choice)
            if choice != 0:
                points_to_spend -= 1

    def _level_up_menu(self):
        print_one_line_in_frame(f"{self.name} leveled up!")
        print(f"\n    1. Strength ({self.strength})")
        print(f"    2. Dexterity ({self.dexterity})")
        print(f"    3. Armor ({self.defense})")
        print(f"    4. Mana ({self.max_mana})")
        print("\n    0. Go Back.")

    def _level_up_choice_handler(self, choice):
        if choice == 1:
            self.strength += 1
        elif choice == 2:
            self.dexterity += 1
        elif choice == 3:
            self.defense += 1
        elif choice == 4:
            self.max_mana += 1
        elif choice == 0:
            return
        else:
            print("Wrong choice! Please repeat.")
            self._level_up_choice_handler(choice)

    def repair_item(self, item: Item) -> None:
        repair_cost = int(item.value * 0.25)
        if self.inventory.gold < repair_cost:
            print(f"You don't have enought gold to repair {item.name}...")
        else:
            self.inventory.gold -= repair_cost
            item.durability = item.max_durability
            print(f"\n{item.name} has been repaired.\n")


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

    def reveal_all(self):
        """Reveals all enemy attributes."""
        print_one_line_in_frame(f"{self.name} revealed!")
        print_full_stats(self)


@dataclass
class Npc:
    name: str = ""
    description: str = ""
    quest: Quest = Quest()

    def talk_to(self):
        print_yellow(f"\nYou talk to {self.name}.\n")

    def give_quest(self, quest):
        pass

    def give_reward(self, reward, player):
        pass
