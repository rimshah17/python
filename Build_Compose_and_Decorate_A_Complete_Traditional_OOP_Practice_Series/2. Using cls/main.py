class Counter:
    # Class variable to keep track of the number of objects
    count = 0
    
    def __init__(self):
        # Increment the count each time a new object is created
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def display_count(cls):
        print(f"Total number of Counter objects created: {cls.count}")

# Example usage
if __name__ == "__main__":
    # Create some Counter objects
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    
    # Display the count using the class method
    Counter.display_count()
    
    # Get the count using the get_count method
    print(f"Count retrieved using get_count(): {Counter.get_count()}")
