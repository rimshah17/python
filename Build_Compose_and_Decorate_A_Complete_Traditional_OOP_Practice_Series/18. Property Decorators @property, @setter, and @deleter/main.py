class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter for price"""
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price with validation"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        print(f"Setting price to {value}...")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

# Create a product
product = Product("Laptop", 999.99)

# Get price using property
print(f"Initial price: ${product.price}")  # Output: Getting price...
                                           #         Initial price: $999.99

# Set price using property
product.price = 899.99                     # Output: Setting price to 899.99...
print(f"New price: ${product.price}")      # Output: Getting price...
                                           #         New price: $899.99

# Try to set negative price
try:
    product.price = -100                   # Output: Setting price to -100...
except ValueError as e:
    print(f"Error: {e}")                   # Output: Error: Price cannot be negative

# Delete price
del product.price                          # Output: Deleting price...

# Try to access deleted price
try:
    print(product.price)
except AttributeError as e:
    print(f"Error: {e}")                   # Output: Error: 'Product' object has no attribute '_price'

"""
Explanation:
1. Property decorators provide a way to:
   - Control access to attributes
   - Add validation
   - Add side effects
   - Maintain encapsulation

2. @property:
   - Defines a getter method
   - Allows attribute-like access
   - Can include validation or computation

3. @price.setter:
   - Defines a setter method
   - Called when assigning to the property
   - Can include validation
   - Can transform the input

4. @price.deleter:
   - Defines a deleter method
   - Called when deleting the property
   - Can include cleanup code
"""
