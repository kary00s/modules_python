def spell_combiner(spell1: callable, spell2: callable) -> callable:
    if not callable(spell1) or not callable(spell2):
        raise ValueError("Spell1 and spell2 must be callable")

    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs),
    )


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    if not callable(base_spell):
        raise ValueError("Base spell must be callable")

    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    if not callable(condition) or not callable(spell):
        raise ValueError("Condition and spell must be callable")

    return lambda *args, **kwargs: (
        spell(*args, **kwargs)
        if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[callable]) -> callable:
    if not all(callable(spell) for spell in spells):
        raise ValueError("All spells must be callable")

    return lambda *args, **kwargs: [
        spell(*args, **kwargs) for spell in spells
    ]




def main() -> None:
    try:

        print("Testing spell combiner...")
        combined_spell = spell_combiner(
        lambda target: f"Fireball hits {target}",
        lambda target: f"Heals {target}",
        )
        spell_one, spell_two = combined_spell("dragon")
        print(f"Combined spell result: {spell_one}, {spell_two}\n")


        # print("Testing power amplifier...")
        # amplified_spell = power_amplifier(lambda x: x + 5, 3)
        # res = amplified_spell(2)
        # print(f"Amplified spell result: {res}\n")

        
        # print("Testing conditional caster...")
        # cond_cast = conditional_caster(
        #     lambda x: True if x > 10 else False, lambda _: "hell world"
        # )
        # print(f"Conditional caster result: {cond_cast(11)}\n")



        # print("Testing spell sequence...")
        # spells_callabes = spell_sequence(
        #     [lambda name: f"hello {name}" for _ in range(4)]
        # )
        # print("Spell sequence result: ", spells_callabes("1337"))


    except Exception as error:
        print(f"Error occured: {error}")


if __name__ == "__main__":
    main()