class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass
# class WaterError(GardenError):
    # pass

def check_watering(watering):
    try:
        if watering < 2:
            raise PlantError
    except PlantError:
        print("Error")
def garden_operations(type):

    if type == "PlantError":
        try:
            if watering < 2:
                raise PlantError
        except PlantError:
            print("caught PlantError : The tomato plant is wilting!")
    # elif type == "WaterError":
    # elif type == "garden_errors":
def test_error_types():
    type = [
        "PlantError",
        "WaterError",
        "garden_errors"
    ]
    for p in type:
        garden_operations(p)

test_error_types()