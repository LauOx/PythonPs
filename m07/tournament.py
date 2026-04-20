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
    # Round robin tournament
    for i in range(len(opponents)):
        # range can take 3 data: (start, end, step): from i+1 to len
        for e in range(i + 1, len(opponents)):
            # extract tuples
            factory_1, strategy_1 = opponents[i]
            factory_2, strategy_2 = opponents[e]
            # create creatures
            creature_1 = factory_1.create_base()
            creature_2 = factory_2.create_base()
            print("* Battle *")
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")
            strategy_1.act(creature_1)
            strategy_2.act(creature_2)
            print()


def main() -> None:
    """"""
    tournament_0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    tournament_1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy),
    ]
    tournament_2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    # Tournament 0
    print("Tournament 0 (basic)")
    print("*** Tournament ***")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print(len(tournament_0), "opponents involved\n")
    battle(tournament_0)
    # Tournament 1
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print(len(tournament_1), "opponents involved\n")
    try:
        battle(tournament_1)
    except BattleStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")
    # Tournament 2
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print(len(tournament_2), "opponents involved\n")
    battle(tournament_2)


main()
