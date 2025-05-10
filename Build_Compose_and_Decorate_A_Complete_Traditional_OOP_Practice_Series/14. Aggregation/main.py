class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} - {self.position}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store employee references

    def add_employee(self, employee):
        """Add an employee to the department"""
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.name} department")

    def remove_employee(self, employee):
        """Remove an employee from the department"""
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"Removed {employee.name} from {self.name} department")
        else:
            print(f"{employee.name} is not in {self.name} department")

    def list_employees(self):
        """List all employees in the department"""
        print(f"\nEmployees in {self.name} department:")
        for employee in self.employees:
            print(f"- {employee.get_info()}")

# Create employees (they exist independently)
john = Employee("John Smith", "Developer")
sarah = Employee("Sarah Johnson", "Manager")
mike = Employee("Mike Brown", "Designer")

# Create departments
engineering = Department("Engineering")
marketing = Department("Marketing")

# Add employees to departments
engineering.add_employee(john)    # Output: Added John Smith to Engineering department
engineering.add_employee(mike)    # Output: Added Mike Brown to Engineering department
marketing.add_employee(sarah)     # Output: Added Sarah Johnson to Marketing department

# List employees in each department
engineering.list_employees()      # Output: Lists John and Mike
marketing.list_employees()        # Output: Lists Sarah

# Move an employee between departments
engineering.remove_employee(mike) # Output: Removed Mike Brown from Engineering department
marketing.add_employee(mike)      # Output: Added Mike Brown to Marketing department

# List employees again to show the change
engineering.list_employees()      # Output: Lists only John
marketing.list_employees()        # Output: Lists Sarah and Mike

"""
Explanation:
1. Aggregation is a "has-a" relationship where objects can exist independently
2. Employee objects exist independently of Department objects
3. Department stores references to Employee objects
4. Employees can be added to or removed from departments
5. The same employee can be moved between departments
6. This is different from composition where the contained object cannot exist without the container
"""
