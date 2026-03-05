import sys


def dict_creator(args):
    inventory = {}
    for item in args:
        try:
            inventory_keys,  value = item.split(':')
            inventory_value = int(value)
            inventory.update({inventory_keys: inventory_value})
        except Exception as e:
            print(e)

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
    while i < len(inventory):
        v = int(value[i])
        percent = (v / total) * 100
        print(f"{key[i]} : {value[i]} units ({percent:.1f}%)")
        i += 1
    return key, value


def statistics(keys, values):
    maxi = max(values)
    mini = min(values)
    i = 0
    j = 0
    if maxi and mini in values:
        while i < len(values):
            if values[i] == maxi:
                unit = "unit" if maxi < 2 else "units"
                print(f"Most abundant: {keys[i]} ({maxi} {unit})")
                break
            i += 1

        while j < len(values):
            if values[j] == mini:
                unit = "unit" if mini < 2 else "units"
                print(f"Least abundant: {keys[j]} ({mini} {unit})")
                break
            j += 1

def Management_Suggestions(keys, values):
    i = 0
    restock = []
    while i < len(values):
        if values[i] < 2:
            restock.append(keys[i])
        i += 1
    if restock:
        print("Restock needed: ", end="")
        for item in restock:
            print(item, end=' ')
    else:
        print("No need for the Restock.")

def Item_Categories(keys, values):
    maxi = max(values)
    i = 0
    if maxi in values:
        while i < len(values):
            if values[i] == maxi:
                print(f"Moderate: {keys[i]} {values[i]}")
                break
            i += 1

        j = 0
        print("Scarce : {", end="")
        while j < len(values):
            if i != j:
                print(f"'{keys[j]}': ", values[j], end=", " if i + 1 != len(keys) else "")
            j += 1
        print("}")

def Properties_Demo(keys, values):
    i = 0
    print("Dictionary keys: ", end="")
    for item in keys:
        print(item, end=", " if i + 1 != len(keys) else "")
        i += 1
    print()
    i = 0
    print("Dictionary keys: ", end="")
    for item in values:
        print(item, end=", " if i + 1 != len(values) else "")
        i += 1
    print()
    print(f"Sample lookup - '{keys[0]}' in inventory: True")
def main():
    args = sys.argv
    if len(args) > 1:
        print("=== Inventory System Analysis ===\n")
        print(args)
        inventory = dict_creator(args[1:])
        total = values_calculator(inventory.values())

        print("\n=== Current Inventory ===")
        keys, values = current_inventory(inventory, total)

        print("\n=== Inventory Statistics ===")
        statistics(keys, values)

        print("\n=== Item Categories ===")
        Item_Categories(keys, values)

        print("\n=== Management Suggestions ===")
        Management_Suggestions(keys, values)
        
        print("\n\n=== Dictionary Properties Demo ===")
        Properties_Demo(keys, values)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)