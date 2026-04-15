#!/usr/bin/env python3

from typing import List, Tuple
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    BattleStrategyError
)
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0 import CreatureFactory, FlameFactory, AquaFactory

def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    """"""
    i = 0
    for creature in opponents:


def main() -> None:
    """"""
    flame_factory = FlameFactory()
    Aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    base



