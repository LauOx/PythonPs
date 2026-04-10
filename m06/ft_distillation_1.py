#!/usr/bin/env python3

import alchemy


def distillation_1() -> None:
    """"""
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print("Testing strength_potion:", alchemy.strength_potion())
    print("Testing heal alias:", alchemy.heal())


distillation_1()
