from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ing_lower = ingredients.lower()
    ing_list = dark_spell_allowed_ingredients()
    for item in ing_list:
        if item in ing_lower:
            return (ing_lower + " - VALID")
    return (ing_lower + " - INVALID")
