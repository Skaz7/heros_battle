from dataclasses import dataclass, field
from decorators import print_green, print_red, print_yellow


@dataclass
class Spell:
    name: str = ""
    description: str = ""
    required_level: int = 1
    base_damage: int = 5
    damage_type: str = ""
    category: str = ""
    mana_cost: int = 5
    value: int = 10

    def info(self):
        for key, value in self.__dict__.items():
            print(f"{key.title().replace('_', ' ')}: {value}")

    def cast(self, attacker, defender):
        attacker.mana -= self.mana_cost
        if self.damage_type == defender.resistance:
            print_red(
                f"You discovered your opponent's resistance to {self.damage_type}!"
            )
            defender.take_damage(self.base_damage * 0.5)
            print(
                f"\n{attacker.name} attacks {defender.name} for {self.base_damage * 0.5} damage!\n"
            )
        elif self.damage_type == defender.weakness:
            print_green(
                f"You discovered your opponent's weakness to {self.damage_type}!"
            )
            defender.take_damage(self.base_damage * 2)
            print(
                f"\n{attacker.name} attacks {defender.name} for {self.base_damage * 2} damage!\n"
            )
        elif self.damage_type == "Reveal":
            defender.reveal_all()
        else:
            defender.take_damage(self.base_damage)
            print(
                f"\n{attacker.name} attacks {defender.name} for {self.base_damage} damage!\n"
            )


@dataclass
class SpellBook:
    spells: list[Spell] = field(default_factory=list)

    def add_spell(self, spell: Spell):
        self.spells.append(spell)

    def remove_spell(self, spell: Spell):
        self.spells.remove(spell)

    def show(self):
        for i, spell in enumerate(self.spells, start=1):
            print(f"[{i}] {spell.name} - {spell.description}")
        print("[0] - BACK\n")
