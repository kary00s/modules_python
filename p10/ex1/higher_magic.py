from typing import Callable
from builtins import callable


def spell(target: str, power: int) -> str:
    return f"targeted {target} and power used is {power}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise Exception("call both Spell1 and spell2")

    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs),
    )


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise Exception("call all the spells")

    return lambda *args, **kwargs: [spell(*args, **kwargs) for spell in spells]


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise Exception("call the Base spell function")

    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise Exception("call both Condition and spell")

    return lambda *args, **kwargs: (
        spell(*args, **kwargs) if condition(*args, **kwargs) else
        "Spell fizzled"
    )


def main() -> None:
    try:

        print("Testing spell combiner...")
        combined_spell = spell_combiner(
            lambda direction: f"Fireball hits {direction}",
            lambda direction: f"Heals {direction}",
        )
        spell_one, spell_two = combined_spell("dragon")
        print(f"Combined spell result:{spell_one}, {spell_two}\n")

        print("Testing power amplifier...")
        Original = 10
        amplified_spell = power_amplifier(lambda x: x + Original, 3)
        res = amplified_spell(0)
        print(f"Original: {Original}, Amplified: {res}\n")

    except Exception as error:
        print(f"Error occured: {error}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
