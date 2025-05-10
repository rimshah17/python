# Python If Statements

This module covers conditional statements in Python, focusing on how to make decisions in your code using if statements and their variations.

## Overview

Conditional statements are fundamental to programming logic, allowing programs to make decisions and execute different code blocks based on specific conditions.

## Topics Covered

### 1. Basic If Statements
```python
if condition:
    # code to execute if condition is True
```

### 2. If-Else Statements
```python
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
```

### 3. If-Elif-Else Chains
```python
if condition1:
    # code for condition1
elif condition2:
    # code for condition2
else:
    # code if no conditions are True
```

## Comparison Operators
- Equal to (`==`)
- Not equal to (`!=`)
- Greater than (`>`)
- Less than (`<`)
- Greater than or equal to (`>=`)
- Less than or equal to (`<=`)

## Logical Operators
- `and`: Both conditions must be True
- `or`: At least one condition must be True
- `not`: Inverts the boolean value

## Practice Examples

1. **Simple Condition Check**
```python
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

2. **Multiple Conditions**
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

3. **Nested If Statements**
```python
is_weekend = True
is_sunny = True

if is_weekend:
    if is_sunny:
        print("Let's go to the beach!")
    else:
        print("Let's watch a movie at home")
else:
    print("It's a work day")
```

## Best Practices

1. **Clear Conditions**
```python
# Good
if age >= 18:
    print("Adult")

# Avoid
if age >= 18 and age <= 100 and not is_restricted:
    print("Adult")
```

2. **Use Truth Values Directly**
```python
# Good
if is_valid:
    process_data()

# Avoid
if is_valid == True:
    process_data()
```

3. **Proper Indentation**
```python
if condition:
    # Four spaces indentation
    statement1
    statement2
```

## Common Patterns

1. **Input Validation**
```python
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
else:
    print("Invalid input")
```

2. **Multiple Conditions**
```python
if 0 <= score <= 100:  # Chained comparison
    print("Valid score")
```

## Advanced Topics

1. **Conditional Expressions (Ternary Operator)**
```python
result = "Pass" if score >= 60 else "Fail"
```

2. **Using any() and all()**
```python
numbers = [1, 2, 3, 4, 5]
if any(num > 4 for num in numbers):
    print("At least one number is greater than 4")
```

## Common Pitfalls

1. **Assignment vs Comparison**
```python
# Common mistake
if x = 5:  # This is assignment
    print("Error")

# Correct
if x == 5:  # This is comparison
    print("Correct")
```

2. **Mutable Objects in Conditions**
```python
# Be careful with empty lists
empty_list = []
if empty_list:  # This will be False
    print("List has items")
```

## Exercises

1. Create a program that checks if a number is positive, negative, or zero
2. Implement a simple calculator with if statements
3. Create a grade calculator using if-elif-else
4. Write a program to check if a year is a leap year

## Additional Resources

- [Python Official Documentation on Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- Practice exercises in the project files
- Interactive Python console for experimentation

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating your feature branch
3. Committing your changes
4. Pushing to the branch
5. Creating a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
