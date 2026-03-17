def main():
    print("=== Import Transmutation Mastery ===\n")
    from alchemy.elements import create_fire
    print(f"Method 1 - Full module import: ")
    print(f"alchemy.elements.create_fire(): {create_fire()}")

    import alchemy.elements
    print("\nMethod 2 - Specific function import: ")
    print(f"create_water(): {alchemy.elements.create_water()}")

    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:")
    print("heal(): ", heal())

    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    print("create_earth(): ", create_earth())
    print("create_fire{}:", create_fire())
    print(strength_potion())
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)