class Plant:
    count = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1

    def __str__(self):
        return f"created : {self.name} ({self.height} cm, {self.age} days)"


plants = {}

plants["Rose"] = Plant("Rose", 25, 30)
plants["Oak"] = Plant("Oak", 200, 365)
plants["Cactus"] = Plant("Cactus", 5, 90)
plants["jasmine"] = Plant("jasmine", 50, 65)
plants["loren"] = Plant("loren", 5, 90)

for p in plants.values():
    print(p)

print(f"\nTotal plants created: {Plant.count}")
