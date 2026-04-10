#!/usr/bin/env python3
#absolute, called from root
from elements import create_fire
# relative, called from transmutation (.. upper folder)
from ..potions import strength_potion, create_air


def lead_to_gold() -> str:
    """"""
    ret = (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()} and {strength_potion()} mixed with {create_fire()}'")
    return ret
