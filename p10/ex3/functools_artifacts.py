from functools import lru_cache, reduce, partial, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "max":
        return reduce(lambda x, y: x if x > y else y, spells)
    elif operation == "min":
        return reduce(lambda x, y: x if x < y else y, spells)
    elif operation == "sum":
        return reduce(lambda x, y: x + y, spells, 0)
    elif operation == "multiply":
        return reduce(lambda x, y: x * y, spells, 1)
    else:
        return 0

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    lightning_enchanter = partial(base_enchantment, power=50, element="lightning")
    ice = partial(base_enchantment, power=100, element="ice")
    fire = partial(base_enchantment, power=100, element="fire")
    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning_enchanter,
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(_: Any) -> callable:
    raise Exception("Invalid type for spell_dispatcher")


@spell_dispatcher.register
def _(damage_spell: int) -> callable:
    return lambda x: f"Damage spell: {damage_spell + x} damage"


@spell_dispatcher.register
def _(enchantment: str) -> callable:
    return lambda _: f"Enchantment: {enchantment.lower()}"


@spell_dispatcher.register
def _(multi_cast: list) -> callable:
    return lambda _: f"Multi-cast: {len(multi_cast)} spells"


def base_enchantment(power: int, element: str, target: str) -> str:
    return (
        f"Enchantment with power {power}"
        f" and element {element} applied to {target}"
    )

def main() -> None:
    try:
        spells = [20, 10, 1, 40, 30]

        print("Testing spell reducer...")
        print(f"Sum: {spell_reducer(spells, 'sum')}")
        print(f"Product: {spell_reducer(spells, 'multiply')}")
        print(f"Max: {spell_reducer(spells, 'max')}")

        print("\nTesting memoized fibonacci...")
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")

        print("\nTesting spell dispatcher...")
        damage = spell_dispatcher(37)
        enchantment = spell_dispatcher("Fireball")
        multi_cast = spell_dispatcher([1, 2, 3])

        print(damage(5))
        print(enchantment("Sword"))
        print(multi_cast(0))

        try:
            spell_dispatcher(3.14)
        except Exception:
            print("Unknown spell type")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()