#!/usr/bin/env python3
import alchemy


def alembic_4() -> None:
    """"""
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: ", alchemy.create_air())
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print("Testing create_earth: ", alchemy.create_earth())
    except AttributeError as e:
        print(f"Got an exception: {e}")


alembic_4()
