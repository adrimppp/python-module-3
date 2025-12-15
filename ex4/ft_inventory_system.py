def inventory_value(player_inventory:int, catalog:int) -> int:
    total_price = 0
    for item, qty in player_inventory.items():
        info = catalog.get(item)
        try:
            total_price = info.get("price") * qty + total_price
        except:
            continue
    return(total_price)

def item_count(player_inventory, catalog):
    total_items = 0
    for item, qty in player_inventory.items():
        if item not in catalog:
            continue
        else:
            total_items = total_items + qty
    return (total_items)

def inventory_info(player_inventory, catalog):
    print(f"=== {player_inventory.get("name")} Inventory ===")
    for item, qty in player_inventory.items():
        info = catalog.get(item)
        if item not in catalog:
            continue
        else:
            price = info.get("price")
            quantity = player_inventory.get(info.get("name"))
            print(f"{info.get("name")} ({info.get("item_type")}, {info.get("quality")}) {quantity}x @ {price} gold each = {quantity * price} gold")

def categories(player_inventory, catalog):
    categories = {}

    for item, qty in player_inventory.items():
        if item not in catalog:
            continue
        info = catalog[item]
        quality = info.get("quality")
        categories[quality] = categories.get(quality, 0) + qty

    return categories


def give_items(player_1, player_2, item, quantity):
    if(player_1.get(item) >= quantity):
        player_1[item] -= quantity
        player_2.update({item : (player_2.get(item, 0) + quantity)})
        print("Transaction succesful!")
    else:
        print(f"Transaction could not be done. Reason {player_1}. Does not have {quantity} {item}")

def get_rarest_tems(inventory_1, inventory_2, catalog):
    rare_scale={"uncommon":0, "common":1, "rare":2}
    max_rare = 0
    rarest_items = set()
    for inventory in (inventory_1, inventory_2):
        for item in inventory:
            if item not in catalog:
                continue

            quality = catalog[item]["quality"]
            rarity_value = rare_scale[quality]

            if rarity_value > max_rare:
                max_rare = rarity_value
                rarest_items = {item}
            elif rarity_value == max_rare:
                rarest_items.add(item)
    print(f"{rarest_items}")



def inventory_analytics(player_1_inventory, player_2_inventory, catalog):
    inventory_1 = {}
    inventory_2 = {}

    inventory_1.update({"value": inventory_value(player_1_inventory, catalog)})
    inventory_2.update({"value": inventory_value(player_2_inventory, catalog)})
    inventory_1.update({"number": item_count(player_1_inventory, catalog)})
    inventory_2.update({"number": item_count(player_2_inventory, catalog)})
    if(inventory_1.get("value") > inventory_2.get("value")):
        print(f"Most valuable player: {player_1_inventory.get("name")} ({inventory_1.get("value")} gold)")
    else:
        print(f"Most valuable player: {player_2_inventory.get("name")} ({inventory_2.get("value")} gold)")

    if(inventory_1.get("number") > inventory_2.get("number")):
        print(f"Most items: {player_1_inventory.get("name")} ({inventory_1.get("number")} items)")
    else:
        print(f"Most items: {player_2_inventory.get("name")} ({inventory_2.get("number")} items)")
    get_rarest_tems(player_1_inventory, player_2_inventory, catalog)

sword_dict = dict(name="sword", item_type="weapon", quality="rare", price=500)
potion_dict = dict(name="potion", item_type="consumable", quality="common", price=50)
shield_dict = dict(name="shield", item_type="armor", quality="uncommon", price=200)
magic_ring_dict = dict(name="magic_ring", item_type="wearable", quality="rare", price=700)

catalog = {
    "sword": sword_dict,
    "potion": potion_dict,
    "shield": shield_dict,
    "magic_ring":magic_ring_dict
}

alice_inventory = {"name": "Alice", "sword": 1, "potion": 5, "shield": 1}
bob_inventory = {"name": "Bob", "magic_ring":1}
total_value = inventory_value(alice_inventory, catalog)
print(f"Inventory value: {total_value} gold")

inventory_info(alice_inventory, catalog)

item_number = item_count(alice_inventory, catalog)
print(f"Item count: {item_number} items")
print(f"Categories: {categories(alice_inventory, catalog)}")

print("=== Transaction: Alice gives Bob 2 potions ===")
give_items(alice_inventory, bob_inventory, "potion", 2)

print("=== Updated Inventories ===")
print(f"Alice potions: {alice_inventory.get("potion", 0)}")
print(f"Bob potions: {bob_inventory.get("potion", 0)}")

print("=== Inventory Analytics ===")
inventory_analytics(alice_inventory, bob_inventory, catalog)
