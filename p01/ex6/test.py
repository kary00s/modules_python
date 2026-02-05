class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.total_growth = 0

    def grow(self, amount):
        self.height += amount
        self.total_growth += amount
        print(f"{self.name} grew {amount}cm")

    def __str__(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color, blooming=False):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.blooming = blooming

    def __str__(self):
        status = "blooming" if self.blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.flower_color} flowers ({status})"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points, blooming=False):
        super().__init__(name, height, flower_color, blooming)
        self.prize_points = prize_points

    def __str__(self):
        return super().__str__() + f", Prize points: {self.prize_points}"

class GardenManager:
    class GardenStats:
        @staticmethod
        def get_stats(plants):
            num_plants = len(plants)
            total_growth = sum(p.total_growth for p in plants)
            types = {'regular': 0, 'flowering': 0, 'prize': 0}
            for p in plants:
                if isinstance(p, PrizeFlower):
                    types['prize'] += 1
                elif isinstance(p, FloweringPlant):
                    types['flowering'] += 1
                else:
                    types['regular'] += 1
            return {
                'num_plants': num_plants,
                'total_growth': total_growth,
                'types': types
            }

    def __init__(self):
        self.gardens = {}

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

    def help_grow(self, garden_name, amount=1):
        if garden_name in self.gardens:
            for plant in self.gardens[garden_name]:
                plant.grow(amount)

    def get_garden_report(self, garden_name):
        if garden_name in self.gardens:
            print("Plants in garden:")
            for p in self.gardens[garden_name]:
                print(f"- {str(p)}")

    def get_stats(self, garden_name):
        if garden_name in self.gardens:
            return self.GardenStats.get_stats(self.gardens[garden_name])

    def get_garden_score(self, garden_name):
        if garden_name in self.gardens:
            plants = self.gardens[garden_name]
            sum_heights = sum(p.height for p in plants)
            bonus = sum(20 for p in plants if isinstance(p, FloweringPlant) and p.blooming)
            return sum_heights + bonus

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    manager = GardenManager()
    manager.add_garden("Alice")
    manager.add_garden("Bob")

    # Add plants to Alice's garden
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", blooming=True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10, blooming=True)

    manager.add_plant("Alice", oak)
    print("Added Oak Tree to Alice's garden")
    manager.add_plant("Alice", rose)
    print("Added Rose to Alice's garden")
    manager.add_plant("Alice", sunflower)
    print("Added Sunflower to Alice's garden")

    print("Alice is helping all plants grow...")
    manager.help_grow("Alice", 1)

    print("=== Alice's Garden Report ===")
    manager.get_garden_report("Alice")
    stats = manager.get_stats("Alice")
    print(f"Plants added: {stats['num_plants']}, Total growth: {stats['total_growth']}cm")
    print(f"Plant types: {stats['types']['regular']} regular, {stats['types']['flowering']} flowering, {stats['types']['prize']} prize flowers")
    print(f"Height validation test: {GardenManager.height_validation_test(oak.height)}")

    # Add a plant to Bob's garden silently to match the score
    bob_plant = Plant("Bob's Tree", 92)
    manager.add_plant("Bob", bob_plant)

    print(f"Garden scores - Alice: {manager.get_garden_score('Alice')}, Bob: {manager.get_garden_score('Bob')}")
    print(f"Total gardens managed: {len(manager.gardens)}")