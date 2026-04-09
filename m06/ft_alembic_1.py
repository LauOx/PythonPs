#!/usr/bin/env python3
from elements import create_water


def alembic_1() -> None:
    """"""
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print("Testing create_water:", create_water())


alembic_1()
