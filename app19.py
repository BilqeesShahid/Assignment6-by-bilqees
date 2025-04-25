#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-19-callable() and __call__()
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method 
#that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor
    
    def __call__(self, x):
        return x * self.factor  # Multiply the input by the factor

# Create an instance of the Multiplier class with a factor of 5
multiply_by_5 = Multiplier(5)

# Use callable() to check if the object is callable
print(callable(multiply_by_5))  # Output: True

# Call the object like a function
result = multiply_by_5(10)  # This will invoke __call__()
print(f"Result of calling the object: {result}")  # Output: 50
