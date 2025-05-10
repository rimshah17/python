class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger object '{self.name}' created")
    
    def __del__(self):
        print(f"Logger object '{self.name}' destroyed")

# Example usage
if __name__ == "__main__":
    # Create a logger object
    logger1 = Logger("System")
    
    # Create another logger object
    logger2 = Logger("Application")
    
    # Objects will be automatically destroyed when the program ends
    # or when they go out of scope
    print("Program is running...")
    
    # You can also explicitly delete an object
    del logger1
    print("logger1 has been explicitly deleted")
    
    # logger2 will be automatically destroyed when the program ends
