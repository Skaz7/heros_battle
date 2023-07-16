from dataclasses import dataclass
from items import Inventory, Weapon, Armor, Consumable
from spellbook import SpellBook
from decorators import print_one_line_in_frame, slow_print
from classes import Dice


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
    armor: int = 10
    status: str = None
    inventory: Inventory = Inventory()
    is_alive: bool = True
    spellbook: SpellBook = SpellBook()

    ######## Getters and setters ########

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

    @spellbook.setter
    def spellbook(self, new_spellbook):
        self._spellbook = new_spellbook

    ######## Methods ########

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
        base_attack = self.strength
        additional_attack = 0
        total_attack = base_attack + additional_attack
        damage = total_attack - defender.armor
        defender.take_damage(damage)
        print(f"\n{self.name} attacks {defender.name} for {damage} damage!\n")

    def defend(self):
        self.armor = int(self.armor * 1.5)
        print(f"\n{self.name} is defending!\n")
        print(f"{self.name}'s armor is now {self.armor}!\n")

    def use_magic(self, defender):
        """Use magic method for both players."""
        print(f"Spells in your spellbook: ")
        for spell in self.spellbook.spells:
            print(f"{spell.name}")
        input("ENTER -> Go Back.\n")

    def flee(self):
        dice = Dice()
        flee_chance = dice.roll(10)
        if flee_chance <= 2:
            print(
                f"\n{self.name} get hurt while running from battle and failed to escape!\n"
            )
            self.health -= int(self.max_health / 20)
            return
        elif 2 < flee_chance <= 5:
            print(f"\n{self.name} failed to escape from the battlefield!\n")
            return
        elif 5 < flee_chance <= 10:
            print(f"\n{self.name} escaped from the battlefield!\n")
            exit()

    def print_basic_stats(self):
        print()
        print_one_line_in_frame(f"{self.name} Stats:")
        slow_print(f"    Health : {self.health}/{self.max_health}\n")
        slow_print(f"    Experience : {self.experience}\n")
        slow_print(f"    Level : {self.level}\n\n")

    def print_full_stats(self):
        print()
        print_one_line_in_frame(f"{self.name} Stats:")
        slow_print(f"   1. Level : {self.level}\n")
        slow_print(f"   2. Experience : {self.experience}\n")
        slow_print(f"   3. Race : {self.race}\n")
        slow_print(f"   3. Health : {self.health}/{self.max_health}\n")
        slow_print(f"   4. Strength : {self.strength}\n")
        slow_print(f"   5. Dexterity : {self.dexterity}\n")
        slow_print(f"   6. Armor : {self.armor}\n")
        slow_print(f"   7. Mana : {self.mana}/{self.max_mana}\n")
        slow_print(f"   8. Status : {self.status}\n")
        slow_print(f"   9. Inventory : {self.inventory}\n")
        slow_print(f"   10. Spellbook : {self.spellbook}\n")


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

    def use_item(self):
        self.inventory.show()
        choice = int(input("> "))
        selected_item = self.player.inventory.items[choice - 1]
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
                self.equip_weapon(selected_item)
            elif isinstance(selected_item, Armor):
                self.equip_armor(selected_item)
            elif isinstance(selected_item, Consumable):
                self.use_consumable(selected_item)
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
        print(f"    3. Armor ({self.armor})")
        print(f"    4. Mana ({self.max_mana})")
        print("\n    0. Go Back.")

    def _level_up_choice_handler(self, choice):
        if choice == 1:
            self.strength += 1
        elif choice == 2:
            self.dexterity += 1
        elif choice == 3:
            self.armor += 1
        elif choice == 4:
            self.max_mana += 1
        elif choice == 0:
            return
        else:
            print("Wrong choice! Please repeat.")
            self.level_up_choice_handler(choice)


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
