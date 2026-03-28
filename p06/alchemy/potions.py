from alchemy import elements


def healing_potion():
    ret = f"Healing potion brewed with {elements.create_fire()}"
    ret += f"and {elements.create_water()}"
    return ret


def strength_potion():
    ret = f"Strength potion brewed with {elements.create_earth()}"
    ret += f" and {elements.create_fire()}"
    return ret


def invisibility_potion():
    ret = f"Invisibility potion brewed with {elements.create_air()}"
    ret += f" and {elements.create_water()}"
    return ret


def wisdom_potion():
    ret = f"Wisdom potion brewed with all elements: [{elements.create_air()}"
    ret += f", {elements.create_fire()}, {elements.create_water()},"
    ret += f" {elements.create_earth()}"
    return ret
