from dataclasses import dataclass, field
from inventory import Inventory, Item, Weapon, Armor, Consumable
from spellbook import SpellBook
from decorators import *
from classes import Dice, Quest
import time
import os


def clear_screen():
    os.system("clear")


@dataclass
class Status:
    """Class for storing player status, which is handled during battles."""

    name: str
    description: str
    duration: int
    attribute_to_change: str
    modification_value: int

    def reset(self):
        self.duration = 0


@dataclass
class Creature:
    """Initializes a new instance of Creature class.
    Player & Enemy classes are a subclasses of Creature class.
    :param name: name of creature
    :param experience: actual experience of player, or enemy experience to gain by player after defeating enemy

    """

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
    equipped_weapon = None
    equipped_armor = None

    # ####### Methods ########

    def show_info(self):
        """
        Shows all available information about Creature object (player or enemy).
        Takes dictionary from Class attributes and prints it by key - value.
        Inventory, SpellBook and Statuses are not printed directly as they are themselves instances of their classes.
        They are printed using classes methods.

        """
        clear_screen()
        print()
        print_one_line_in_frame(f"{self.name.upper()} INFORMATION")
        for key, value in self.__dict__.items():
            if (
                key[1:]
                != "inventory"  # don't print this because you will get Inventory Class information
                and key[1:]
                != "spellbook"  # don't print this because you will get SpellBook Class information
                and key[1:]
                != "statuses"  # don't print this because you will get list of classes
            ):
                slow_print(f"    {key[1:].title().replace('_', ' '):10} : {value}\n")
        print(f"    Statuses   : {', '.join(status.name for status in self.statuses)}")
        self.inventory.show()
        self.spellbook.show()

    def heal(self, additional_health):
        self.health += additional_health

    def take_damage(self, damage):
        if damage > 0:
            self.health -= damage
        if self.health < 0:
            self.health = 0
            self.statuses = ["dead"]
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
        """
        When player defends, his defense is multiplied by 50%.
        """
        self.defense = int(self.defense * 1.5)
        print(f"\n{self.name} is defending!\n")
        print(f"{self.name}'s armor is now {self.defense}!\n")

    def use_magic(self, defender):
        """Use magic method for both players."""
        self.spellbook.show()
        choice = input("Which spell would you like to use?\n > ")
        self._use_magic_choice_handler(choice, defender)

    def _use_magic_choice_handler(self, choice, defender):
        if choice == "":
            return
        else:
            spell = self.spellbook.spells[int(choice) - 1]
        if self.mana < spell.mana_cost:
            print_red(f"You don't have enough mana to cast {spell.name}!\n")
            time.sleep(1)
            self.use_magic(defender)
        else:
            spell.cast(self, defender)
            print(f"You used your magic skills casting {spell.name} spell.")

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
                    print_red(f"{selected_item.name} is broken and can't be used!")
                    return
                else:
                    self.equip_weapon(selected_item)
            elif isinstance(selected_item, Armor):
                for armor in self.inventory.items:
                    if isinstance(armor, Armor) and armor.is_equipped:
                        self.unequip_armor(armor)
                if selected_item.durability <= 0:
                    print_red(f"{selected_item.name} is broken and can't be used!")
                    return
                else:
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

    def flee(self):
        dice = Dice()
        flee_chance = dice.roll("1d10")
        print(f"You rolled {flee_chance}")
        time.sleep(0.5)
        if flee_chance <= 2:
            health_lost = int(self.max_health / 20)
            print_red(
                f"\n{self.name} failed to escape and hurt himself for {health_lost}!\n"
            )
            self.health -= health_lost
            time.sleep(1)
            return
        elif 2 < flee_chance <= 9:
            print(f"\n{self.name} failed to escape from the battlefield!\n")
            time.sleep(1)
            return
        elif 9 < flee_chance <= 10:
            print_green(f"\n{self.name} escaped from the battlefield!\n")
            time.sleep(1)
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

    def equip_weapon(self, weapon):
        """Equips a weapon to the hero."""
        self.equipped_weapon = weapon
        weapon.is_equipped = True
        self.strength += weapon.damage

    def unequip_weapon(self, weapon):
        """Unequips a weapon from the hero."""
        self.equipped_weapon = None
        weapon.is_equipped = False
        self.strength -= weapon.damage

    def equip_armor(self, armor):
        """Equips an armor to the Creature."""
        self.equipped_armor = armor
        armor.is_equipped = True
        self.defense += armor.protection

    def unequip_armor(self, armor):
        """Unequips an armor from the Creature."""
        self.equipped_armor = None
        armor.is_equipped = False
        self.defense -= armor.protection


@dataclass
class Hero(Creature):
    max_mana: int = 20
    mana: int = 10

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
        self.health = self.max_health
        while points_to_spend > 0:
            self._level_up_menu()
            print(f"\nYou have {points_to_spend} points to spend.")
            choice = int(input("\nWhich statistic do you want to increase?  -> "))
            self._level_up_choice_handler(choice)
            if choice != 0:
                points_to_spend -= 1

    def _level_up_menu(self):
        clear_screen()
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
        print_one_line_in_frame("Enemy revealed!")
        time.sleep(1)
        self.show_info()
        input()


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
