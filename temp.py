class Hero:
    def __init__(
        self,
        name: str = "Hero",
        level: int = 1,
        race: str = None,
        health: int = 100,
        strength: int = 10,
        dexterity: int = 10,
        mana: int = 10,
        status: str = None,
        inventory: list = [],
    ):
        self.name = name
        self.level = level
        self.race = race
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
        self.mana = mana
        self.status = status
        self.inventory = inventory


class Inventory:
    pass
