class Plant:
    count = 0

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1

    def creator(self):
        return f"created : {self.name} ({self.height} cm, {self.age} days)"


def main():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    for plant in plants:
        print(plant.creator())
    print(f"\nTotal plants created: {Plant.count}")


if __name__ == "__main__":
    main()
