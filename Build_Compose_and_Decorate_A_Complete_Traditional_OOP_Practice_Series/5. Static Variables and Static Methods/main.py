class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage
if __name__ == "__main__":
    # Call the static method without creating an instance
    result = MathUtils.add(5, 3)
    print(f"5 + 3 = {result}")
    
    # You can also call it from an instance (though not recommended)
    math = MathUtils()
    result2 = math.add(10, 20)
    print(f"10 + 20 = {result2}")
