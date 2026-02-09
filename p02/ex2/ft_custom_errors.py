class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass
class Plant:
    def __init__(self, name, last_days_watering):
        self.name = name
        self.last_days_watering = last_days_watering


def check_tank(size):
    if size < 5:
        print("Caught WaterError: Not enough water in the tank!")

def check_plant(self, last_day_watering):
    if last_day_watering > 2:
        

def garden_operations(type):

    if type == "PlantError":
        try:
            
            print("----------------------------------")
        except PlantError:
            print("Caught PlantError: The tomato plant is wilting!")
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