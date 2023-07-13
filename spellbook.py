from dataclasses import dataclass, field


@dataclass
class Spell:
    name: str = ""
    description: str = ""
    base_damage: int = 5
    damage_type: str = ""
    category: str = ""
    mana_cost: int = 5
    value: int = 10


@dataclass
class SpellBook:
    spells: list[Spell] = field(default_factory=list)

    def add_spell(self, spell: Spell):
        self.spells.append(spell)

    def remove_spell(self, spell: Spell):
        self.spells.remove(spell)

    def get_spell(self, name: str):
        for spell in self.spells:
            if spell.name == name:
                return spell
        return None


fireball = Spell(
    name="Fireball",
    description="A small ball of fire",
    base_damage=10,
    damage_type="Fire",
    category="Elemental Magic",
    mana_cost=5,
    value=10,
)
