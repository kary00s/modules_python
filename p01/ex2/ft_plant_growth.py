class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
    
    def age_days(self):
        self.age += 1


def garden_grew(days):
    i = 1
    print(f"=== Day {i} ===")
    print(f"{plant.name} : {plant.height} cm, {plant.age} days old")
    while i < days:
        i += 1
        plant.grow()
        plant.age_days()
    print(f"=== Day {i} ===")
    print(f"{plant.name} : {plant.height} cm, {plant.age} days old")
    print(f"\nGrowth this week: +{i-1}cm")


if __name__ == "__main__":
    plant = plant("werda", 25, 30)
    garden_grew(22)
