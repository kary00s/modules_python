class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height= height

    def display(self)
        print(f"name : ({self.name}) height ({self.height}) age :{self.age} ")

class tree(Plant):
    def __init__(self ,name , age, height, diameter):
        Plant.__init__(self, name, age, height)
        self.diameter = diameter