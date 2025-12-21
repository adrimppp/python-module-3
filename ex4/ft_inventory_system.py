def inventory_value(inventory: dict):
    i = 0
    total_value = 0
    keys = list(inventory.keys())
    while i < len(keys):
        item = inventory.get(keys[i])
        total_value += item.get("price") * item.get("quantity")
        i += 1
    return total_value

def get_item_qty(inventory: dict):
    i = 0
    item_count = 0
    keys = list(inventory.keys())
    while i < len(keys):
        item = inventory.get(keys[i])
        item_count += item.get("quantity")
        i += 1
    return item_count

def print_categories(inventory: dict):
    weapons = 0
    consumables = 0
    armors = 0
    i = 0
    keys = list(inventory.keys())
    while i < len(keys):
        item = inventory.get(keys[i])
        if item.get("type") == "weapon":
            weapons += item.get("quantity")
        elif item.get("type") == "consumable":
            consumables += item.get("quantity")
        elif item.get("type") == "armor":
            armors += item.get("quantity")
        i += 1

    print(f"Categories: weapon({weapons}), consumable({consumables}), armor({armors}))")

def print_items(inventory: dict):
    i = 0
    keys = list(inventory.keys())
    while i < len(keys):
        item = inventory.get(keys[i])
        print(f"{keys[i]} ({item.get('type')}, {item.get('rarity')}) {item.get('quantity')}x @ {item.get('price')} gold each = {item.get('quantity')*item.get('price')}")
        i += 1

def inventory_info(inventory: dict):
    total_value = inventory_value(alice_inventory)
    print_items(alice_inventory)
    print(f"\nInventory Value: {total_value}")
    print(f"Item count: {get_item_qty(inventory)} items")
    print_categories(alice_inventory)

def give_object(giver_dict: dict, receiver_dict: dict, item_name: str, qty: int):
    print(f"=== Transaction: Alice gives Bob {qty} {item_name} ===")

    if item_name not in giver_dict:
        print("Item not found in giver inventory")
        return

    if giver_dict[item_name]["quantity"] < qty:
        print("Not enough quantity")
        return

    giver_dict[item_name]["quantity"] -= qty

    receiver_dict[item_name]["quantity"] += qty
    print("Transaction successful!")
    print("=== Updated Inventories ===")
    print(f"Alice potions: {giver_dict[item_name]['quantity']}")
    print(f"Bob potions: {receiver_dict[item_name]['quantity']}")


def compare_analytics(inventory_1: dict, inventory_2: dict):
    inventory_1_value = inventory_value(inventory_1)
    inventory_2_value = inventory_value(inventory_2)
    item_qty_1 = get_item_qty(inventory_1)
    item_qty_2 = get_item_qty(inventory_2)
    if inventory_1_value > inventory_2_value:
        print(f"Most valuable player: Alice ({inventory_1_value} gold)")
    elif inventory_1_value < inventory_2_value:
        print(f"Most valuable player: Bob ({inventory_2_value} gold)")
    else:
        print(f"Same value inventory: {inventory_1_value} gold")
    if item_qty_1 > item_qty_2:
        print(f"Most items: Alice ({item_qty_1} items)")
    elif item_qty_1 < item_qty_2:
        print(f"Most items:: Bob ({item_qty_2} items)")
    else:
        print(f"Same items: {item_qty_2} items")
    print_rarest_items(inventory_1, inventory_2)


def print_rarest_items(inventory_1: dict, inventory_2: dict):
    rarest = []
    keys_1 = list(inventory_1.keys())
    i = 0
    while i < len(keys_1):
        item = keys_1[i]
        data = inventory_1.get(item)

        if data.get("rarity") == "rare":
            rarest.append(item)

        i += 1

    keys_2 = list(inventory_2.keys())
    j = 0
    while j < len(keys_2):
        item = keys_2[j]
        data = inventory_2.get(item)

        if data.get("rarity") == "rare":
            rarest.append(item)

        j += 1

    print(f"Rarest items: {', '.join(rarest)}")



if __name__ == '__main__':
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    alice_inventory = {
        "sword": dict({"type": "weapon", "rarity": "rare", "quantity": 1, "price": 500}),
        "potion": dict({"type": "consumable", "rarity": "common", "quantity": 5, "price": 50}),
        "shield": dict({"type": "armor", "rarity": "uncommon", "quantity": 1, "price": 200})
    }
    bob_inventory = {
        "magic_ring": dict({"type": "weapon", "rarity": "rare", "quantity": 1, "price": 500}),
        "potion": dict({"type": "consumable", "rarity": "common", "quantity": 0, "price": 50})
    }
    inventory_info(alice_inventory)
    give_object(alice_inventory, bob_inventory, "potion", 2)
    compare_analytics(alice_inventory, bob_inventory)
