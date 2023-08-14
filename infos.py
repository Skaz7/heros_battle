from decorators import slow_print, print_one_line_in_frame


def print_basic_stats(creature):
    print()
    print_one_line_in_frame(f"{creature.name} Stats:")
    slow_print(f"    Health : {creature.health}/{creature.max_health}\n")
    slow_print(f"    Experience : {creature.experience}\n")
    slow_print(f"    Level : {creature.level}\n\n")


def print_battle_stats(player, enemy):
    print()
    print((player.name).ljust(30) + "<----->" + (enemy.name).rjust(30))
    print("-" * 67)
    print(
        f"Health : {player.health}/{player.max_health}".ljust(30)
        + "       "
        + f"Health : {enemy.health}/{enemy.max_health}".rjust(30)
    )
    print(
        f"Level : {player.level}".ljust(30)
        + "       "
        + f"Level :     {enemy.level}".rjust(30)
    )
    print(
        f"Experience : {player.experience:}".ljust(30)
        + "       "
        + f"Experience :     {enemy.experience}".rjust(30)
    )
    print(f"Mana : {player.mana}/{player.max_mana}".ljust(30))
    print("-" * 67)
    print()


def print_turn_options():
    print("1. Attack")
    print("2. Defend")
    print("3. Use Magic")
    print("4. Use Item")
    print("5. Flee")
