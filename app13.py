#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-13-Composition
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car
#class during initialization. Access a method of the Engine class via the Car class.

# Class Engine
class Engine:
    def start(self):
        print("Engine has started.")

# Class Car using composition
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Access Engine's method via Car

# Create an Engine object
my_engine = Engine()

# Pass it to the Car class (composition)
my_car = Car(my_engine)

# Use the Car to start the engine
my_car.start_car()

#Output: 
# Starting the car...
# Engine has started.