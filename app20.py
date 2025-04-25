#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-20-Creating a Custom Exception
#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. 
#Handle it with try...except.

# Define a custom exception class InvalidAgeError
class InvalidAgeError(Exception):
    pass

# Define a function that checks the age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older!")  # Raise custom exception
    else:
        return "Age is valid."

# Test the custom exception with try...except
try:
    age = int(input("Enter your age: "))
    result = check_age(age)  # Call the function
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer for age.")

# Output :
# Enter your age: 18
# Age is valid.

# Enter your age: qw
# Please enter a valid integer for age.

# Enter your age: 15
# Error: Age must be 18 or older!