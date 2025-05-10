class InvalidAgeError(Exception):
    """Custom exception for invalid age"""
    def __init__(self, age, message="Age must be at least 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_age(age):
    """Check if age is valid"""
    if age < 18:
        raise InvalidAgeError(age)
    return True

# Test with valid age
try:
    check_age(20)
    print("Age is valid")
except InvalidAgeError as e:
    print(f"Error: {e}")

# Test with invalid age
try:
    check_age(15)
    print("Age is valid")
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: Age must be at least 18
    print(f"Invalid age provided: {e.age}")  # Output: Invalid age provided: 15

# Test with custom message
try:
    age = 16
    if age < 18:
        raise InvalidAgeError(age, "You must be an adult to access this content")
    print("Age is valid")
except InvalidAgeError as e:
    print(f"Error: {e}")  # Output: Error: You must be an adult to access this content

"""
Explanation:
1. Custom exceptions should:
   - Inherit from Exception
   - Have a descriptive name
   - Include relevant information
   - Have a clear error message

2. InvalidAgeError:
   - Stores the invalid age
   - Provides a default message
   - Allows custom messages
   - Inherits from Exception

3. try...except blocks:
   - Catch specific exceptions
   - Handle errors gracefully
   - Provide meaningful feedback
   - Can access exception attributes
"""
