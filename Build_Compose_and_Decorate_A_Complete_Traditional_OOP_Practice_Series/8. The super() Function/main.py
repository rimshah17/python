class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for {name}")

    def introduce(self):
        print(f"Hello, I am {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        # Call the parent class constructor using super()
        super().__init__(name)
        self.subject = subject
        print(f"Teacher constructor called for {name} teaching {subject}")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

# Create a Person object
person = Person("John")
person.introduce()

# Create a Teacher object
teacher = Teacher("Sarah", "Mathematics")
teacher.introduce()  # Inherited from Person
teacher.teach()     # Specific to Teacher

"""
Output will be:
Person constructor called for John
Hello, I am John
Person constructor called for Sarah
Teacher constructor called for Sarah teaching Mathematics
Hello, I am Sarah
Sarah is teaching Mathematics
"""
