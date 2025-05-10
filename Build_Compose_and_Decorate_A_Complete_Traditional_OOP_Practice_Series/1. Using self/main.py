class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

# Example usage
if __name__ == "__main__":
    # Create a student object
    student1 = Student("John Doe", 85)
    
    # Display student details
    student1.display()
