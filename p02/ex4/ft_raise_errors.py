def Check_water(water_level):
    if water_level >= 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level <= 2:
        raise ValueError(f"Water level {water_level} is too low (min 2)")


def Check_sunlight(sunlight_hours):
    if sunlight_hours >= 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
    elif sunlight_hours <= 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")


def Check_plant_name(plant_name):
    if len(plant_name) == 0:
        raise ValueError("Plant name cannot be empty!")


def Check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        Check_plant_name(plant_name)
        Check_water(water_level)
        Check_sunlight(sunlight_hours)
    except ValueError as error:
        print(f"Error : {error}")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    Check_plant_health("tomato",4, 4)

    print("\nTesting empty plant name...")
    Check_plant_health("", 5, 5)

    print("\nTesting bad water level...")
    Check_plant_health("tomato", 15, 5)

    print("\nTesting bad sunlight hours...")
    Check_plant_health("tomato", 5, 0)

    print("\nAll error raising tests completed!")
if __name__ == "__main__":
    test_plant_checks()