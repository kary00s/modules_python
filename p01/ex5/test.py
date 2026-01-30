class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


class tree(Plant):
    def __init__(self, name, age, height, diameter, shade):
        Plant.__init__(self, name, age, height)
        self.diameter = diameter
        self.shade = shade
    
    def produce_shade(self):
        print(f"{self.name} (Tree) : {self.height} cm, {self.age} days, {self.diameter} cm diameter")
        print(f"Oak provides {self.shade} square meters of shade")


class flower(Plant):
    def __init__(self, name, age, height, color):
        Plant.__init__(self, name, age, height)
        self.color = color
    
    def bloom(self):
        print(f"{self.name} (Flower) : {self.height} cm, {self.age} days, {self.color} cm diameter")
        print("Rose is blooming beautifully!")


class Vegetable(Plant):
    def __init__(self, name, age, harvest_season,  nutritional_value):
        Plant.__init__(self, name, age, None)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def harvest(self):
        print(f"{self.name} (Vergetebale) : {self.height} cm, {self.age} days,"
              f"{self.harvest_season} cm diameter")
        print(f"Tomato is rich in vitamin {self.nutritional_value}")
def display():
    