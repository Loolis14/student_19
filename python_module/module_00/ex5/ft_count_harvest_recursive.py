def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def loop(n: int) -> None:
        if n == 0:
            return
        loop(n - 1)
        print(f"Day {n}")
    loop(days)
    print("Harvest time!")
