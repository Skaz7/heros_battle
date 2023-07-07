from decorators import slow_print, print_one_line_in_frame


def print_all_stats(creature):
    print()
    print_one_line_in_frame(f"{creature.name} Stats:")
    for key, value in creature.__dict__.items():
        slow_print(f"    {key[1:].title():10} : {value}\n")
    creature.inventory.show()


def print_battle_stats(creature):
    print()
    print_one_line_in_frame(f"{creature.name} Stats:")
    slow_print(f"    Health : {creature.health}/{creature.max_health}\n")
    slow_print(f"    Experience : {creature.experience}\n")
    slow_print(f"    Level : {creature.level}\n\n")
    