class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def plant_type(self):
        return "regular"

    def grow(self):
        print(f"{self.name} flower grew 1cm")
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
    
    def plant_type(self):
        return "flowering"

    def display(self):
        print(f"{self.name} (Flower) : {self.height} cm, {self.color} "
              "flowers (blooming) ", end=' ')


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, point):
        super().__init__(name, height, color)
        self.point = point

    def plant_type(self):
        return "prize"

    def display(self):
        self.height += 1
        print(f" Prize points: {self.point}")


class Garden:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
   
    def add_plant(self, plant):
        self.plants.append(plant)
        plant.display()
    
    def total_plants(self):
        return len(self.plants)

    def get_garden(cls):
        return cls

    def display():
        print(f"added {Plant.name} to {Garden.owner_name} garden")      


class GardenManager:
    gardens = []
    score = 0

    class GardenStats:
        def total_garden(self):
            return len(self.gardens) 

        def score(self):
            for i in self.gardens:
                score += 1
            return score
        
        def grow_garden_plants(self):
            for plant in self.plants:
                self.total_grow = plant.grow()
            return self.total_grow

    def garden_network(cls):
        return cls


def get_infos():
    print("=== Garden Management System Demo ===")



    print(f"\n=== {person.name}'s Garden Report ===")
    

get_infos()