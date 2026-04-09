#!/usr/bin/env
"""
Set up the alchemy package and expose selected functions.
"""

from .elements import create_air
from .potions import healing_potion, strength_potion

__all__= ["create_air", "healing_potion", "strength_potion"] # esto es lo que queda expuesto al importar el odulo
