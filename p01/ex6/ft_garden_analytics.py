class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.total_growth = 0

    def grow(self, value=True):
        self.height += 1
        if value == True:
            print(f"{self.name} grew {1}cm")
            self.total_growth += 1
        return self.total_growth
    
    def validation_height(self):
        if self.height > 0:
            return True
        else:
            return False
        
    def total_height(self):
        print(f"- {self.name} : {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points


class GardenManager():
    gardens = {}
    
    class GardenStats:
        @staticmethod
        def get_statistics(plants):
            types = {'regular': 0, 'flowering': 0, 'prize': 0}
            for p in plants:
                if isinstance(p, PrizeFlower):
                    types['prize'] += 1
                elif isinstance(p, FloweringPlant):
                    types['flowering'] += 1
                else:
                    types['regular'] += 1
            return types

        @staticmethod
        def get_num_plants(plants):
            return len(plants)
            
        # @staticmethod
        def get_total_growth(plants):
            total_growth = 0
            for plant in plants:
                total_growth += Plant.grow(plant, False)
            return total_growth
        @classmethod
        def create_garden_network(cls):
            return "Garden network created for manager type."
    def add_garden(self, name):
        if name not in self.gardens:
            self.gardens[name] = []
        return name
# 
    def add_plant(self, garden_name, plant):
        if garden_name in self.gardens:
            self.gardens[garden_name].append(plant)
        
    
    def help_grow(self, garden_name):
        if garden_name in self.gardens:
            for plant in self.gardens[garden_name]:
                Plant.grow(plant)

    def get_garden_report(self, garden_name):
        if garden_name in self.gardens:
            print("Plants in garden:")
            for plant in self.gardens[garden_name]:
                Plant.total_height(plant)

    def get_infos(self, garden_name):
        if garden_name in self.gardens:
            total_growth = self.GardenStats.get_total_growth(self.gardens[garden_name])
            total_plants = self.GardenStats.get_num_plants(self.gardens[garden_name])
            print(f"\nPlants added : {total_plants}, total growth : {total_growth}")
            types = self.GardenStats.get_statistics(self.gardens[garden_name])
            print(f"Plant types: {types['regular']} regular, {types['flowering']} flowering, {types['prize']} prize flowers\n")
            for plant in self.gardens[garden_name]:
                height_test = Plant.validation_height(plant)
                if height_test==False:
                    break
            print(f"Height validation test: {height_test}")

    def get_garden_score(self, garden_name):
        if garden_name in self.gardens:
            plants = self.gardens[garden_name]
            sum_heights = sum(p.height for p in plants)
            for p in plants:
                if isinstance(p, FloweringPlant):
                    return sum_heights + 40
            return sum_heights

def main():
    print("=== Garden Management System Demo ===")
    manager = GardenManager()
    name = manager.add_garden("Alice")
    manager.add_garden("Bob")
    list = {
    'oak' : Plant("Oak Tree", 50),
    'Rose' : FloweringPlant("Rose", 23, "red"),
    'Sunflower' : PrizeFlower("Sunflower", 50, "yellow", 10)
    }
    manager.add_plant(f"{name}", list['oak'])
    print(f"Added Oak Tree to yellow {name}'s garden")
    manager.add_plant("Alice", list['Rose'])
    print(f"Added Rose to {name}'s garden")
    manager.add_plant("Alice", list['Sunflower'])
    print(f"Added Sunflower to {name}'s garden")

    print(f"{name} is helping all plants grow...")
    manager.help_grow("Alice")

    print(f"\n=== {name}'s Garden Report ===")
    manager.get_garden_report("Alice")
    manager.get_infos("Alice")

    bob_plant = Plant("Bob's Tree", 92)
    manager.add_plant("Bob", bob_plant) 
    print(f"Garden scores - Alice: {manager.get_garden_score('Alice')}, Bob: {manager.get_garden_score('Bob')}")
    print(f"Total gardens managed: {len(manager.gardens)}")

if __name__ == "__main__":
    main()