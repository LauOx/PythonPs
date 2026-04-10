#!/usr/bin/env python3
"""
Set up the grimoire package and expose selected functions.
"""

from .light_spellbook import light_spell_allowed_ingredients
from .light_spellbook import light_spell_record
from .light_validator import validate_ingredients
from .dark_spellbook import dark_spell_allowed_ingredients
from .dark_spellbook import dark_spell_record
from .dark_validator import dark_validate_ingredients

__all__ = [
    "light_spell_allowed_ingredients",
    "light_spell_record",
    "validate_ingredients",
    "dark_spell_allowed_ingredients"
    "dark_spell_record",
    "dark_validate_ingredients"
    ]
