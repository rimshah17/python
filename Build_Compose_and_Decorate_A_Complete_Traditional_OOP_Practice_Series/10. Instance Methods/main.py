class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    # Instance method
    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof! Woof!")

# Create two Dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Call the instance method on each object
dog1.bark()  # Output: Buddy the Golden Retriever says: Woof! Woof!
dog2.bark()  # Output: Max the German Shepherd says: Woof! Woof!

"""
Explanation:
1. Instance variables (name and breed) are initialized in __init__
2. Each Dog object has its own copy of these variables
3. The bark() method is an instance method that:
   - Can access instance variables using self
   - Produces different output for each dog
4. Instance methods are called on specific objects
"""
