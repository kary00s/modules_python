class SecurePlant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.__height = height
        self.__age = age

    def display(self):
        print(f"plant created : {self.name}")
        self.set_age()
        self.set_height()
        print(f"Current plant: Rose ({self.__age}cm, 30 days)")

    def set_age(self):
        if self.get_age() >= 0:
            self.__age = self.get_age()
            print(f"age updated: age {self.__age}cm [OK]\n")
        else:
            print("Invalid operation attempted:"
                  f"age {self.__age}cm [REJECTED]")
            print("Security: Negative age rejected\n")

    def set_height(self):
        if self.get_height() >= 0:
            self.__height = self.get_height()
            print(f"Height updated: height {self.__height}cm [OK]\n")
        else:
            print("Invalid operation attempted:"
                  f" height {self.__height}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height


if __name__ == "__main__":
    p = SecurePlant("jasmine", -10, 1)
    print("=== Garden Security System ===\n")
    p.display()
    print("\n")
