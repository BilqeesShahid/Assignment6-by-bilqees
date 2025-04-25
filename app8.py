#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-8-The super() Function
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, 
#add a subject field, and use super() to call the base class constructor.

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)       # Calls the constructor of Person
        self.subject = subject

    def display(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

t1 = Teacher("Miss Sara", "Mathematics")
t1.display()
