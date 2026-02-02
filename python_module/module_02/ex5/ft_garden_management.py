#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterLvlError(GardenError):
    pass


class SunError(GardenError):
    pass


class TankError(GardenError):
    pass


class Plant:
    def __init__(self, name, water, sun):
        if not name:
            raise PlantError("Error: Plant name cannot be empty!")
        self.name = name
        self.water = water
        self.sun = sun

    def check_healthy(self):
        if self.water < 1:
            raise WaterLvlError(
                f"Error: Water level {self.water} is too low (min 1)")
        elif self.water > 10:
            raise WaterLvlError(
                f"Error: Water level {self.water} is too high (max 10)")
        if self.sun < 2:
            raise SunError(
                f"Error: sun hours {self.sun} is too low (min 2)")
        elif self.sun > 12:
            raise SunError(
                f"Error: sun hours {self.sun} is too high (max 12)")
        print(f"{self.name}: healthy (water: {self.water}, sun: {self.sun})")


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, plant_name, water, sun):
        try:
            plant = Plant(plant_name, water, sun)
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self, tank):
        WateringSystem.opening_system()
        try:
            for plant in self.plants:
                try:
                    TankSystem.use(tank, 1)
                except TankError as e:
                    print(e)
                plant.water += 1
                print(f"Watering {plant.name} - success")
            print("Watering completed successfully!")
        finally:
            WateringSystem.closing_system()

    @staticmethod
    def check_plant_health(plant):
        try:
            Plant.check_healthy(plant)
        except (WaterLvlError, SunError) as e:
            print(e)


class WateringSystem:
    count_opening = 0
    count_closing = 0

    @classmethod
    def opening_system(cls):
        print("Opening watering system")
        WateringSystem.count_opening += 1

    @classmethod
    def closing_system(cls):
        cls.count_closing += 1
        print("Closing watering system (cleanup)")

    @classmethod
    def get_state(cls):
        if cls.count_opening == cls.count_closing:
            return "\nCleanup always happens, even with errors!"
        else:
            return "\nYou failed!"


class TankSystem:
    def __init__(self, water):
        self.water = water

    def refill(self, quantity):
        self.water += quantity
        print("System recovered and continuing...")

    def use(self, quantity):
        if self.water - quantity < 0:
            raise TankError("Caught GardenError: Not enough water in tank")
        else:
            self.water -= quantity


def add_plant(bob: GardenManager):
    print("\nAdding plants to garden...")
    bob.add_plants("tomato", 4, 8)
    bob.add_plants("lettuce", 10, 6)
    bob.add_plants(None, 2, 6)


def watering(bob: GardenManager, tank: TankSystem):
    print("\nWatering plants...")
    try:
        bob.water_plants(tank)
    except TankError as e:
        print(e)


def checking_plant_health(bob: GardenManager):
    print("\nChecking plant health...")
    for plant in bob.plants:
        try:
            plant.check_healthy()
        except (WaterLvlError, SunError) as e:
            print(e)


def recovery_tank(bob: GardenManager, tank: TankSystem):
    print("\nTesting error recovery...")
    try:
        tank.use(3)
    except TankError as e:
        print(e)
        tank.refill(10)


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    bob: GardenManager = GardenManager()
    tank: TankSystem = TankSystem(2)
    add_plant(bob)
    watering(bob, tank)
    checking_plant_health(bob)
    recovery_tank(bob, tank)
    print("\nGarden management system test complete!")
