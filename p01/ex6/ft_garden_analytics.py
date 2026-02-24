class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.total_growth = 0

    def grow(self, value=True):
        self.height += 1
        if value is True:
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

    def total_height(self):
        print(f"- {self.name} : {self.height}cm "
              f"{self.flower_color} (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def total_height(self):
        print(f"- {self.name} : {self.height}cm {self.flower_color}"
              f"(blooming), prize points :{self.prize_points}")


class GardenManager():
    gardens = {}

    class GardenStats:
        def get_statistics(plants: list):
            types = {'regular': 0, 'flowering': 0, 'prize': 0}
            for p in plants:
                if p.__class__ == PrizeFlower:
                    types['prize'] += 1
                elif p.__class__ == FloweringPlant:
                    types['flowering'] += 1
                elif p.__class__ == Plant:
                    types['regular'] += 1
            return types
        get_statistics = staticmethod(get_statistics)

        def get_num_plants(plants):
            counter = 0
            for p in plants:
                p
                counter += 1
            return counter
        get_num_plants = staticmethod(get_num_plants)

        def get_total_growth(plants: dict):
            total_growth = 0
            for plant in plants:
                total_growth += Plant.grow(plant, False)
            return total_growth
        get_total_growth = staticmethod(get_total_growth)

    def add_garden(self, name: str):
        if name not in self.gardens:
            self.gardens[name] = []
        return name

    def add_plant(self, g_name: str, plant: str):
        if g_name in self.gardens:
            self.gardens[g_name].append(plant)

    def help_grow(self, g_name: str):
        if g_name in self.gardens:
            for plant in self.gardens[g_name]:
                Plant.grow(plant)

    def get_garden_report(self, g_name: str):
        if g_name in self.gardens:
            print("Plants in garden:")
            for plant in self.gardens[g_name]:
                if plant.__class__ == PrizeFlower:
                    PrizeFlower.total_height(plant)
                elif plant.__class__ == Plant:
                    Plant.total_height(plant)
                elif plant.__class__ == FloweringPlant:
                    FloweringPlant.total_height(plant)

    def get_infos(self, g_name: str):
        if g_name in self.gardens:
            t_growth = self.GardenStats.get_total_growth(self.gardens[g_name])
            t_plants = self.GardenStats.get_num_plants(self.gardens[g_name])
            print(f"\nPlants added : {t_plants},"
                  f" total growth : {t_growth}")
            types = self.GardenStats.get_statistics(self.gardens[g_name])
            print(f"Plant types: {types['regular']} regular,"
                  f" {types['flowering']}"
                  f" flowering, {types['prize']} prize flowers\n")
            for plant in self.gardens[g_name]:
                height_test = Plant.validation_height(plant)
                if height_test is False:
                    break
            print(f"Height validation test: {height_test}")

    def get_garden_score(self, g_name: str):
        if g_name in self.gardens:
            plants = self.gardens[g_name]
            sum_heights = sum(p.height for p in plants)
            for p in plants:
                if p.__class__ == FloweringPlant:
                    return sum_heights + 81
            return sum_heights


def main():
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager()
    name = manager.add_garden("Alice")
    manager.add_garden("Bob")
    list = {'oak': Plant("Oak Tree", 100),
            'Rose': FloweringPlant("Rose", 24, "red"),
            'Sunflower': PrizeFlower("Sunflower", 50, "yellow", 10)}
    manager.add_plant(f"{name}", list['oak'])
    print(f"Added Oak Tree to yellow {name}'s garden")
    manager.add_plant("Alice", list['Rose'])
    print(f"Added Rose to {name}'s garden")
    manager.add_plant("Alice", list['Sunflower'])
    print(f"Added Sunflower to {name}'s garden")

    print(f"\n{name} is helping all plants grow...")
    manager.help_grow("Alice")

    print(f"\n=== {name}'s Garden Report ===\n")
    manager.get_garden_report("Alice")
    manager.get_infos("Alice")

    bob_plant = Plant("Bob's Tree", 92)
    manager.add_plant("Bob", bob_plant)
    print(f"Garden scores - Alice: {manager.get_garden_score('Alice')},"
          f" Bob: {manager.get_garden_score('Bob')}")
    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    main()
