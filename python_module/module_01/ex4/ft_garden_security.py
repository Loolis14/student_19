#!/usr/bin/env python3

class SecurePlant:
    """Class to maintain secure variables"""
    def __init__(self, name, height, day_old):
        self._name = name
        print("Plant created:", self._name)
        self._height = 0
        self._day_old = 0
        self.set_height(height)
        self.set_age(day_old)

    def __str__(self):
        return f"{self._name} ({self._height}cm, {self._day_old} days)"

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, day_old):
        if day_old < 0:
            print(f"Invalid operation attempted: age {day_old}cm [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._day_old = day_old
            print(f"Age updated: {self._day_old} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose}")
