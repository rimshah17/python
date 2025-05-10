class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable (convention)
        self.__ssn = ssn         # Private variable (name mangling)

# Create an Employee object
emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing public variable - works fine
print("Name:", emp.name)         # Output: John Doe

# Accessing protected variable - works but should be used carefully
print("Salary:", emp._salary)    # Output: 50000

# Accessing private variable - will raise AttributeError
try:
    print("SSN:", emp.__ssn)     # This will fail
except AttributeError as e:
    print("Error accessing private variable:", e)

# Note: Private variables can still be accessed using name mangling
# This is not recommended but possible
print("SSN (using name mangling):", emp._Employee__ssn)  # Output: 123-45-6789

"""
Explanation of access modifiers in Python:

1. Public variables (like 'name'):
   - Can be accessed directly from anywhere
   - No special syntax required
   - Example: emp.name

2. Protected variables (like '_salary'):
   - Conventionally marked with single underscore prefix
   - Can still be accessed directly, but indicates it should be treated as protected
   - Example: emp._salary

3. Private variables (like '__ssn'):
   - Marked with double underscore prefix
   - Python uses name mangling to make it harder to access
   - Direct access (emp.__ssn) will raise AttributeError
   - Can still be accessed using name mangling (emp._Employee__ssn)
   - This is a convention, not a strict enforcement
"""
