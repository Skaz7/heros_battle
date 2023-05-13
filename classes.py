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
        mana: int = 10,
        gold: int = 10,
        status: str = None,
        inventory: list = [],
    ):
        self.name = name
        self.level = level
        self.experience = experience
        self.race = race
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
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


class Inventory:
    pass


class Item:
    pass


class Weapon:
    pass


class Consumable:
    pass


class Enemy:
    pass


class Spell:
    pass
