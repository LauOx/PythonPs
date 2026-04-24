#!/usr/bin/env python3

from ex0.creaturefactory import CreatureFactory
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    pass

    def create_base(self) -> Sproutling:
        """"""
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        """"""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    pass

    def create_base(self) -> Shiftling:
        """"""
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        """"""
        return Morphagon()
