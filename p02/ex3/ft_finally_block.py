class Plant_error(Exception):
    pass

def check_tank_size(tank_size):
    if tank_size < 5:
        raise Plant_error("Error")


def normal_watering(plant):
    print(f"watering : {plant}")

def check_plant(plant):
    if isinstance(plant, str):
        return (plant)
    else:
        raise Plant_error("Error")


def water_plants(plant_list):
    tank_size = 10
    try:
        for plant in plant_list:
            check_plant(plant)
            check_tank_size(tank_size)
            normal_watering(plant)
            tank_size -= 5

    except Plant_error as e:
        print(f"{e}: Cannot water None - invalid plant!")

    finally:
        print("Closing watering system (cleanup)")


def main():
    plant_list = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    print("Opening watering system")
    for plant in plant_list:
        normal_watering(plant)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    print("Opening watering system")
    water_plants(plant_list)


if __name__ == "__main__":
    main()
