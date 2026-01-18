#!/usr/bin/env python3

def game_event():
    for i in range(1, 1000):
        yield i


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, (a + b)


def prime_numbers(n):
    for i in range(2, n):
        if i 


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")
    events = game_event()
    print(f"Event {next(events)} : Player alice (level 5) killed monster")
    print(f"Event {next(events)} : Player bob (level 12) found treasure")
    print(f"Event {next(events)} : Player charlie (level 8) leveled up")
    print("...\n")
    n = 10
    value = fibonacci(n)
    print(f"Fibonacci sequence (first {n}): {next(value)}, {next(value)}, "
          f"{next(value)}, {next(value)}, {next(value)}, {next(value)}, "
          f"{next(value)}, {next(value)}, {next(value)}, {next(value)}")
