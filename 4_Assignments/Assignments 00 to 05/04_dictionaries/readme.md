# Python Dictionaries - Code Examples

## Basic Dictionary Operations
```python
# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: John
print(person.get("age"))  # Output: 30

# Adding/Updating items
person["email"] = "john@example.com"
person["age"] = 31

# Removing items
del person["city"]
email = person.pop("email")
last_item = person.popitem()  # Removes last item
```

## Dictionary Methods
```python
# Dictionary methods
student = {
    "id": "001",
    "name": "Alice",
    "grades": {"math": 90, "science": 85}
}

# Get all keys
keys = student.keys()  # dict_keys(['id', 'name', 'grades'])

# Get all values
values = student.values()  # dict_values(['001', 'Alice', {...}])

# Get key-value pairs
items = student.items()  # dict_items([('id', '001'), ('name', 'Alice'), ...])

# Clear dictionary
student.clear()  # {}
```

## Dictionary Comprehension
```python
# Create dictionary using comprehension
squares = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering with comprehension
even_squares = {x: x**2 for x in range(5) if x % 2 == 0}
# Output: {0: 0, 2: 4, 4: 16}
```

## Nested Dictionaries
```python
# Working with nested dictionaries
school = {
    "class_a": {
        "teacher": "Mrs. Smith",
        "students": {
            "1": {"name": "John", "grade": "A"},
            "2": {"name": "Emma", "grade": "B"}
        }
    },
    "class_b": {
        "teacher": "Mr. Brown",
        "students": {
            "1": {"name": "Alex", "grade": "B"},
            "2": {"name": "Sarah", "grade": "A"}
        }
    }
}

# Accessing nested values
print(school["class_a"]["students"]["1"]["grade"])  # Output: A
```

## Dictionary Merging
```python
# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update method
dict1.update(dict2)

# Using | operator (Python 3.9+)
merged = dict1 | dict2

# Merging with overlapping keys
dict3 = {"a": 10, "d": 40}
merged = dict1 | dict3  # dict3 values override dict1
```

## Default Values
```python
# Using setdefault
contacts = {}
contacts.setdefault("John", []).append("123-456-7890")
contacts.setdefault("John", []).append("john@example.com")

# Using defaultdict
from collections import defaultdict
grades = defaultdict(list)
grades["Math"].append(90)  # No need to check if "Math" exists
```

## Dictionary Type Hints (Python 3.9+)
```python
from typing import Dict, Union

# Type hints for dictionaries
prices: dict[str, float] = {
    "apple": 0.50,
    "banana": 0.75,
    "orange": 0.60
}

# Complex type hints
user_data: dict[str, Union[str, int, list[str]]] = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "swimming"]
}
```
```

This README focuses on practical code examples for working with Python dictionaries, including:
- Basic operations
- Dictionary methods
- Dictionary comprehension
- Nested dictionaries
- Dictionary merging
- Default values
- Type hints for dictionaries


