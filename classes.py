#  super().__init__()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('Move')

    def draw(self):
        print('Draw')


point1 = Point(10, 30)
point1.x = 10
point1.y = 30

point1.draw()
print(point1.x)


class Person:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def talk(self):
        print("talk")


john = Person("John Smith")
print(john.name)
print(john.talk())


# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
