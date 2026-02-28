class WaterError(Exception):
    pass


class PlantError(Exception):
    pass


class GardenError(Exception):
    pass


class GardenManager:
    list = []
    tank_size = 2

    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

    def Check_water_level(self) -> None:
        if self.water_level >= 10:
            raise PlantError(f"Water level "
                             f"{self.water_level} is too high (max 10)")
        elif self.water_level <= 2:
            raise PlantError(f"Water level"
                             f" {self.water_level} is too low (min 2)")

    def Check_sunlight(self) -> None:
        if self.sunlight_hours >= 12:
            raise PlantError(
                f"Sunlight hours {self.sunlight_hours} is too high (max 10)"
            )
        elif self.sunlight_hours <= 2:
            raise PlantError(f"Sunlight hours "
                             f"{self.sunlight_hours} is too low (min 2)")

    def Check_plant_name(name) -> None:
        if len(name) == 0:
            raise PlantError("Plant name cannot be empty!")

    def add_plants(self) -> None:
        try:
            GardenManager.Check_plant_name(self.name)
            GardenManager.list.append(self)
        except PlantError as error:
            print(f"Error : {error}")
        else:
            print(f"Added {self.name} successfully")

    def check_tank_level() -> None:
        if GardenManager.tank_size > 5:
            pass
        else:
            raise GardenError("Not enough water in tank")

    def watering_plants() -> None:
        try:
            for plant in GardenManager.list:
                GardenManager.Check_water_level(plant)
                print(f"Watering {plant.name} - success")
                GardenManager.tank_size -= 5
        except WaterError as error:
            print(f"Error : {error}")
        finally:
            print("Closing watering system (cleanup)")

    def Check_plant_health() -> None:
        for plant in GardenManager.list:
            try:
                GardenManager.Check_water_level(plant)
                GardenManager.Check_sunlight(plant)
            except PlantError as error:
                print(f"Error cheaking {plant.name} : {error}")
            else:
                print(
                    f"{plant.name} : healthy (water : {plant.water_level},"
                    f" sun : {plant.sunlight_hours})"
                )


def test_garden_management(plant_list: list) -> None:
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    for plant in plant_list:
        GardenManager.add_plants(plant)

    print("\nWatering plants...")
    print("Opening watering system")
    GardenManager.watering_plants()

    print("\nChecking plant health...")
    GardenManager.Check_plant_health()

    print("\nTesting error recovery...")
    try:
        GardenManager.check_tank_level()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        print("System recovered and continuing...")
    finally:
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    list = [
            GardenManager("tomato", 5, 8),
            GardenManager("lettuce", 5, 15),
            GardenManager("", 4, 7),
        ]
    test_garden_management(list)
