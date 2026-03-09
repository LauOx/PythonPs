import sys
from typing import Dict


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
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {len(como sumo los objetos?)}")



if __name__ == "__main__":
    inventory_system()
