from classes import *
from data.characters import *
from infos import *
from decorators import *
from game import menu, clear_screen
import time


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
        if player.health == 0:
            self.win(enemy)
        if enemy.health == 0:
            self.win(player)

    def next_turn(self):
        self.turn += 1
        clear_screen()
        if self.turn % 2 != 0:
            self.player_turn()
        else:
            self.enemy_turn()

    def print_info(self):
        print_battle_stats(player, enemy)
        print_one_line_in_frame(f"Turn {self.turn}")
        print()
        self.player_healthbar.draw_health_bar()
        self.enemy_healthbar.draw_health_bar()
        self.print_options()

    def player_turn(self):
        player.handle_statuses()
        self.print_info()
        choice = self.get_player_choice()
        self.handle_player_choice(choice)
        input("[ENTER] - continue")


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
        else:
            print("Invalid choice!")
            time.sleep(1)
            self.player_turn()

    def print_action_info(self):
        pass

    def enemy_turn(self):
        self.print_info()
        enemy.attack(self.player)
        input("[ENTER] - continue")

    def win(self, attacker):
        print_one_line_in_frame(f"{attacker.name} wins the battle!")
        print("\n\nEnter - continue")
        if attacker == self.enemy:
            input()
            menu.show()
        elif attacker == self.player:
            self.player.experience += self.enemy.experience
            self.player.health = self.player.max_health
            if self.player.experience >= 10:
                self.player.level_up()
            input()
