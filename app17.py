#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-17-Class Decorators
#Create a class decorator add_greeting that modifies a class to add a greet() method
#returning "Hello from Decorator!". Apply it to a class Person.

# Class Decorator
def add_greeting(cls):
    # Add a new method greet to the class
    def greet(self):
        return "Hello from Decorator!"
    
    # Add greet to the class
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_name(self):
        return f"My name is {self.name}"

# Create an object of Person
person = Person("Bilqees")

# Call methods on the person object
print(person.say_name())  # Existing method
print(person.greet())     # New method added by the decorator

#Output
# My name is Bilqees
# Hello from Decorator!