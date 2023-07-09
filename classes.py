import random
from dataclasses import dataclass


@dataclass
class Dice:
    """Simulates a dice roll of n-sides."""

    def roll(self, sides):
        return random.randint(1, sides)


class HealthBar:
    def __init__(self, creature):
        self.player = creature
        self.max_health = creature.max_health
        self.current_health = creature.health

    def draw_health_bar(self):
        self.max_health = self.player.max_health
        self.current_health = self.player.health

        if self.current_health >= self.max_health * 0.7:
            health_bar_color = "\033[0;32m"
        elif 0.7 * self.max_health > self.current_health >= self.max_health * 0.3:
            health_bar_color = "\033[0;33m"
        elif self.current_health < self.max_health * 0.3:
            health_bar_color = "\033[0;31m"

        health_size = int((self.current_health / self.max_health) * 100)

        print(
            f"Health: {health_bar_color}{self.current_health}/{self.max_health}  ",
            end="",
        )
        print(f"[{health_size * '█'}{(100- health_size) * '-'}] \033[0m")


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
