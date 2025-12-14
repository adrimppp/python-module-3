def inventory_value(player_inventory, catalog) -> None:
    total_price = 0
    for item, qty in player_inventory.items():
        info = catalog.get(item)
        try:
            total_price = info.get("price") * qty + total_price
        except:
            continue
    print(f"Inventory value: {total_price} gold")

#def inventory_info(player_inventory, catalog):
#    print(f"=== {player_inventory.get("name")} Inventory ===")
#    for item, qty in player_inventory.items():
#        info = catalog.get(item)
#        print(f"{info.get("name")} ({info.get("item_type")}, {info.get("quality")})")

sword_dict = dict(name = "sword", item_type = "weapon", quality = "rare", price = 500)

potion_dict = dict(name = "potion", item_type = "consumable", quality = "common", price = 50)
shield_dict = dict(name = "shield", item_type = "armor", quality = "uncommon", price = 200)

catalog = {
    "sword": sword_dict,
    "potion": potion_dict,
    "shield": shield_dict
}
alice_inventory = {"name" : "Alice", "sword": 1, "potion": 5, "shield": 1}
inventory_value(alice_inventory, catalog)