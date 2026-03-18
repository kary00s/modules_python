from alchemy.grimoire.validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)

    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    elif "INVALID" in result:
        return f"Spell rejected: {spell_name} ({result})"
