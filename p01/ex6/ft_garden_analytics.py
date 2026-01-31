class Plant:
    def __init__(self, name, height):
        self.name = name 
        self.height = height
    def grow(self):
        self.height += 1

    ############ TYPE OF PLANT ##########


class tree(Plant):
    def __init__(self, name, height):
        Plant.__init__(self, name, height)

    def display(self):
        print(f"{self.name} (Tree) : {self.height} cm,")

    def grow(self):
        print(f"{self.name} Tree grew 1cm")
        self.height += 1


class flower(Plant):
    def __init__(self, name, height, color):
        Plant.__init__(self, name, height)
        self.color = color

    def grow(self):
        print(f"{self.name} flower grew 1cm")
        self.height += 1

    def display(self):
        print(f"{self.name} (Flower) : {self.height} cm, {self.color} "
              "flowers (blooming) ")

    #######################################


class FloweringPlant(Plant):
    def __init__(self, name, age, height, color):
        Plant.__init__(self, name, age, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, point):
        FloweringPlant.__init__(self, name, height, color)
        self.point = point


class GardenManager:
    def __init__(self, name):
        self.name = name

    class GardenStats:
        def __init__(self,):
            pass


flower = flower("jasmine", 3, "red")
tree = tree("Oak", 5)
person = GardenManager("karim")


def get_infos():
    print("=== Garden Management System Demo ===")
    print(f"Added {tree.name} Tree to {person.name}'s garden")
    print(f"Added {flower.name} to {person.name}'s garden\n")
    print(f"{person.name} is helping all plants grow...")
    tree.grow()
    flower.grow()


get_infos()
