#!/usr/bin/env python3
from alchemy.elements import create_air


def alembic_3() -> None:
    """"""
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using "
          "'from ... import ...' structure")
    print(create_air())


alembic_3()
