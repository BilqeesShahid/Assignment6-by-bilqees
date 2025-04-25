#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
##Assignment-2-Using cls
#Create a class Counter that keeps track of how many objects have been created.
#Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0  # class variable to track number of objects

    def __init__(self):
        Counter.count += 1  # increment when a new object is created

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()  # Output: Total objects created: 3

