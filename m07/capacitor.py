#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def testing_healing_factory(factory: HealingCreatureFactory) -> None:
    """"""
    print("Testing Creature with healing capability")
    base_creature = factory.create_base()
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal())
    evolved_creature = factory.create_evolved()
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal())
    print(evolved_creature.heal())


def testing_transform_factory(factory: TransformCreatureFactory) -> None:
    """"""
    print("Testing Creature with transform capability")
    base_creature = factory.create_base()
    print(" base:")
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform())
    print(base_creature.revert())
    evolved_creature = factory.create_evolved()
    print(" evolved:")
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform())
    print(evolved_creature.revert())


def main() -> None:
    """"""
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    testing_healing_factory(healing_factory)
    print()
    testing_transform_factory(transform_factory)


main()
