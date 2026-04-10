#!/usr/bin/env python3

import alchemy.grimoire.light_spellbook as grimoire


def kboom_0() -> None:
    """"""
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell:",
          grimoire.light_spell_record("Fantasy", "Earth, wind and fire"))


kboom_0()
