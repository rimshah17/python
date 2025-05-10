def add_greeting(cls):
    """Class decorator that adds a greet method"""
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

# Create a Person object
person = Person("Alice")

# Call the original method
print(person.introduce())  # Output: My name is Alice

# Call the added method
print(person.greet())      # Output: Hello from Decorator!

"""
Explanation:
1. add_greeting is a class decorator that:
   - Takes a class as an argument
   - Defines a new method greet()
   - Adds the method to the class
   - Returns the modified class

2. @add_greeting is syntactic sugar for:
   Person = add_greeting(Person)

3. The decorator:
   - Modifies the class at definition time
   - Adds new functionality without inheritance
   - Preserves existing class methods
   - Works with any instance of the class

4. Class decorators are useful for:
   - Adding methods
   - Modifying class attributes
   - Implementing mixins
   - Adding class-level functionality
"""
