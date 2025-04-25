#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-5-Static Variables and Static Methods
#Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b  # returns the sum

# Call the static method directly from the class
result = MathUtils.add(10, 5)
print("Sum is:", result)


# Output: Sum is: 15