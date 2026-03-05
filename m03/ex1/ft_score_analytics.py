import sys


def score_cruncher() -> None:
    """
    """
    list_len = len(sys.argv)
    scores = []
    i = 1
    print("=== Player Score Analytics ===")
    if list_len > 2:
        while i < list_len:
            scores.append(sys.argv[i])
            i += 1
        print(f"Scores processed: {scores}")
    else:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
    # append scores to list



if __name__ == "__main__":
    """
    """
    score_cruncher()
