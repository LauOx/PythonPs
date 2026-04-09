#!/usr/bin/env python3
import alchemy.elements


def alembic_2() -> None:
    """"""
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", alchemy.elements.create_earth())


alembic_2()
