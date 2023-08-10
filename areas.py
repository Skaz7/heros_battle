from dataclasses import dataclass, field
from data.weapons import *
from cli import *
from creatureclass import Npc
from classes import Chest
from decorators import *
from battle import Battle
from data.characters import player, enemy


@dataclass
class Store:
    name: str = ""
    description: str = ""
    stock: Inventory = Inventory()
    discount: int = 0

    def show_stock(self) -> None:
        shop_menu(self)


@dataclass
class Shop(Store):
    def buy_item(self, player, item_index):
        item = self.stock.items[item_index - 1]
        player.inventory.add_item(item)
        self.stock.remove_item(item)
        print(f"You bought {self.stock}!")


@dataclass
class Temple(Store):
    def heal_player(self, player):
        player.health = player.max_health

    def learn_spell(self, player, spell):
        if spell.required_level <= player.level:
            player.spellbook.add_spell(spell)


@dataclass
class Blacksmith(Store):
    def repair_weapon(self, weapon):
        repair_cost = int(weapon.value * 0.25)
        weapon.durability = weapon.max_durability

    def repair_armor(self, armor):
        repair_cost = int(armor.value * 0.25)
        armor.durability = armor.max_durability

    def buy_item(self, player, item_index):
        item = self.stock.items[item_index - 1]
        player.inventory.add_item(item)
        self.stock.remove_item(item)
        print(f"You bought {item.name}!")


@dataclass
class Area:
    name: str = ""
    description: str = ""
    available_directions: list = field(default_factory=list)
    enemies: list = field(default_factory=list)
    treasures: Chest = Chest()
    npcs: Npc = Npc()
    store: Store = Store()
    visited: bool = False

    def examine(self) -> None:
        print("\nWhat do you want to do?\n")

        activities = self.list_area_activities()

        for key, value in activities.items():
            print(f"{key}. {value}")

        choice = int(input(" > "))
        self.examine_handler(choice, activities)

    def list_area_activities(self) -> dict:
        activities_dict = {
            1: "Show inventory",
            2: "Stop examining area",
        }
        activities_list = []
        if self.enemies is not None:
            activities_list.append("Fight Enemy")
        if self.treasures is not None:
            activities_list.append("Open chest")
        if self.npcs is not None:
            activities_list.append("Talk to NPC")

        activities_dict.update(
            {i: activity for i, activity in enumerate(activities_list, start=3)}
        )
        return activities_dict

    def examine_handler(self, choice, activities_dict) -> None:
        if choice not in activities_dict.keys():
            print_red("Invalid choice!")
            time.sleep(0.5)
            self.examine()
        else:
            result = activities_dict[choice]
            if result == "Show inventory":
                player.inventory.show()
                input()
                self.examine()
            elif result == "Stop examining area":
                return
            elif result == "Fight Enemy":
                battle = Battle(player, enemy)
                battle.start_battle()
            elif result == "Open chest":
                player.open_chest(self.treasures)
            elif result == "Talk to NPC":
                npc = self.npcs.talk()
                print()
