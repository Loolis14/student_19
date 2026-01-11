#!/usr/bin/env python3

class Plant():
    def __init__(self, name):
        super().__init__()
        if name:
            self.name = name
        else:
            raise PlantNameError(str(name))


class PlantNameError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Error: Cannot water {self.message} - invalid plant!"


class WateringSystem:
    count_opening = 0
    count_closing = 0

    @classmethod
    def opening_system(cls):
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


def water_plants(plant_list):
    WateringSystem.opening_system()
    try:
        for plant in plant_list:
            plante = Plant(plant)
            print(f"Watering {plante.name}")
        print("Watering completed successfully!")
    except PlantNameError as e:
        print(e)
    finally:
        WateringSystem.closing_system()


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    plant_list = ["tomato", None]
    print("\nTesting with error...")
    water_plants(plant_list)
    print(WateringSystem.get_state())
