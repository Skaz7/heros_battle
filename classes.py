import random


class Hero:
    def __init__(
        self,
        name: str = "Hero",
        level: int = 1,
        experience: int = 0,
        race: str = None,
        max_health: int = 100,
        health: int = 100,
        strength: int = 10,
        dexterity: int = 10,
        armor: int = 10,
        mana: int = 10,
        gold: int = 10,
        status: str = None,
        inventory=None,
    ):
        self.name = name
        self.level = level
        self.experience = experience
        self.race = race
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
        self.armor = armor
        self.mana = mana
        self.gold = gold
        self.status = status
        self.inventory = inventory

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
    def mana(self):
        return self._mana

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

    @mana.setter
    def mana(self, new_mana):
        self._mana = new_mana

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

    def attack(self, target):
        damage = self.strength
        print(f"\n{self.name} attacks {target.name} for {damage} damage!\n")
        target.health -= damage


class Enemy:
    def __init__(
        self,
        race: str = "Hero",
        level: int = 1,
        attack: int = 10,
        health: int = 100,
        armor: int = 10,
        xp: int = 0,
        gold: int = 10,
        weakness: str = None,
        resistance: str = None,
        status: str = None,
    ):
        self.race = race
        self.level = level
        self.attack = attack
        self.health = health
        self.armor = armor
        self.xp = xp
        self.gold = gold
        self.weakness = weakness
        self.resistance = resistance
        self.status = status

    @property
    def level(self):
        return self._level

    @property
    def race(self):
        return self._race

    @property
    def attack(self):
        return self._attack

    @property
    def health(self):
        return self._health

    @property
    def armor(self):
        return self._armor

    @property
    def xp(self):
        return self._xp

    @property
    def gold(self):
        return self._gold

    @property
    def weakness(self):
        return self._weakness

    @property
    def resistance(self):
        return self._resistance

    @property
    def status(self):
        return self._status

    @race.setter
    def race(self, new_race):
        self._race = new_race

    @level.setter
    def level(self, new_level):
        self._level = new_level

    @attack.setter
    def attack(self, new_attack):
        self._attack = new_attack

    @health.setter
    def health(self, new_health):
        self._health = new_health

    @armor.setter
    def armor(self, new_armor):
        self._armor = new_armor

    @xp.setter
    def xp(self, new_xp):
        self._xp = new_xp

    @gold.setter
    def gold(self, new_gold):
        self._gold = new_gold

    @weakness.setter
    def weakness(self, new_weakness):
        self._weakness = new_weakness

    @resistance.setter
    def resistance(self, new_resistance):
        self._resistance = new_resistance

    @status.setter
    def status(self, new_status):
        self._status = new_status


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_turn(self):
        print(f"\n{self.player.name} vs {self.enemy.race}\n")
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
            self.battle_menu()

    def enemy_turn(self):
        pass

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
        defender.health -= damage
        print(f"\n{attacker.name} attacks {defender.race} for {damage} damage!\n")
        if defender.health <= 0:
            self.win()

    def defend(self, defender):
        defender.armor *= 1.5
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
        return


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


class Item:
    def __init__(self, name: str, description: str, value: int):
        """Initializes a new instance of item.
        Item type can be weapon, armor or consumable.
        """
        self.name = name
        self.description = description
        self.value = value

    def destroy(self):
        print(f"\n{self.name} is destroyed!\n")
        Hero.inventory.remove(self)


class Weapon(Item):
    def __init__(
        self, name: str, description: str, damage_type: str, value: int, damage: int
    ):
        """Initializes a new instance of Weapon item.
        In addition to Item attributes, there is 'damage' attribute.
        """
        super().__init__(name, description, value)
        self.damage_type = damage_type
        self.damage = damage


class Armor(Item):
    def __init__(
        self,
        name: str,
        description: str,
        additional_resistance: str,
        value: int,
        armor: int,
    ):
        """Initializes a new instance of Armor item.
        In addition to Item attributes,, there is 'armor' attribute.
        """
        super().__init__(name, description, value)
        self.additional_resistance = additional_resistance
        self.armor = armor


class Consumable:
    def __init__(
        self,
        name: str,
        description: str,
        value: int,
        heal: int,
        mana: int,
        strength: int,
        dexterity: int,
    ):
        """Initializes a Consumable Item.
        Consuming one of this items will upgrade player statistics.
        Upgrade can be temporary or permanent, depending of the item."""
        super().__init__(name, description, value)
        self.heal = heal
        self.mana = mana
        self.strength = strength
        self.dexterity = dexterity


class Spell:
    pass


class Status:
    def __init__(self, name: str, description: str, duration: int):
        self.name = name
        self.description = description
        self.duration = duration
