class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    ############ TYPE OF PLANT ##########

class tree(Plant):
    def __init__(self, name, height):
        Plant.__init__(self, name, height)

    def display(self):
        print(f"{self.name} (Tree) : {self.height} cm")

    def grow(self):
        print(f"{self.name} Tree grew 1cm")
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        Plant.__init__(self, name, height)
        self.color = color

    def grow(self):
        print(f"{self.name} flower grew 1cm")
        self.height += 1

    def disp(self):
        print(f"{self.name} (Flower) : {self.height} cm, {self.color} "
              "flowers (blooming) ", end=' ')


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, point):
        FloweringPlant.__init__(self, name, height, color)
        self.point = point
    def display(self):
        self.height += 1
        print(f" Prize points: {point}")


class GardenManager:
    def __init__(self, name):
        self.name = name

    class GardenStats:
        def __init__(self,):
            pass


person = GardenManager("karim")
list_flowers = [
    PrizeFlower("rose", 3, "red", 10 ),
    PrizeFlower("jasmine", 7, "white",10)
    ]

list_trees = [
    tree("Oak", 5),
    tree("Cactus", 8),
    tree("Orange", 4),
    ]

def get_infos():
    print("=== Garden Management System Demo ===")
    for t in list_trees:
        print(f"Added {t.name} Tree to {person.name}'s garden")
    for f in list_flowers:
        print(f"Added {f.name} to {person.name}'s garden")

    print(f"\n{person.name} is helping all plants grow...")

    for t in list_trees:
        t.grow()
    for f in list_flowers:
        f.grow()

    print(f"\n=== {person.name}'s Garden Report ===")
    for f in list_flowers:
        f.disp()
        f.display()
    for t in list_trees:
        t.display()


get_infos()
