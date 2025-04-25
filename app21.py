#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-21-Make a Custom Class Iterable
#Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make 
#the object iterable in a for-loop,counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize the starting number
        self.current = start  # The current number to be decremented

    def __iter__(self):
        # The __iter__ method returns the iterator object itself
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop the iteration when the count reaches below 0
        else:
            self.current -= 1  # Decrease the current count
            return self.current + 1  # Return the current count before decrementing

# Using the Countdown class in a for-loop
countdown = Countdown(5)
for number in countdown:
    print(number)

# Output: 
# 5
# 4
# 3
# 2
# 1
# 0