#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-1-Using self
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values
# via a constructor. Add a method display() that prints student details.
class Student:
    def __init__(self, name, marks):
        self.name = name       # using self to set the instance variable 'name'
        self.marks = marks     # using self to set the instance variable 'marks'

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")


student1 = Student("Ahmed", 24)
student1.display()



