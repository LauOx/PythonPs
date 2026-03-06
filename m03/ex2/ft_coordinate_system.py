import sys
import math


def coordinate_system():
    """
    """
    print("=== Game Coordinate System ===\n")
    ar_len = len(sys.argv)
    error_tracker = False
    # define parsing if arg entered as "str"
    if ar_len == 2:
        parsing = sys.argv[1].split()
        try:
            if len(parsing) != 3:
                raise ValueError("Coordinate system needs 3 values "
                                 f"(entered {len(parsing)})")
            try:
                coor = f'"{parsing[0]},{parsing[1]},{parsing[2]}"'
                for x in parsing:
                    int(x)
                print(f'Parsing coordinates: {coor}')
            except ValueError as e:
                error_tracker = True
                print(f"Parsing invalid coordinates: {coor}")
                print(f"Error parsing coordinates: {e}")
                print('Error details - Type: ValueError, '
                      f'Args ("{e}".)')
        except ValueError as e:
            error_tracker = True
            print(f"Caught ValueError: {e}")
    # define parsing if entered 3 values
    elif len(sys.argv) == 4:
        parsing = sys.argv[1:]
    # raise error and end program if number of values is incorrect
    else:
        try:
            raise ValueError("coordinate system needs 3 values "
                             f"(entered {len(sys.argv) - 1})")
        except ValueError as e:
            error_tracker = True
            print(f"Caught ValueError: {e}")
    # parsing is defined
    if not error_tracker:
        try:
            coor = f'"{parsing[0]},{parsing[1]},{parsing[2]}"'
            for x in parsing:
                int(x)
        except ValueError as e:
            error_tracker = True
            print(f"Parsing invalid coordinates: {coor}")
            print(f"Error parsing coordinates: {e}")
            print('Error details - Type: ValueError, '
                  f'Args ("{e}".)')
    # create tuple coordinates
    if not error_tracker:
        x2 = int(parsing[0])
        y2 = int(parsing[1])
        z2 = int(parsing[2])
        coordinates = (x2, y2, z2)
        # define start point
        start_point = (0, 0, 0)
        x1, y1, z1 = start_point
        distance = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
        print(f"Position created: {coordinates}")
        print(f"Distance between {start_point} and {coordinates}: "
              f"{distance:.2f}")
        print()
        # demonstration
        print("Unpacking demonstration:")
        print(f"Player at x={x2}, y={y2}, z={z2}")
        print(f"Coordinates at X={x2}, Y={y2}, Z={z2}")


if __name__ == "__main__":
    """
    """
    coordinate_system()
