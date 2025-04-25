#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-18-Property Decorators: @property, @setter, and @deleter
#Create a class Product with a private attribute _price. Use @property to get the price, 
#@price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    # @property decorator for getting the price
    @property
    def price(self):
        return self._price

    # @price.setter decorator for updating the price
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Price cannot be negative!")
        else:
            self._price = new_price

    # @price.deleter decorator for deleting the price
    @price.deleter
    def price(self):
        print("Price deleted!")
        del self._price

# Create a Product object
product = Product("Laptop", 1000)

# Access the price using the @property method
print(f"Initial Price Of Laptop: ${product.price}")

# Update the price using the @price.setter method
product.price = 1200
print(f"Updated Price Of Laptop: ${product.price}")

# Attempt to set a negative price
product.price = -500  # This will trigger the validation in the setter

# Delete the price using the @price.deleter method
del product.price

# Output:
# Initial Price Of Laptop: $1000
# Updated Price Of Laptop: $1200
# Price cannot be negative!     
# Price deleted!
