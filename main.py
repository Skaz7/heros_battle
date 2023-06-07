from classes import Hero, Enemy
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


def create_enemy(
    race,
    level,
    attack,
    health,
    armor,
    xp,
    gold,
    status,
):
    global enemy
    enemy = Enemy(
        race,
        level,
        attack,
        health,
        armor,
        xp,
        gold,
        status,
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


def print_enemy_stats(enemy):
    print("\nEnemy Stats:")
    print(f"    Race:       {enemy.race}")
    print(f"    Level:      {enemy.level}")
    print(f"    Attack:     {enemy.attack}")
    print(f"    Health:     {enemy.health}")
    print(f"    Armor:      {enemy.armor}")
    print(f"    XP:         {enemy.xp}")
    print(f"    Gold:       {enemy.gold}")
    print(f"    Status:     {enemy.status}")
    print()


if __name__ == "__main__":
    os.system("cls")

    create_player("Jimi Hendrix", 2, 0, "Gnome", 150, 27, 12, 8, 21, 129, "Sick", [])
    create_enemy("Goblin", 1, 10, 20, 0, 10, 10, "Alive")
    print_player_stats(player)
    print_enemy_stats(enemy)
