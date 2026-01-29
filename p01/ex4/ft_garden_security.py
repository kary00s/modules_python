class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def display(self):
        print(f"plant created : {self.name}")
        print(f"hight updated : {self.__height}")
        print(f"age updated : {self.__age}")

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {self.__age}cm [REJECTED]")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: age {self.__height}cm [REJECTED])

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height


p1 = plant("rose", -10, -20)
p1.set_age(p1.get_age())
p1.set_height(p1.get_height())
print(p1.get_age())
p1.display()