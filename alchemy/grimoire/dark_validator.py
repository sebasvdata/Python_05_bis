from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for allowed in dark_spell_allowed_ingredients():
        if allowed in ingredients:
            return "VALID"
    return "INVALID"
