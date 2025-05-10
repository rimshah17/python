# Traditional OOP Practice Series

This repository contains a series of Python examples demonstrating various Object-Oriented Programming (OOP) concepts and patterns.

## Table of Contents

1. [Access Modifiers](#access-modifiers)
2. [The super() Function](#the-super-function)
3. [Abstract Classes and Methods](#abstract-classes-and-methods)
4. [Instance Methods](#instance-methods)
5. [Class Methods](#class-methods)
6. [Static Methods](#static-methods)
7. [Composition](#composition)
8. [Aggregation](#aggregation)
9. [Method Resolution Order (MRO)](#method-resolution-order-mro)
10. [Function Decorators](#function-decorators)
11. [Class Decorators](#class-decorators)
12. [Property Decorators](#property-decorators)
13. [callable() and __call__()](#callable-and-__call__)
14. [Custom Exceptions](#custom-exceptions)
15. [Custom Iterators](#custom-iterators)

## Access Modifiers

Demonstrates public, protected, and private access modifiers in Python:
- Public variables (no prefix)
- Protected variables (single underscore prefix)
- Private variables (double underscore prefix)

## The super() Function

Shows how to use `super()` to call parent class methods:
- Inheritance hierarchy
- Method overriding
- Parent class initialization

## Abstract Classes and Methods

Implements abstract base classes using the `abc` module:
- Abstract methods
- Interface definition
- Concrete class implementation

## Instance Methods

Demonstrates instance methods and variables:
- Instance-specific data
- Method access to instance variables
- Object state management

## Class Methods

Shows class methods and class variables:
- `@classmethod` decorator
- Class-level data
- Alternative constructors

## Static Methods

Implements static methods:
- `@staticmethod` decorator
- Utility functions
- No instance or class access

## Composition

Demonstrates composition ("has-a" relationship):
- Object containment
- Component reuse
- Strong ownership

## Aggregation

Shows aggregation (weaker "has-a" relationship):
- Object references
- Independent existence
- Flexible relationships

## Method Resolution Order (MRO)

Explains Python's method resolution order:
- Multiple inheritance
- Diamond problem
- `__mro__` attribute

## Function Decorators

Implements function decorators:
- Function modification
- Cross-cutting concerns
- `@decorator` syntax

## Class Decorators

Shows class decorators:
- Class modification
- Method addition
- Class-level functionality

## Property Decorators

Demonstrates property decorators:
- `@property`
- `@setter`
- `@deleter`
- Attribute access control

## callable() and __call__()

Implements callable objects:
- `__call__` method
- Function-like objects
- State maintenance

## Custom Exceptions

Shows custom exception creation:
- Exception inheritance
- Error handling
- Custom error messages

## Custom Iterators

Demonstrates iterator protocol:
- `__iter__` method
- `__next__` method
- `StopIteration` exception

## Usage

Each concept is demonstrated in its own Python file with:
- Clear examples
- Detailed comments
- Expected output
- Explanation of the concept

## Requirements

- Python 3.x
- No external dependencies

## License

This project is open source and available under the MIT License. 