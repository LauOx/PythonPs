#!/usr/bin/env python3
from .dark_spellbook import dark_spell_allowed_ingredients

def  dark_validate_ingredients(ingredients: str) -> str:
    """"""
    # by importing the package after the function has started
    # circular dependencies are avoided
    allowed = dark_spell_allowed_ingredients()
    entered = ingredients.split()
    ret = ingredients + " - "
    validate = False
    for e in entered:
        if e.lower() in allowed:
            validate = True
    ret += "VALID" if validate else "UNVALID"
    return ret
