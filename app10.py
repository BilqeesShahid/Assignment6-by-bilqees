#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-10-Instance Methods
#Create a class Dog with instance variables name and breed. Add an instance method bark() 
#that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name        # Instance variable
        self.breed = breed      # Instance variable

    def bark(self):             # Instance method
        print(f"{self.name} says: Woof! Woof!")

# Creating an object of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Calling the instance method
my_dog.bark()
