class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold)

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return "hi, my name is " + self.name

some_person = Person("Monica")
print(some_person.greeting())

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor {}".format(self.color, self.flavor)
    
goldengold = Apple("green", "sour")
print(goldengold)