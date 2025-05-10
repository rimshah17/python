class Multiplier:
    def __init__(self, factor):
        """Initialize with a multiplication factor"""
        self.factor = factor

    def __call__(self, x):
        """Multiply input by the factor"""
        return x * self.factor

# Create multiplier objects
double = Multiplier(2)
triple = Multiplier(3)

# Check if objects are callable
print(f"Is double callable? {callable(double)}")  # Output: True
print(f"Is triple callable? {callable(triple)}")  # Output: True

# Call objects like functions
print(f"Double of 5: {double(5)}")    # Output: 10
print(f"Triple of 5: {triple(5)}")    # Output: 15

# Use in a list comprehension
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [double(n) for n in numbers]
print(f"Doubled numbers: {doubled_numbers}")  # Output: [2, 4, 6, 8, 10]

# Create a custom multiplier
times_ten = Multiplier(10)
print(f"10 times 7: {times_ten(7)}")  # Output: 70

"""
Explanation:
1. __call__ method allows objects to be called like functions
2. When an object is called, its __call__ method is invoked
3. callable() checks if an object can be called
4. This pattern is useful for:
   - Creating function-like objects
   - Implementing decorators
   - Creating callable classes
   - Maintaining state between calls
"""
