#!/usr/bin/env python3
import sys


class InventoryError(Exception):
    """"""
    pass


class QuantityError(InventoryError):
    """voy a usar este error para que no se puedan meter más de 5 elementos en el inventario"""
    pass


def get_quantity(item: str, number: str) -> int:
    """
    """
    if number == '1':
        quantity = 1
    elif number == '2':
        quantity = 2
    elif number == '3':
        quantity = 3
    elif number == '4':
        quantity = 4
    elif number == '5':
        quantity = 5
    else:
        raise QuantityError(f"{item} quantity is not valid "
                            f"(must be betwen 1 and 5, entered {number})")
    return quantity


def arg_parsing(inventory_list: list) -> dict[str, int]:
    """
    """
    inv_dic = dict()
    for item in inventory_list:
        i = 0
        while i < len(item) and item[i] != ':':
            i += 1
        key = item[:i]
        qt_str = item[i+1:]
        try:
            quantity = get_quantity(item, qt_str)
        except QuantityError as e:
            print(f"Caught QuantityError: {e}")
        inv_dic.update({key: quantity})
    return inv_dic


def inventory_system() -> None:
    """"""
    inventory = dict()
    inventory = arg_parsing(sys.argv[1:])
    total = 0
    types = 0
    print("=== Inventory System Analysis ===")
    # total items
    for quantity in inventory.values():
        total += quantity
    print(f"Total items in inventory: {total}")
    # total types
    for items in inventory:
        types += 1
    print(f"Unique items types: {types}")
    # current inventory
    print("\n=== Current Inventory ===")
    for item in inventory:
        units = inventory.get(item, quantity)
        print(f"{item}: {units} units ({(units * 100) / total:.1f}%)")
    # inventory statistics
    print("\n=== Inventory Statistics ===")
    max_key = ""
    max_value = 0
    for item in inventory:
        units = inventory.get(item, quantity)
        if units > max_value:
            max_key = item
            max_value = units
    print(f"Most abundant: {max_key} ({max_value} units)")
    min_key = ""
    min_value = 5
    for item in inventory:
        units = inventory.get(item, quantity)
        if units < min_value:
            min_key = item
            min_value = units
    print(f"Least abundant: {min_key} ({min_value} units)")
    # Item categories
    print("\n== Item Category ===")
    moderate = dict()
    scarce = dict()
    for item, quantity in inventory.items():
        if quantity >= 4:
            moderate.update({item: quantity})
        else:
            scarce.update({item: quantity})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    # Management sugestions
    print("\n=== Management Suggestions ===")
    restock_sugest = ""
    for item, quantity in inventory.items():
        if quantity == 1:
            if restock_sugest == "":
                restock_sugest = item
            else:
                restock_sugest = restock_sugest + ", " + item
    print(f"Restock needed: {restock_sugest}")
    # Dictionary properties demo 
    print("\n === Dictionary Properties Demo ===")
    print("Dictionary keys:", end=" ")
    print(*inventory.keys(), sep=", ")
    print("Dictionary values:", end=" ")
    print(*inventory.values(), sep=", ")
    # simple lookup
    find_item = 'sword'
    exist = find_item in inventory
    print(f"Sample lookup - {find_item} in inventory: {exist}")


if __name__ == "__main__":
    inventory_system()
