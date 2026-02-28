def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    if unit == "packets":
        x = (f"{seed_type} seeds : {quantity} {unit} available .").capitalize()
        print(x)
    elif unit == "grams":
        x = (f"{seed_type} seeds : {quantity} {unit} total .").capitalize()
        print(x)
    elif unit == "area":
        x = (f"{seed_type} seeds :covers" f" {quantity} square meters.").capitalize()
        print(x)
    else:
        print("Unknown unit type.")
