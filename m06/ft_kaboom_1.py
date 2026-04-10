#!/usr/bin/env python3


def kboom_1() -> None:
    """"""
    print("=== Kaboom 1 ===")
    print("Test import now - THIS WILL RAISE AN EXCEPTION")
    try:
        import alchemy.grimoire.dark_spellbook as grimoire
        print(grimoire.dark_spell_record("Hell", "bats, frogs"))
    except ImportError as e:
        print(f"Your alchemist laboratory has just exploded! {e}")


kboom_1()
