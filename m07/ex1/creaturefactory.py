#!/usr/bin/env python3

from ex0.creaturefactory import CreatureFactory
from ex0.creature import Creature
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    pass

    def create_base(self) -> Creature:
        """"""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """"""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    pass

    def create_base(self) -> Creature:
        """"""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """"""
        return Morphagon()
