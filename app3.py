#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
##Assignment-3-Public Variables and Methods
#Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.
class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):        # public method
        print(f"The {self.brand} car is starting...")

# Instantiate the class
my_car = Car("Toyota Corolla")

# Access public variable
print(my_car.brand)

# Call public method
my_car.start()
