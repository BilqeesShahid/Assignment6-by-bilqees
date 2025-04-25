#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-16-Function Decorators
#Write a decorator function log_function_call that prints "Function is being called" 
#before a function executes. Apply it to a function say_hello().

# Function Decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Function to be decorated(Inside the decorator function it calls the original function.)
@log_function_call
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

#Output:
# Function is being called
# Hello!
