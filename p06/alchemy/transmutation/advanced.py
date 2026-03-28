from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    ret = "Philosopher’s stone created using"
    ret += f"{lead_to_gold()} and {healing_potion()}"
    return ret


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
