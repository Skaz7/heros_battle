from dataclasses import dataclass, field
from data.weapons import *
from creatureclass import Hero, Npc
from spellbook import Spell
from classes import Chest
from game import clear_screen
from decorators import *
from battle import Battle
from data.characters import player, enemy


@dataclass
class Store:
    name: str = ""
    description: str = ""
    stock: list = field(default_factory=list)
    discount: int = 0

    def show_stock(self) -> None:
        print("Item you can buy in this place:")
        for i, item in enumerate(self.stock, start=1):
            print(f"{i}. {item.name:20} for price {item.value}")


class Shop(Store):
    def buy_item(self, player, item_index):
        item = self.stock[item_index - 1]
        player.inventory.add_item(item)
        self.stock.remove(item)
        print(f"You bought {item.name}!")


@dataclass
class Temple(Store):
    def heal_player(self, player: Hero):
        player.health = player.max_health

    def learn_spell(self, player, spell: Spell):
        if spell.required_level <= player.level:
            player.spellbook.add_spell(spell)
        else:
            print_red("You don't have required level to learn this spell.")


@dataclass
class Blacksmith(Store):
    owner: str = "John"
    price_multipier = 0.5

    def info(self):
        print_one_line_in_frame(f"{self.owner} the Blacksmith")
        print("You can repair your stuff here.")

@dataclass
class Area:
    name: str = ""
    description: str = ""
    available_directions: list = field(default_factory=list)
    enemies: list = field(default_factory=list)
    treasure: Chest = Chest()
    npc: Npc = Npc()
    store: Store = Store()
    visited: bool = False

    def examine(self) -> None:
        clear_screen()
        print("\nWhat do you want to do?\n")

        activities = list_area_activities(self)

        for key, value in activities.items():
            print(f"{key}. {value}")

        choice = int(input(" > "))
        self.handle_examine_choice(choice, activities)

    def handle_examine_choice(self, choice, activities_dict) -> None:
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
                player.open_chest(self.treasure)
            elif result == f"Talk to {self.npc.name}":
                npc = self.npc.talk_to()
                print()


def list_area_activities(area=Area()) -> dict[int, str]:
    activities_dict = {
        1: "Show inventory",
        2: "Stop examining area",
    }
    activities_list = []
    if area.enemies is not None:
        activities_list.append("Fight Enemy")
    if area.treasure is not None:
        activities_list.append("Open chest")
    if area.npc is not None:
        activities_list.append(f"Talk to {area.npc.name}")
    activities_dict.update(
        {i: activity for i, activity in enumerate(activities_list, start=3)}
    )
    return activities_dict
