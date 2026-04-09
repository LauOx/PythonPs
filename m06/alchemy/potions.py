#!/usr/bin/env python3
from alchemy.elements import create_air, create_earth
import elements


def healing_potion() -> None:
    """"""
    ret = "“Healing potion brewed with "
    f"’[{create_earth()}]’ and ’[{create_air()}]”."
    return ret


def strength_potion() -> None:
    """"""
    ret = "“Strength potion brewed "
    f"with ’[{create_fire()}]’ and ’[{create_water()}]”"
    return ret
