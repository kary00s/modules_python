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
        except Exception:
            print(f"The {item} should be a number")
    print(f"Total items in inventory: {counter}")  
    print(f"Unique item types: {len(lst)}")
    return counter

def current_inventory(inventory, total):
    for key, value in inventory.items():
        
    key =  [item for item in inventory.keys()]
    print(key)
    value = inventory.values()
    lentgh = len(inventory)
    i = 0
    
    while i < lentgh:
        v = int(value)
        percent = (v / total) * 100
        print(f"{key[i]} : {value[i]} units ({percent:.2f})")
def main():
    print("=== Inventory System Analysis ===\n")
    args = sys.argv
    print(args)
    inventory = dict_creator(args[1:])
    total = values_calculator(inventory.values())

    print("\n=== Current Inventory ===")
    current_inventory(inventory, total)

main()
