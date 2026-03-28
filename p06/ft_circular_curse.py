def main():
    from alchemy.grimoire.validator import validate_ingredients

    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    first_ingredients = "fire air"
    result = validate_ingredients(first_ingredients)
    print(f"valifate ingredients: ({first_ingredients})", result)
    sec_ingredients = "dragon scales"
    result = validate_ingredients(sec_ingredients)
    print(f"valifate ingredients: ({sec_ingredients})", result)

    from alchemy.grimoire.spellbook import record_spell

    print("\nTesting spell recording with validation:")
    name = "Fireball"
    ingredients = "fire air"
    result = record_spell(name, ingredients)
    print(f"record_spell({name}, {ingredients}):", result)
    name = "Dark Magic"
    ingredients = "shadow"
    result = record_spell(name, ingredients)
    print(f"record_spell({name}, {ingredients}):", result)

    from alchemy.grimoire import record_spell

    print("\nTesting late import technique:")
    name = "Lightning"
    ingredients = "air"
    result = record_spell(name, ingredients)
    print(f"record_spell({name}, {ingredients})", result)

    print(
        "\nCircular dependency curse avoided using late imports!\n"
        "All spells processed safely!"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
