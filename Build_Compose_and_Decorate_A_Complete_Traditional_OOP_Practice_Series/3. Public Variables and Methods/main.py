class Car:
    def __init__(self, brand):
        
        self.brand = brand
    
    # Public method
    def start(self):
        print(f"The {self.brand} car has started!")

# Example usage
if __name__ == "__main__":
   
    my_car = Car("Toyota")
    
    # Access the public variable
    print(f"Car brand: {my_car.brand}")
    
    
    my_car.start()
    
   
    my_car.brand = "Honda"
    print(f"New car brand: {my_car.brand}")
    my_car.start()
