class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("the age cant be negative")

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("the height cant be negative")

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height
    