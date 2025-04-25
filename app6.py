#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-6-Constructors and Destructors
#Create a class Logger that prints a message when an object is created (constructor) and 
# another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created!")  # Constructor message

    def __del__(self):
        print("Logger object destroyed!")  # Destructor message
        
        
log1 = Logger()

 

 
