#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import cast
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    pass

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    pass

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            c_creature = cast(Creature | TransformCapability, creature)
            print(c_creature.transform())
            print(c_creature.attack())
            print(c_creature.revert())
        else:
            raise BattleStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
                )


class DefensiveStrategy(BattleStrategy):
    pass

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            c_creature = cast(Creature | HealCapability, creature)
            print(c_creature.attack())
            print(c_creature.heal())
        else:
            raise BattleStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
                )
