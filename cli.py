def shop_menu(shop):
    print("Item you can buy in this place:")
    for i, item in enumerate(shop.stock.items, start=1):
        print(f"{i}. {item.name:20} for price {item.value}")

