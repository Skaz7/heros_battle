from decorators import print_one_line_in_frame


def shop_menu(shop):
    print("Item you can buy in this place:")
    for i, item in enumerate(shop.stock.items, start=1):
        print(f"{i}. {item.name:20} for price {item.value}")


def print_game_menu():
    print()
    print_one_line_in_frame("GAME OPTIONS")
    print("\n1. Show Inventory")
    print("2. Load game")
    print("3. Save game")
    print("4. EXIT GAME\n")
