#!/usr/bin/env python3
# importing just the module 'import .light_validator
# and calling the function needed light_validator.validate_ingredients
# the circular dependencies can also be avoided.


def light_spell_allowed_ingredients() -> list:
    """"""
    ingredients = ["earth", "air", "fire", "water"]
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """"""
    from .light_validator import validate_ingredients
    val_str = "(" + validate_ingredients(ingredients) + ")"
    val_bool = True if "VALID" in val_str.split() else "rejected"
    spell_record = "recorded" if val_bool else "rejected"
    ret = f"Spell {spell_record}: {spell_name} {val_str}"
    return ret

# moving imports to the bottom of the file
# also helps to avoid circular dependencies
