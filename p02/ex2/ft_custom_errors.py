class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_watering_garden() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garder error: {e}\n")


def check_plant_garden() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garder error: {e}")


def garden_operations(type):

    if type == "PlantError":
        try:
            print("Testing PlantError ...")
            raise PlantError("The tomato plant is wilting!")
        except PlantError as error:
            print(f"caught PlantError : {error}")

    elif type == "WaterError":
        try:
            print("\nTesting WaterError ...")
            raise WaterError("Not enough water in the tank!")
        except WaterError as error:
            print(f"caught PlantError : {error}")

    elif type == "GardenError":
        print("\nTesting catching all garden errors...")
        check_plant_garden()
        check_watering_garden()


def test_error_types():
    type = ["PlantError", "WaterError", "GardenError"]
    for p in type:
        garden_operations(p)

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
