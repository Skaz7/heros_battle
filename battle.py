from classes import *
from infos import *
from decorators import *


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0

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

    def player_turn(self):
        print(f"\n{self.player.name} vs {self.enemy.name}\n")
        self.player.print_battle_stats()
        print("1. Attack")
        print("2. Defend")
        print("3. Use Item")
        print("4. Flee")
        print("5. End Game")

        choice = self.get_player_choice()
        self.handle_player_choice(choice)

    def get_player_choice(self):
        """Get player choice and return it."""
        choice = input("Enter your choice -> ")
        return choice

    def handle_player_choice(self, choice):
        """Handle player choice."""
        if choice == "1":
            self.attack(self.player, self.enemy)
        elif choice == "2":
            self.defend(self.player)
        elif choice == "3":
            self.use_item()
        elif choice == "4":
            self.flee()
        elif choice == "0":
            self.end()
        else:
            print("Invalid choice!")
            time.sleep(2)
            self.player_turn()

    def enemy_turn(self):
        print(f"\n{self.enemy.name} vs {self.player.name}\n")
        self.attack(self.enemy, self.player)

    def attack(self, attacker, defender):
        """Attack method for both players.
        Damage dealt to defender is based on the attacker's strength and additional damage provided by equipped weapon.
        If the defender is defending, the damage dealt is reduced by the defender's armor.
        If the defender's health is reduced to 0 or below, the attacker wins.
        """
        base_attack = attacker.strength
        additional_attack = 0
        total_attack = base_attack + additional_attack
        damage = total_attack - defender.armor
        if damage < 0:
            damage = 0
        defender.health -= damage
        print(f"\n{attacker.name} attacks {defender.name} for {damage} damage!\n")
        if defender.health <= 0:
            defender.health = 0
            defender.status = "dead"
            defender.is_alive = False
            self.win(attacker)

    def defend(self, defender):
        defender.armor = int(defender.armor * 1.5)
        print(f"\n{defender.name} is defending!\n")

    def use_item(self):
        self.player.inventory.show()
        choice = int(input("> "))
        selected_item = self.player.inventory.items[choice - 1]
        selected_item.info()
        print(f"1 - Use {selected_item.name}?")
        print("0 - Go Back.\n")
        choice = int(input("> "))
        if choice == 1:
            if isinstance(selected_item, Weapon):
                for weapon in self.player.inventory.items:
                    if isinstance(weapon, Weapon) and weapon.is_equipped:
                        self.player.unequip_weapon(weapon)
                self.player.equip_weapon(selected_item)
            elif isinstance(selected_item, Armor):
                self.player.equip_armor(selected_item)
            elif isinstance(selected_item, Consumable):
                self.player.use_consumable(selected_item)
        elif choice == 0:
            return
        else:
            print("Wrong choice! Please repeat.")
            self.use_item()

    def flee(self):
        dice = Dice()
        flee_chance = dice.roll(10)
        if flee_chance <= 2:
            print(
                f"\n{self.player.name} get hurt while running from battle and failed to escape!\n"
            )
            self.player.health -= int(self.player.max_health / 20)
            return
        elif 2 < flee_chance <= 5:
            print(f"\n{self.player.name} failed to escape from the battlefield!\n")
            return
        elif 5 < flee_chance <= 10:
            print(f"\n{self.player.name} escaped from the battlefield!\n")
            exit()

    def win(self, attacker):
        print_one_line_in_frame(f"{attacker.name} wins the battle!")
        attacker.experience += self.enemy.experience
        attacker.health = attacker.max_health

    def end(self):
        exit()
