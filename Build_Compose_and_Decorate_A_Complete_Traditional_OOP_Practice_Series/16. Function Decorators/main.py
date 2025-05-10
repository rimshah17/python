def log_function_call(func):
    """Decorator that logs when a function is called"""
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    """Function that greets a person"""
    print(f"Hello, {name}!")

# Call the decorated function
say_hello("Alice")  # Output: Function is being called
                    #         Hello, Alice!

# Call with different arguments
say_hello("Bob")    # Output: Function is being called
                    #         Hello, Bob!

"""
Explanation:
1. log_function_call is a decorator function that:
   - Takes a function as an argument
   - Returns a wrapper function
   - The wrapper function:
     * Prints a message
     * Calls the original function
     * Returns the result

2. @log_function_call is syntactic sugar for:
   say_hello = log_function_call(say_hello)

3. The decorator preserves the original function's:
   - Arguments (*args, **kwargs)
   - Return value
   - Functionality

4. Decorators are useful for:
   - Logging
   - Timing
   - Authentication
   - Caching
   - And more!
"""
