#!/usr/bin/env python3
# importing just the module 'import .light_validator
# and calling the function needed light_validator.validate_ingredients
# the circular dependencies can also be avoided.
from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    """"""
    ingredients = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """"""
    val_str = "(" + dark_validate_ingredients(ingredients) + ")"
    val_bool = True if "VALID" in val_str.split() else "rejected"
    spell_record = "recorded" if val_bool else "rejected"
    ret = f"Spell {spell_record}: {spell_name} {val_str}"
    return ret

# moving imports to the bottom of the file
# also helps to avoid circular dependencies
