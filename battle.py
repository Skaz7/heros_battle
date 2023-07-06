from classes import *


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0

    def start_battle(self):
        while self.player.is_alive and self.enemy.is_alive:
            self.next_turn()

    def next_turn(self):
        self.turn += 1
        print(f"Turn {self.turn}")
        if self.turn % 2 != 0:
            self.player_turn()
        else:
            self.enemy_turn()

    def player_turn(self):
        print(f"\n{self.player.name} vs {self.enemy.name}\n")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Item")
        print("4. Flee")
        print("0. End Game")
        choice = input("Enter your choice: ")
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
            self.win(attacker)

    def defend(self, defender):
        defender.armor = int(defender.armor * 1.5)
        print(f"\n{defender.name} is defending!\n")

    def use_item(self):
        self.player.inventory.show()
        choice = int(input("> "))
        equipped_weapon = self.player.inventory[choice - 1]

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
        print(f"\n{attacker.name} wins the battle!\n")

    def end(self):
        exit()
