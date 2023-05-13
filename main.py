from classes import Hero
import os
import time


def create_player(
    name,
    level,
    experience,
    race,
    max_health,
    health,
    strength,
    dexterity,
    mana,
    gold,
    status,
    inventory,
):
    global player
    player = Hero(
        name,
        level,
        experience,
        race,
        max_health,
        health,
        strength,
        dexterity,
        mana,
        gold,
        status,
        inventory,
    )


def print_player_stats(player):
    print("\nHero Stats:")
    print(f"    Name:       {player.name}")
    print(f"    Level:      {player.level}")
    print(f"    Experience: {player.experience}")
    print(f"    Race:       {player.race}")
    print(f"    Max Health: {player.max_health}")
    print(f"    Health:     {player.health}")
    print(f"    Strength:   {player.strength}")
    print(f"    Dexterity:  {player.dexterity}")
    print(f"    Mana:       {player.mana}")
    print(f"    Gold:       {player.gold}")
    print(f"    Status:     {player.status}")
    print(f"    Inventory:  {player.inventory}")
    print()


if __name__ == "__main__":
    os.system("cls")
    create_player("Jimi Hendrix", 2, 0, "Gnome", 150, 27, 12, 8, 21, 129, "Sick", [])
    print_player_stats(player)
    player.level_up()
    print_player_stats(player)
