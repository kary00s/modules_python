def mage_counter() -> callable:
    cnt = 0

    def counter_mages() -> int:
        nonlocal cnt
        cnt += 1
        return cnt

    return counter_mages


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulate(spell_power: int) -> int:
        nonlocal power
        power += spell_power
        return power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment_creator(factory: str) -> str:
        return f"{enchantment_type} {factory}"

    return enchantment_creator


def memory_vault() -> dict[str, callable]:
    vault_dict = {}

    def store(key: str, value: callable) -> None:
        if value is None:
            print("Memory not found")
            return
        vault_dict[key] = value
        print(f"Store '{key}' = {value(0)}")

    def recall(key: str) -> callable:
        value = vault_dict.get(key)
        if value is None:
            print("Recall 'unknown': Memory not found")
            return None
        print(f"Recall '{key}': {value(0)}")
        return value

    return {
        "store": store,
        "recall": recall,
    }


def main() -> None:
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Testing mage counter... ")
    print(f"counter_a Call 1:, {counter_a()}")
    print(f"counter_a Call 2:, {counter_a()}")
    print(f"counter_b Call 1:, {counter_b()}")

    base = 100
    accumulator_spells = spell_accumulator(base)
    print("\nTesting spell accumulator... ")
    print(f"base {base}, add 20, {accumulator_spells(20)}")
    print(f"base {base}, add 30, {accumulator_spells(30)}")

    names = ["Sword", "Shield"]
    enhancements = ["Flaming", "Frozen"]
    print("\nTesting enchantment factory... ")
    factory = zip(names, enhancements)
    for name, enhancement in factory:
        result = enchantment_factory(enhancement)
        print(result(name))

    vault = memory_vault()
    print("\nTesting memory vault... ")

    vault["store"]("secret", spell_accumulator(42))
    vault["recall"]("secret")
    vault["recall"]("unknown")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
