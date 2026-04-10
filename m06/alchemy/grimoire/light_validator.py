#!/usr/bin/env python3

def  validate_ingredients(ingredients: str) -> str:
    """"""
    # by importing the package after the function has started
    # circular dependencies are avoided
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    entered = ingredients.split()
    ret = ingredients + " - "
    validate = False
    for e in entered:
        if e.lower() in allowed:
            validate = True
    ret += "VALID" if validate else "UNVALID"
    return ret
