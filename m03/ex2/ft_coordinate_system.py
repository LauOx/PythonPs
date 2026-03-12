#!/usr/bin/env python3
import sys
import math


def check_arg_len(arguments: list) -> None:
    """
    checks how many arguemnts entered
    """
    if len(arguments) != 3:
        raise ValueError("Coordinate system needs 3 values "
                         f"(entered {len(arguments)})")


def compute_distance(arguments: str) -> None:
    """
    calculates the distance between two 3D points,
    using the Euclidean distance formula
    """
    # change str to tuple
    x2 = int(arguments[0])
    y2 = int(arguments[1])
    z2 = int(arguments[2])
    coordinates = (x2, y2, z2)
    # define tuple start point
    start_point = (0, 0, 0)
    x1, y1, z1 = start_point
    # math
    distance = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    print(f"Position created: {coordinates}")
    print(f"Distance between {start_point} and {coordinates}: "
          f"{distance:.2f}")
    print()
    # demonstration
    print("Unpacking demonstration:")
    print(f"Player at x={x2}, y={y2}, z={z2}")
    print(f"Coordinates at X={x2}, Y={y2}, Z={z2}")


def manual_coordinates() -> list:
    """
    This function gives coordinates as an example
    if coordinates were not given.
    """
    manual_coor = [10, 20, 5]
    return manual_coor


def coordinate_system() -> None:
    """
    This function reads coordinates from terminal (or from manual_coordinates())
    and checks all posible erros before computing with compute_distance()
    """
    print("=== Game Coordinate System ===\n")
    ar_len = len(sys.argv)
    error_tracker = False
    # define parsing if arg entered as "str" and checks errors
    if ar_len == 1:
        arguments = manual_coordinates()
    elif ar_len == 2:
        arguments = sys.argv[1].split()
        try:
            check_arg_len(arguments)
        except ValueError as e:
            error_tracker = True
            print(f"Caught ValueError: {e}")
    # define parsing if entered 3 values
    elif ar_len == 4:
        arguments = sys.argv[1:]
    # raise error and if number of arguments is incorrect
    else:
        try:
            raise ValueError("coordinate system needs 3 values "
                             f"(entered {len(sys.argv) - 1})")
        except ValueError as e:
            error_tracker = True
            print(f"Caught ValueError: {e}")
    # checks all arguments are int
    if not error_tracker:
        try:
            coor = f'"{arguments[0]},{arguments[1]},{arguments[2]}"'
            for x in arguments:
                int(x)
            if ar_len == 2:
                print(f'Parsing coordinates: {coor}')
        except ValueError as e:
            error_tracker = True
            print(f"Parsing invalid coordinates: {coor}")
            print(f"Error parsing coordinates: {e}")
            print('Error details - Type: ValueError, '
                  f'Args ("{e}".)')
    # compute distance
    if not error_tracker:
        compute_distance(arguments)


if __name__ == "__main__":
    """
    """
    coordinate_system()
