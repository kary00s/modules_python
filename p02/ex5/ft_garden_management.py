class WaterError(Exception):
    pass


class PlantError(Exception):
    pass

class GardenManager:
    list = []
    def __init__(self, name, water_level, sunlight_hours):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def Check_water_level(self):
        if self.water_level >= 10:
            raise PlantError(f"Water level {self.water_level} is too high (max 10)")
        elif self.water_level <= 2:
            raise PlantError(f"Water level {self.water_level} is too low (min 2)")

    def Check_sunlight(self):
        if self.sunlight_hours >= 12:
            raise PlantError(f"Sunlight hours {self.sunlight_hours} is too high (max 10)")
        elif self.sunlight_hours <= 2:
            raise PlantError(f"Sunlight hours {self.sunlight_hours} is too low (min 2)")

    def Check_plant_name(name):
        if len(name) == 0:
            raise PlantError("Plant name cannot be empty!")

    def add_plants(self):
        try:
            GardenManager.Check_plant_name(self.name)
            GardenManager.list.append(self)
        except PlantError as error:
            print(f"Error : {error}")
        else:
            print(f"Added {self.name} successfully")

    def watering(self):
        if self.water_level > 5:
            print(f"Watering {self.name} - success")
            self.water_level -= 5
        else:
            raise WaterError("Not enough water in tank")

    def watering_plants():
        try:
            for plant in GardenManager.list:
                GardenManager.watering(plant)
        except WaterError as error:
            print(f"Error : {error}")
        finally:
            print("Closing watering system (cleanup)")

    def Check_plant_health():
        for plant in GardenManager.list:
            try:
                GardenManager.Check_water_level(plant)
                GardenManager.Check_sunlight(plant)
            except PlantError as error:
                print(f"Error : {error}")
            else:
                print(f"{plant.name} : healthy (water : {plant.water_level}, sun : {plant.sunlight_hours})")



def test_garden_management(plant_list):
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    for plant in plant_list:
        GardenManager.add_plants(plant)

    print("\nWatering plants...")
    print("Opening watering system")
    GardenManager.watering_plants()

    print("\nChecking plant health...")
    GardenManager.Check_plant_health()

test_garden_management( [
                        GardenManager("tomato", 5, 8),
                        GardenManager("lettuce", 8, 15),
                        GardenManager("", 4, 7)])