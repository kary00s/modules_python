class SecurePlant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        self.__height = height
        self.__age = age

    def display(self):
        if self.set_height() is True:
            print(f"plant created : {self.name}")
            height = self.get_height()
            print(f"Height updated: height {height}cm [OK]")
            self.set_age()

    def set_age(self):
        if self.get_age() >= 0:
            age = self.get_age()
            print(f"age updated: age {age}cm [OK]")
        else:
            print("Invalid operation attempted:"
                  f"age {age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def set_height(self):
        height = self.get_height()
        if self.get_height() >= 0:
            return True
        else:
            print("\nInvalid operation attempted:"
                  f" height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return False

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height


def main():
    plant1 = SecurePlant("rose", 30, 25)
    plant2 = SecurePlant("Sunflower", -5, -5)
    print("=== Garden Security System ===\n")
    plant1.display()
    plant2.display()
    print("\nCurrent plant: Rose"
          f"({plant1.get_height()}cm, {plant1.get_age()} days)")


if __name__ == "__main__":
    main()
