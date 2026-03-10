#!/usr/bin/env python3
import sys


def score_cruncher() -> None:
    """
    This function shows statistics based on the score data given
    """
    list_len = len(sys.argv)
    scores = []
    error_trace = False
    print("=== Player Score Analytics ===")
    if list_len > 2:
        for x in sys.argv[1:]:
            try:
                scores.append(int(x))
            except ValueError:
                print(f"'{x}' is not a valid number")
                error_trace = True
        if not error_trace:
            # data printed:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / (list_len - 1)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
            print()
    else:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")


if __name__ == "__main__":
    """
    main function
    """
    score_cruncher()
