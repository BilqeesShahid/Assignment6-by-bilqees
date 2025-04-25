#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-12-Static Methods
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
#that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Using the static method without creating an object
temp_celsius = 25
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")   # output: 25°C is equal to 77.0°F

 