#!/usr/bin/env python3
from .elements import create_air, create_earth
import elements


def healing_potion() -> str:
    """"""
    ret = (
        "Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
        )
    return ret


def strength_potion() -> str:
    """"""
    ret = (
        "Strength potion brewed with "
        f"'{elements.create_fire()}' and '{elements.create_water()}'"
        )
    return ret
