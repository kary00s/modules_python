class plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    sunflower = plant("Sunflower", 30, 20)
    rose = plant("Rose", 80, 45)
    cactus = plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    print(f"{sunflower.name} : {sunflower.height} cm, "
          f"{sunflower.age} days old")
    print(f"{rose.name} : {rose.height} cm, {rose.age} days old")
    print(f"{cactus.name} : {cactus.height} cm, {cactus.age} days old")
