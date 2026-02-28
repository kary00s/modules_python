class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.age = age
        self.height = height


class tree(Plant):
    def __init__(self: str, name: str, age: int, height: int, diameter: int):
        super().__init__(name, age, height)
        self.diameter = diameter

    def produce_shade(self):
        print(
            f"{self.name} (Tree) : {self.height} cm, {self.age} days,"
            f" {self.diameter} cm diameter"
        )
        shade_area = 3.14 * ((20 * self.diameter / 200) ** 2)
        print(f"Oak provides {shade_area:.0f} square meters of shade\n")


class flower(Plant):
    def __init__(self, name: str, age: int, height: int, color: str):
        super().__init__(name, age, height)
        self.color = color

    def bloom(self):
        print(
            f"{self.name} (Flower) : {self.height} cm, {self.age} days,"
            f" {self.color} color"
        )
        print("Rose is blooming beautifully!\n")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: int,
        harvest_season: str,
        nutritional_value: str,
    ):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self):
        print(
            f"{self.name} (Vergetebale) : {self.height} cm,{self.age} days,"
            f" {self.harvest_season} harvest"
        )
        print(f"Tomato is rich in vitamin {self.nutritional_value}\n")


def main():
    print("=== Garden Security System ===\n")
    rose = flower("Rose", 30, 25, "red")
    rose.bloom()

    oak = tree("Oak", 1825, 500, 50)
    oak.produce_shade()

    tomato = Vegetable("Tomato", 10, 80, "summer", "C")
    tomato.harvest()


if __name__ == "__main__":
    main()
