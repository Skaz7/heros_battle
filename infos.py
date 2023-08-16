from decorators import slow_print, print_one_line_in_frame
from inventory import Weapon


def print_basic_stats(creature):
    print()
    print_one_line_in_frame(f"{creature.name} Stats:")
    slow_print(f"    Health : {creature.health}/{creature.max_health}\n")
    slow_print(f"    Experience : {creature.experience}\n")
    slow_print(f"    Level : {creature.level}\n\n")


def print_battle_stats(player, enemy):
    print()
    print((player.name).ljust(30) + "<---->" + (enemy.name).rjust(30))
    print("-" * 67)
    print(
        f"{player.health}/{player.max_health}".ljust(25)
        + "<-   HEALTH   ->"
        + f"{enemy.health}/{enemy.max_health}".rjust(25)
    )
    print(
        f"{player.level}".ljust(25)
        + "<-   LEVEL    ->"
        + f"{enemy.level}".rjust(25)
    )
    print(
        f"{player.experience:}".ljust(25)
        + "<- EXPERIENCE ->"
        + f"{enemy.experience}".rjust(25)
    )
    print(f"{player.mana}/{player.max_mana}".ljust(25) + "<-    MANA    ->")
    print(
            f"{', '.join(status.name for status in player.statuses)}".ljust(25)
        + "<-   STATUS   ->"
        + f"{', '.join(status.name for status in enemy.statuses)}".rjust(25)
    )

    if player.equipped_weapon is None:
        player_weapon = None
    else:
        player_weapon = player.equipped_weapon.name
    if enemy.equipped_weapon is None:
        enemy_weapon = None
    else:
        enemy_weapon = enemy.equipped_weapon.name
    print(
        f"{player_weapon}".ljust(25)
        + "<-   WEAPON   ->"
        + f"{enemy_weapon}".rjust(25)
    )

    if player.equipped_shield is None:
        player_shield = None
    else:
        player_shield = player.equipped_shield.name
    if enemy.equipped_shield is None:
        enemy_shield = None
    else:
        enemy_shield = enemy.equipped_shield.name
    print(
        f"{player_shield}".ljust(25)
        + "<-   SHIELD   ->"
        + f"{enemy_shield}".rjust(25)
    )

    if player.equipped_armor is None:
        player_armor = None
    else:
        player_armor = player.equipped_armor.name
    if enemy.equipped_armor is None:
        enemy_armor = None
    else:
        enemy_armor = enemy.equipped_armor.name
    print(
        f"{player_armor}".ljust(25)
        + "<-   ARMOR    ->"
        + f"{enemy_armor}".rjust(25)
    )

    print("-" * 67)
    print()


def print_turn_options():
    print("1. Attack")
    print("2. Defend")
    print("3. Use Magic")
    print("4. Use Item")
    print("5. Flee")
