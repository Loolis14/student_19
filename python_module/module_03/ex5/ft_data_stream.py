#!/usr/bin/env python3

"""Sixth Exercise."""


def game_event_stream():
    """Store 1000 events."""
    players: list[str] = ["alice", "bob", "charlie"]
    events: list[str] = ["killed monster", "found treasure", "leveled up"]
    level: list[int] = [5, 12, 8]

    for i in range(1000):
        yield (f"Event {i + 1}: Player {players[i % 3]} "
               f"(level {level[i % 3]}) {events[i % 3]}")


def fibonacci(n: int):
    """Store number of fibonnacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, (a + b)


def prime_numbers():
    """Store prime numbers."""
    n: int = 2
    while True:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")
    event_count: int = 0
    event = game_event_stream()

    while event_count < 3:
        print(next(event))
        event_count += 1
    print("...\n")
    print("=== Generator Demonstration ===")
    n: int = 10
    str_: str = f"Fibonacci sequence (first {n}):"
    value = fibonacci(n)
    print(f"Fibonacci sequence (first {n}): {next(value)}, {next(value)}, "
          f"{next(value)}, {next(value)}, {next(value)}, {next(value)}, "
          f"{next(value)}, {next(value)}, {next(value)}, {next(value)}")
    prime = prime_numbers()
    n = 5
    solution = ", ".join(str(next(prime)) for _ in range(n))
    print(f'Prime numbers (first {n}): {solution}')
