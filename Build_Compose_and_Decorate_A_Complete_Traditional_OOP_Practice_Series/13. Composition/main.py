class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"Engine started with {self.horsepower} horsepower")

    def stop(self):
        self.is_running = False
        print("Engine stopped")

    def get_status(self):
        return "running" if self.is_running else "stopped"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        print(f"Starting {self.make} {self.model}")
        self.engine.start()

    def stop(self):
        print(f"Stopping {self.make} {self.model}")
        self.engine.stop()

    def get_engine_status(self):
        return f"Engine is {self.engine.get_status()}"

# Create an engine
v8_engine = Engine(horsepower=300)

# Create a car with the engine
mustang = Car("Ford", "Mustang", v8_engine)

# Use the car's methods which delegate to the engine
mustang.start()  # Output: Starting Ford Mustang
                 #         Engine started with 300 horsepower

# Check engine status through the car
print(mustang.get_engine_status())  # Output: Engine is running

# Stop the car
mustang.stop()  # Output: Stopping Ford Mustang
                #         Engine stopped

print(mustang.get_engine_status())  # Output: Engine is stopped

"""
Explanation:
1. Composition is a "has-a" relationship
2. Car has an Engine (Car contains an Engine object)
3. Car delegates engine-related operations to its Engine object
4. Engine can exist independently of Car
5. This is different from inheritance which is an "is-a" relationship
"""
