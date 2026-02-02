#!/usr/bin/env python3

def game_event_stream():
    players = ["alice", "bob", "charlie"]
    events = ["killed monster", "found treasure", "leveled up"]
    level = [5, 12, 8]

    for i in range(3):
        yield (f"Event {i + 1}: Player {players[i % 3]} "
               f"(level {level[i]}) {events[i % 3]}")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, (a + b)


def prime_numbers():
    n = 2
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
    event_count = 0
    for event in game_event_stream():
        print(event)
        event_count += 1
    print("...\n")
    print("=== Generator Demonstration ===")
    n = 10
    str_ = f"Fibonacci sequence (first {n}):"
    value = fibonacci(n)
    print(f"Fibonacci sequence (first {n}): {next(value)}, {next(value)}, "
          f"{next(value)}, {next(value)}, {next(value)}, {next(value)}, "
          f"{next(value)}, {next(value)}, {next(value)}, {next(value)}")
    prime = prime_numbers()
    n = 5
    solution = ", ".join(str(next(prime)) for _ in range(n))
    print(f'Prime numbers (first {n}): {solution}')
