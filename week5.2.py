# Base class: Animal
class Animal:
    def move(self):
        pass  # Base move method is empty; will be overridden in subclasses

# Subclass: Dog
class Dog(Animal):
    def move(self):
        print("Running 🐕")

# Subclass: Cat
class Cat(Animal):
    def move(self):
        print("Jumping 🐈")

# Subclass: Fish
class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

# Polymorphism in action
animals = [Dog(), Cat(), Fish()]

for animal in animals:
    animal.move()  # The move() method behaves differently based on the object type
