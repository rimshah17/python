# Python Loops and Control Flow - Code Examples

## For Loops
```python
# Basic for loop
for i in range(5):
    print(i)  # Outputs: 0, 1, 2, 3, 4

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Range with start, stop, step
for i in range(2, 10, 2):
    print(i)  # Outputs: 2, 4, 6, 8
```

## While Loops
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with break
number = 0
while True:
    if number >= 5:
        break
    print(number)
    number += 1

# While loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)  # Skips printing 3
```

## Nested Loops
```python
# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Pattern printing
for i in range(5):
    print('*' * i)
```

## Loop Control Statements
```python
# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)  # Stops at 4

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)  # Skips 2

# Pass statement
for i in range(3):
    if i == 1:
        pass  # Do nothing
    else:
        print(i)
```

## List Comprehension with Loops
```python
# Simple list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Conditional list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

## Iterating Over Different Data Structures
```python
# Dictionary iteration
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")

# Items method
for key, value in person.items():
    print(f"{key}: {value}")

# Set iteration
colors = {"red", "green", "blue"}
for color in colors:
    print(color)
```

## Loop with else Clause
```python
# Loop with else
for i in range(5):
    if i == 10:
        break
    print(i)
else:
    print("Loop completed successfully")

# While with else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed")
```

## Infinite Loops with Control
```python
# Controlled infinite loop
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break

# With user input
while True:
    response = input("Continue? (y/n): ")
    if response.lower() != 'y':
        break
```

## Loop with Exception Handling
```python
# Safe loop with try-except
numbers = [1, 2, 0, 4, 5]
for num in numbers:
    try:
        result = 10 / num
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
        continue
```

This README provides practical code examples for:
- For and while loops
- Nested loops
- Loop control statements
- List comprehensions
- Iterating over different data structures
- Loop with else clause
- Infinite loops
- Exception handling in loops

Each example demonstrates a specific aspect of Python loops and control flow with clear, executable code.
