from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ing_lower = ingredients.lower()
    ing_list = light_spell_allowed_ingredients()
    for item in ing_list:
        if item in ing_lower:
            return (ing_lower + " - VALID")
        return (ing_lower + " - INVALID")
