from .. import potions, elements
from elements import create_fire


def lead_to_gold() -> str:
    air = elements.create_air()
    strength = potions.strength_potion()
    fire = create_fire()
    return ("Recipe transmuting Lead to Gold: brew "
            f"'{air}' and '{strength}' mixed with '{fire}'")
