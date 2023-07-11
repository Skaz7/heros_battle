import random
from dataclasses import dataclass


@dataclass
class Dice:
    """Simulates a dice roll of n-sides."""

    def roll(self, sides):
        return random.randint(1, sides)


class HealthBar:
    def __init__(self, creature):
        self.creature = creature

    def draw_health_bar(self):
        max_health = self.creature.max_health
        current_health = self.creature.health

        health_bar_color = self.get_health_bar_color(current_health, max_health)
        health_size = int((current_health / max_health) * 100)

        print(f"Health: {health_bar_color}{current_health}/{max_health}  ", end="")
        print(f"[{health_size * '█'}{(100 - health_size) * '-'}] \033[0m")

    @staticmethod
    def get_health_bar_color(current_health, max_health):
        if current_health >= max_health * 0.7:
            return "\033[0;32m"
        elif max_health * 0.7 > current_health >= max_health * 0.3:
            return "\033[0;33m"
        elif current_health < max_health * 0.3:
            return "\033[0;31m"


@dataclass
class Quest:
    name: str = ""
    description: str = ""
    giver: str = ""
    reward: tuple = ()
    completed: bool = False

    def complete_quest(self):
        self.completed = True


class Spell:
    pass


class Status:
    def __init__(self, name: str, description: str, duration: int):
        self.name = name
        self.description = description
        self.duration = duration
