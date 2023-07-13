import random
import re
from dataclasses import dataclass, field


class Dice:
    """Simulates a dice roll of n-sides.
    D&D system has dices as below:
    d4: 4-sided dice
    d6: 6-sided dice
    d8: 8-sided dice
    d10: 10-sided dice
    d12: 12-sided dice
    d20: 20-sided dice
    d100: 100-sided dice
    """

    def __init__(self, roll_string: str = "1d6"):
        self.roll_string = roll_string
        self.sides = [4, 6, 8, 10, 12, 20, 100]

    def roll(self, roll_string):
        pattern = r"(\d+)d(\d+)([+-]\d+)?"  # Regex for pattern: XkY(+/-)Z
        match = re.match(pattern, roll_string)  # Check if string matches pattern

        if not match:
            raise ValueError(
                "Wrong roll string format. Use XdY(+/-)Z e.g. 2d6 or 1d20+3"
            )
        if not int(match.group(2)) in self.sides:
            raise ValueError(
                "Wrong dice sides number. Use d4, d6, d8, d10, d12, d20 or d100"
            )

        # Parsing X, Y i Z
        num_dice = int(match.group(1))
        num_sides = int(match.group(2))
        modifier = int(match.group(3) or 0)

        # Simulating dice rolls
        dice_rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total_sum = sum(dice_rolls)

        # Return result with modifier
        return total_sum + modifier


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


class Status:
    def __init__(self, name: str, description: str, duration: int):
        self.name = name
        self.description = description
        self.duration = duration
