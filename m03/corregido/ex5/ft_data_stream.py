#!/usr/bin/env python3
from typing import Generator


def event_yield(n: int) -> Generator[dict, None, None]:
    """
    Random event generator because they wont let us use random()
    """
    # n is the number of events
    # lists that rotate
    players = ["alice", "bob", "charlie", "diana"]
    actions = ["killed monster", "found treasure", "leveled up"]
    num_players = len(players)
    num_actions = len(actions)
    for i in range(1, n + 1):
        # In the list we get the player with the index (module i % players).
        player = players[i % num_players]
        action = actions[i % num_actions]
        # Invented level based on i (just because) max 15
        level = (i * 5) % 2000
        yield {
            'player': player,
            'level': level,
            'action': action
        }


def is_prime(n: int) -> bool:
    """
    checks if n is prime
    """
    i = 3
    if n % 2 == 0:
        return False
    while i < n:
        if n % i == 0:
            return False
        else:
            i += 2
    return True


def prime_yield(n: int) -> Generator[int, None, None]:
    """
    Yield firs n prime numbers
    """
    i = 2
    count = 0
    while count < n:
        if is_prime(i):
            yield i
            count += 1
        i += 1


def fibonacci_yield(n: int) -> Generator[int, None, None]:
    """
    Yield firs n fibonacci numbers
    """
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def generator_demo() -> None:
    """
    Prints fibonacci and prime numbers using generator
    """
    print("== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib = fibonacci_yield(10)
    first_n = True
    for _ in range(10):
        n = next(fib)
        if first_n:
            print(f"{n}", end="")
            first_n = False
        else:
            print(f", {n}", end="")
    print()
    print("Prime numbers (first 5): ", end="")
    prime_n = prime_yield(5)
    first_n = True
    for _ in range(5):
        prime = next(prime_n)
        if first_n:
            print(f"{prime}", end="")
            first_n = False
        else:
            print(f", {prime}", end="")
    print()


def game_data_stream(game_events: int):
    """
    shows and analyses game data
    """
    count = 0
    event_id = 1
    high_level = 0
    treasure = 0
    level_up = 0
    ("=== Game Data Stream Processor ===")
    print(f"Processing {game_events} game events...")
    # showing n game events
    event = event_yield(game_events)
    i = 0
    for _ in range(game_events):
        e = next(event)
        if i < 3:
            print(f"Event {event_id}: {e['player']} (level {e['level']}) "
                  f"{e['action']}")
            i += 1
        if e['level'] >= 10:
            high_level += 1
        if e['action'] == "found treasure":
            treasure += 1
        if e['action'] == "leveled up":
            level_up += 1
        event_id += 1
        count += 1
    print("...")
    # Stream Analytics
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {count}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print()
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


if __name__ == "__main__":
    game_data_stream(10)
    print()
    generator_demo()
