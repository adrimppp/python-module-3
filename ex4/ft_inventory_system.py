def inventory_value(inventory: dict):
    i = 0
    total_value = 0
    keys = list(inventory.keys())
    while i < len(keys):
        item = inventory.get(keys[i])
        total_value += item.get("price") * item.get("quantity")
        i += 1
    return total_value

def get_categories(inventory: dict):
    pass

def give_object(giver_int: dict, receiver_dict: dict, item_name: str, qty: int):
    pass

if __name__ == '__main__':
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    alice_inventory = {
        "sword": {"type": "weapon", "rarity": "rare", "quantity": 1, "price": 500},
        "potion": {"type": "consumable", "rarity": "common", "quantity": 5, "price": 50},
        "shield": {"type": "armor", "rarity": "uncommon", "quantity": 1, "price": 200}
    }
    inventory_value = inventory_value(alice_inventory)
    print(f"\nInventory Value: {inventory_value}")
    print(f"Item count: {len(alice_inventory)}")