# Base class: Superhero
class Superhero:
    def __init__(self, name, power, age):
        self.name = name
        self.power = power
        self.age = age
    
    def save_the_day(self):
        print(f"{self.name} is saving the day with {self.power}!")

    def display_info(self):
        print(f"Superhero: {self.name}")
        print(f"Power: {self.power}")
        print(f"Age: {self.age}")

# Subclass: FlyingSuperhero (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, age, flight_speed):
        super().__init__(name, power, age)  # Call the parent class constructor
        self.flight_speed = flight_speed

    def save_the_day(self):
        print(f"{self.name} is flying at {self.flight_speed} mph to save the day!")

# Subclass: StrengthSuperhero (inherits from Superhero)
class StrengthSuperhero(Superhero):
    def __init__(self, name, power, age, strength_level):
        super().__init__(name, power, age)
        self.strength_level = strength_level

    def save_the_day(self):
        print(f"{self.name} is using their super strength to lift cars and save the day!")

# Creating instances
hero1 = Superhero("Wonder Woman", "Combat Skills", 30)
hero2 = FlyingSuperhero("Superman", "Super Strength", 35, 900)
hero3 = StrengthSuperhero("Hulk", "Super Strength", 40, "Extreme")

# Calling methods
hero1.display_info()
hero1.save_the_day()

hero2.display_info()
hero2.save_the_day()

hero3.display_info()
hero3.save_the_day()
