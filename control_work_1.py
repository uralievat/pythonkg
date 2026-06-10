class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Животное издает звук")

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу!")

dog = Dog("Шарик", 5)
kitty = Cat("Барсик", 2)

dog.make_sound()
kitty.make_sound()

print(dog.get_name())
print(dog.get_age())
print(kitty.get_name())
print(kitty.get_age())

kitty.set_age(2)
print(kitty.get_age())

kitty.set_name("Снежка")
print(kitty.get_name())

dog.set_age(7)
print(dog.get_age())

dog.set_name("Рекс")
print(dog.get_name())