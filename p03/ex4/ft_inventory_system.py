import sys

def dict_creator(args):
    inventory = {}
    for item in args:
        inventory_keys,  inventory_value = item.split(':')
        inventory.update({inventory_keys: inventory_value})
    return inventory


def values_calculator(lst):
    counter = 0
    for item in lst:
        try:
            counter += int(item)
        except ValueError:
            print(f"The {item} should be a number")
    print(f"Total items in inventory: {counter}")  
    print(f"Unique item types: {len(lst)}")
    return counter

def current_inventory(inventory, total):
    i = 0
    key = [item for item in inventory.keys()]
    value = [item for item in inventory.values()]
    lst = value
    print(key, value)
    while i < len(inventory):
        v = int(value[i])
        percent = (v / total) * 100
        print(f"{key[i]} : {value[i]} units ({percent:.1f}%)")
        i += 1
    return lst


def statistics(values):
    lst = []
    for item in values:
        try:
            lst.append(int(item))
        except Exception:
            print("kalwa")
    print(lst)

def main():
    print("=== Inventory System Analysis ===\n")
    args = sys.argv
    print(args)
    inventory = dict_creator(args[1:])
    total = values_calculator(inventory.values())

    print("\n=== Current Inventory ===")
    values = current_inventory(inventory, total)
    print("\n=== Inventory Statistics ===")
    statistics(values)

main()
