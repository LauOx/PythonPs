#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def testing_factory(factory: CreatureFactory) -> None:
    """"""
    print("Testing factory")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def battle(factory_1: CreatureFactory, factory_2: CreatureFactory) -> None:
    """"""
    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()
    print("Testing battle")
    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())
    print(" fight!")
    print(creature_1.attack())
    print(creature_2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    testing_factory(flame_factory)
    print()
    testing_factory(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)


main()
