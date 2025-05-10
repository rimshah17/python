from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate area of the shape"""
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of the rectangle"""
        return self.length * self.width

# Create a Rectangle object
rectangle = Rectangle(5, 3)
print(f"Area of rectangle: {rectangle.area()}")  # Output: 15

# Try to create a Shape object (will raise TypeError)
try:
    shape = Shape()
except TypeError as e:
    print(f"Error: {e}")

"""
Explanation:
1. ABC (Abstract Base Class) is imported from the abc module
2. Shape is made abstract by inheriting from ABC
3. area() is marked as abstract using @abstractmethod
4. Rectangle inherits from Shape and must implement area()
5. Cannot instantiate Shape directly as it's abstract
"""
