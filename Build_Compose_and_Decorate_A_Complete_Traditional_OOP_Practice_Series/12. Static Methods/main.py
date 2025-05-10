class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert temperature from Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert temperature from Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9

# Test the conversion methods
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {fahrenheit_temp:.1f}°F")  # Output: 25°C is 77.0°F

# Convert back to Celsius
converted_back = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp:.1f}°F is {converted_back:.1f}°C")  # Output: 77.0°F is 25.0°C

# Test with freezing point
freezing_c = 0
freezing_f = TemperatureConverter.celsius_to_fahrenheit(freezing_c)
print(f"Water freezes at {freezing_c}°C or {freezing_f:.1f}°F")  # Output: Water freezes at 0°C or 32.0°F

"""
Explanation:
1. @staticmethod decorator marks methods that don't need access to instance or class
2. Static methods can be called on the class without creating an instance
3. They are utility functions that are logically related to the class
4. No self or cls parameter is needed
5. Useful for operations that don't depend on instance or class state
"""
