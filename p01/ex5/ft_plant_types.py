class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


class tree(Plant):
    def __init__(self, name, age, height, diameter):
        Plant.__init__(self, name, age, height)
        self.diameter = diameter
    
    def produce_shade(self):
        print(f"{self.name} (Tree) : {self.height} cm, {self.age} days,"
              f" {self.diameter} cm diameter")
        shade_area = 3.14 * ((20 * self.diameter / 200)**2)
        print(f"Oak provides {shade_area:.0f} square meters of shade\n")


class flower(Plant):
    def __init__(self, name, age, height, color):
        Plant.__init__(self, name, age, height)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} (Flower) : {self.height} cm, {self.age} days,"
              f" {self.color} cm diameter")
        print("Rose is blooming beautifully!\n")


class Vegetable(Plant):
    def __init__(self, name, age, height, harvest_season,  nutritional_value):
        Plant.__init__(self, name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def harvest(self):
        print(f"{self.name} (Vergetebale) : {self.height} cm,{self.age} days,"
              f" {self.harvest_season} harvest")
        print(f"Tomato is rich in vitamin {self.nutritional_value}\n")


def display():
    print("=== Garden Security System ===\n")
    rose = flower("rose", 25, 30, "red")
    rose.bloom()

    oak = tree("Oak", 500, 1825, 50)
    oak.produce_shade()

    tomato = Vegetable("tomato", 80, 10, "summer", "a")
    tomato.harvest()


display()
