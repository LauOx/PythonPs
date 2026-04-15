#!/usr/bin/env python3

from ex0.creaturefactory import CreatureFactory
from ex0.creature import Creature
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    pass

    def create_base(creature_name: str) -> Creature:
        """"""
        return Sproutling()

    def create_evolved(creature_name: str) -> Creature:
        """"""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    pass

    def create_base(creature_name: str) -> Creature:
        """"""
        return Shiftling()

    def create_evolved(creature_name: str) -> Creature:
        """"""
        return Morphagon()
