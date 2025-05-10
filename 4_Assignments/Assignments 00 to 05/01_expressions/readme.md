# Python Expressions

This module covers Python expressions, their evaluation, and how they form the building blocks of Python programs.

## Overview

Expressions are combinations of values, variables, operators, and function calls that can be evaluated to produce a result. Understanding expressions is fundamental to Python programming.

## Topics Covered

### 1. Basic Expression Types
- Arithmetic expressions
- String expressions
- Boolean expressions
- Comparison expressions
- Assignment expressions

### 2. Operators
- **Arithmetic Operators**
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
  - Floor Division (//)
  - Modulus (%)
  - Exponentiation (**)

- **Comparison Operators**
  - Equal to (==)
  - Not equal to (!=)
  - Greater than (>)
  - Less than (<)
  - Greater than or equal to (>=)
  - Less than or equal to (<=)

- **Logical Operators**
  - and
  - or
  - not

### 3. Expression Evaluation
- Order of operations
- Operator precedence
- Left-to-right evaluation
- Expression grouping with parentheses

## Code Examples

```python
# Arithmetic Expressions
result = 5 + 3 * 2  # Result: 11 (multiplication before addition)
result = (5 + 3) * 2  # Result: 16 (parentheses change precedence)

# String Expressions
greeting = "Hello" + " " + "World"  # String concatenation
repeated = "Python" * 3  # String repetition

# Boolean Expressions
is_valid = True and False  # Logical AND
is_true = not False  # Logical NOT
```

## Practice Exercises

1. **Basic Arithmetic**
   - Create expressions using different arithmetic operators
   - Understand operator precedence
   - Use parentheses to modify evaluation order

2. **String Operations**
   - Practice string concatenation
   - Experiment with string multiplication
   - Combine strings and numbers using conversion

3. **Boolean Logic**
   - Create complex boolean expressions
   - Use comparison operators
   - Combine logical operators

## Common Gotchas

1. Division returns a float in Python 3.x
2. Integer division truncates toward negative infinity
3. Mixing numeric types can affect results
4. String concatenation only works with strings, not other types without conversion

## Best Practices

1. Use parentheses to make complex expressions clear
2. Break long expressions into smaller parts
3. Use meaningful variable names
4. Consider readability when writing complex expressions

## Additional Resources

- [Python Official Documentation on Expressions](https://docs.python.org/3/reference/expressions.html)
- Practice problems in the project files
- Interactive Python console for experimentation

## Contributing

Contributions to improve the examples, exercises, or documentation are welcome:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
