"""Inventory System Module"""

# Inventory storage (dictionary)
inventory = {}


def add_item(item_name, quantity):
    """Add a new item to the inventory."""
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity


def remove_item(item_name, quantity):
    """Remove a given quantity of an item from the inventory."""
    if item_name in inventory:
        inventory[item_name] -= quantity
        if inventory[item_name] <= 0:
            del inventory[item_name]
    else:
        print(f"Item '{item_name}' not found in inventory.")


def get_quantity(item_name):
    """Return the quantity of the specified item."""
    return inventory.get(item_name, 0)


def load_data(data):
    """Load inventory data from a provided dictionary."""
    inventory.clear()
    inventory.update(data)


def save_data():
    """Return the current inventory data."""
    return inventory.copy()


def print_data():
    """Display all items and their quantities."""
    print("Current Inventory:")
    for item, qty in inventory.items():
        print(f"- {item}: {qty}")


def check_low_items(threshold):
    """Print all items with quantity below a given threshold."""
    low_items = {
        item: qty for item, qty in inventory.items()
        if qty < threshold
    }
    if low_items:
        print("Low stock items:")
        for item, qty in low_items.items():
            print(f"- {item}: {qty}")
    else:
        print("All items have sufficient stock.")


if __name__ == "__main__":
    # Demonstration of the inventory system
    sample_data = {"Apples": 10, "Bananas": 5, "Oranges": 12}
    load_data(sample_data)
    print_data()
    add_item("Apples", 5)
    remove_item("Bananas", 2)
    check_low_items(6)
    print("\nUpdated Inventory:")
    print_data()
