class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):
    pass

# Create an object of D
d = D()

# Call show() and observe which version is called
d.show()  # Output: B's show() method

# Print the Method Resolution Order
print("\nMethod Resolution Order (MRO):")
for i, cls in enumerate(D.__mro__):
    print(f"{i+1}. {cls.__name__}")

"""
Explanation:
1. Diamond inheritance structure:
       A
      / \
     B   C
      \ /
       D

2. MRO determines the order in which methods are searched:
   - D -> B -> C -> A
   - This is why B's show() is called instead of C's

3. MRO follows these rules:
   - Subclasses come before base classes
   - Base class order is preserved
   - The first occurrence of a class is used

4. You can check MRO using:
   - D.__mro__
   - D.mro()
   - help(D)
"""
