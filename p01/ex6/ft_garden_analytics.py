class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.total_growth = 0

    def grow(self):
        self.height += 1
        self.total_growth += 1
        print(f"{self.name} grew {1}cm")

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
    class GardenStats:
        @staticmethod
        def get_stats(plants):
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

        @staticmethod
        def get_total_growth(plants):
                return sum(p.total_growth for p in plants)
            

    def __init__(self):
        self.gardens = {}
    def get_list_plants(self):
        print(f"Plants added: {self.gardens['regular']}, Total growth: {self.gardens['regular']}cm")
    @classmethod
    def create_garden_network(cls):
        return "Garden network created for manager type."

    @staticmethod
    def height_validation_test(height):
        return height > 0

    def add_garden(self, name):
        if name not in self.gardens:
            self.gardens[name] = []

    def add_plant(self, garden_name, plant):
        if garden_name in self.gardens:
            self.gardens[garden_name].append(plant)
    
    def help_grow(self, garden_name):
        if garden_name in self.gardens:
            for plant in self.gardens[garden_name]:
                plant.grow()

    def get_garden_report(self, garden_name):
        if garden_name in self.gardens:
            print("Plants in garden:")
            for p in self.gardens[garden_name]:
                p.total_height()

    def get_stats(self, garden_name):
        if garden_name in self.gardens:
            return self.GardenStats.get_stats(self.gardens[garden_name])

    def get_garden_score(self, garden_name):
        if garden_name in self.gardens:
            plants = self.gardens[garden_name]
            sum_heights = sum(p.height for p in plants)
            bonus = sum(20 for p in plants if isinstance(p, FloweringPlant))
            return sum_heights + bonus

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    manager = GardenManager()
    manager.add_garden("Alice")
    manager.add_garden("Bob")

    # Add plants to Alice's garden
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    manager.add_plant("Alice", oak)
    print("Added Oak Tree to Alice's garden")
    manager.add_plant("Alice", rose)
    print("Added Rose to Alice's garden")
    list =  manager.add_plant("Alice", sunflower)
    print("Added Sunflower to Alice's garden")

    print("Alice is helping all plants grow...")
    manager.help_grow("Alice")

    print("=== Alice's Garden Report ===")
    manager.get_garden_report("Alice")
    stats = manager.get_stats("Alice")
    GardenManager.get_list_plants()
    # GardenManager.GardenStats.get_stats(plants)

    # print(f"Plants added: {}, Total growth: {}cm")
    # print(f"Plant types: {stats['types']['regular']} regular,)"
        #   f"{stats['types']['flowering']} flowering,"
        #   f" {stats['types']['prize']} prize flowers")
    
    # print(f"Height validation test: {GardenManager.height_validation_test(oak.height)}")

    bob_plant = Plant("Bob's Tree", 92)
    manager.add_plant("Bob", bob_plant)

    print(f"Garden scores - Alice: {manager.get_garden_score('Alice')}, Bob: {manager.get_garden_score('Bob')}")
    print(f"Total gardens managed: {len(manager.gardens)}")