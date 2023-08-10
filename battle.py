from classes import *
from data.characters import *
from infos import *
from decorators import *


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0

        self.player_healthbar = HealthBar(player)
        self.enemy_healthbar = HealthBar(enemy)

    def start_battle(self):
        while self.player.is_alive and self.enemy.is_alive:
            self.next_turn()
        return

    def next_turn(self):
        self.turn += 1
        print(f"Turn {self.turn}")
        if self.turn % 2 != 0:
            self.player_turn()
        else:
            self.enemy_turn()

    def print_info(self):
        print(f"\n{self.player.name} vs {self.enemy.name}\n")
        print_battle_stats(player, enemy)
        self.player_healthbar.draw_health_bar()
        self.enemy_healthbar.draw_health_bar()
        self.print_options()

    def player_turn(self):
        self.print_info()
        choice = self.get_player_choice()
        self.handle_player_choice(choice)

    def print_options(self):
        print_turn_options()

    def get_player_choice(self):
        """Get player choice and return it."""
        choice = input("Enter your choice -> ")
        return choice

    def handle_player_choice(self, choice):
        """Handle player choice."""
        if choice == "1":
            player.attack(self.enemy)
        elif choice == "2":
            player.defend()
        elif choice == "3":
            player.use_magic(self.enemy)
        elif choice == "4":
            player.use_item()
        elif choice == "5":
            player.flee()
        elif choice == "6":
            self.end()
        else:
            print("Invalid choice!")
            time.sleep(1)
            self.player_turn()

    def enemy_turn(self):
        print(f"\n{self.enemy.name} vs {self.player.name}\n")
        enemy.attack(self.player)

    def win(self, attacker):
        print_one_line_in_frame(f"{attacker.name} wins the battle!")
        attacker.experience += self.enemy.experience
        attacker.health = attacker.max_health

    def end(self):
        exit()
