class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def display(self):
        print(f"plant created : {self.name}")

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"age updated: age {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: age {self.__age}cm [REJECTED]")

    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: height {self.__height}cm [OK]")
        else:
            print("Invalid operation attempted:"
                  f" height {self.__height}cm [REJECTED]")

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height


plants = {}
plants["Rose"] = SecurePlant("Rose", 25, -30)
plants["Oak"] = SecurePlant("Oak", -200, 365)
plants["Cactus"] = SecurePlant("Cactus", -5, 90)
plants["jasmine"] = SecurePlant("jasmine", -50, 65)

if __name__ == "__main__":
    print("=== Garden Security System ===\n")
    for p in plants.values():
        p.display()
        p.set_age(p.get_age())
        p.set_height(p.get_height())
        print("\n")
