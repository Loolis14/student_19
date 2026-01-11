#!/usr/bin/env python3
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterLvlError(GardenError):
    pass


class SunlightError(GardenError):
    pass


class TankError(GardenError):
    pass


class Plant:
    def __init__(self, name, water_level, sunlight):
        if name:
            self.name = name
        else:
            raise PlantError("Error: Plant name cannot be empty!")
        try:
            Plant(name, water_level, sunlight)
        except (WaterLvlError, SunlightError) as e:
            print(e)
        else:
            self.water_level = self.water_level
            self.sunlight = sunlight

    def check_healthy(self):
        if self.water_level < 1:
            raise WaterLvlError(
                f"Error: Water level {self.water_level} is too low (min 1)")
        elif self.water_level > 10:
            raise WaterLvlError(
                f"Error: Water level {self.water_level} is too high (max 10)")
        if self.sunlight < 2:
            raise SunlightError(
                f"Error: Sunlight hours {self.sunlight} is too low (min 2)")
        elif self.sunlight > 12:
            raise SunlightError(
                f"Error: Sunlight hours {self.sunlight} is too high (max 12)")


class GardenManager:
    def __init__(self, plants):
        self.plants = plants

    def add_plants(self, plant_name, *args):
        try:
            plant = Plant(plant_name, *args)
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except ValueError as e:
            print(e)

    def water_plants(self, tank):
        WateringSystem.opening_system()
        try:
            for plant in self.plants:
                TankSystem.use(tank, 1)
        except TankError as e:
            print(e)
        else:
            plant.water += 1
            print(f"Watering {plant.name} - success")
        finally:
            WateringSystem.closing_system()

    def check_plant_health(plant):
        try:
            Plant.check_healthy(plant)
        except (WaterLvlError, SunlightError) as e:
            print(e)


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


class TankSystem:
    def __init__(self, water):
        self.water = water

    def refill(self, quantity):
        self.water += quantity
    
    def use(self, quantity):
        if self.water - quantity  < 0:
            raise TankError("Caught GardenError: Not enough water in tank")
        else:
            self.water -= quantity
