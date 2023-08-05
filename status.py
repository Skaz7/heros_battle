from dataclasses import dataclass
from creatureclass import Creature
from abc import ABC, abstractmethod


class StatusProcessor(ABC):
    def buff_status(self):
        pass

    def debuff_status(self):
        pass
    



dataclass
class Status:
    name: str = ""
    description: str = ""
    duration: int = 1

    def apply_status(self, creature, status):
        if status == "bleed":
            creature.health = creature.health * 0.9

    def end_status(self, status):
        pass


@dataclass
class Buff:
    name: str = ""
    description: str = ""
    duration: int = 1
    attribute_to_buff: str = ""
    modification_value: int = 10

    def buff(self, creature: Creature):
        pass

    def reset(self):
        pass


@dataclass
class Debuff:
    name: str = ""
    description: str = ""
    duration: int = 1

    def debuff(self):
        pass

    def reset(self):
        pass

