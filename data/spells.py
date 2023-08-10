from spellbook import Spell


fireball = Spell(
    name="Fireball",
    description="A small ball of fire",
    required_level=1,
    base_damage=10,
    damage_type="Fire",
    category="Elemental Magic",
    mana_cost=5,
    value=10,
)

freeze = Spell(
    name="Freeze",
    description="Freezes the enemy",
    required_level=1,
    base_damage=10,
    damage_type="Cold",
    category="Elemental Magic",
    mana_cost=5,
    value=10,
)

reveal = Spell(
    name="Reveal",
    description="Reveals the enemy",
    required_level=1,
    base_damage=0,
    damage_type="Reveal",
    category="Elemental Magic",
    mana_cost=7,
    value=15,
)
