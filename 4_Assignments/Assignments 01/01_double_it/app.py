def get_valid_number():
    """
    Get a valid number from user input.
    Handles both integer and float inputs.
    Returns None if input is invalid.
    """
    try:
        # Get input from user and remove any whitespace
        user_input = input("Please enter a number: ").strip()
        
        # Try converting to float first to handle both integers and decimals
        number = float(user_input)
        
        # If it's a whole number, convert to integer for cleaner output
        if number.is_integer():
            return int(number)
        return number
    
    except ValueError:
        return None

def double_number(number):
    """
    Takes a number and returns its double value
    """
    return number * 2

def format_output(original, doubled):
    """
    Formats the output string based on number type
    """
    # Handle integer vs float formatting
    if isinstance(original, int):
        return f"Double of {original} is {doubled}"
    else:
        return f"Double of {original:.2f} is {doubled:.2f}"

def main():
    """
    Main program loop
    """
    print("Welcome to the Number Doubler! 🔢")
    print("This program will double any number you enter.")
    
    while True:
        # Get number from user
        number = get_valid_number()
        
        # Handle invalid input
        if number is None:
            print("❌ Invalid input! Please enter a valid number.")
            continue
        
        # Double the number and display result
        result = double_number(number)
        print("\n✨ " + format_output(number, result))
        
        # Ask if user wants to continue
        while True:
            continue_choice = input("\nWould you like to double another number? (yes/no): ").lower().strip()
            if continue_choice in ['yes', 'no', 'y', 'n']:
                break
            print("Please enter 'yes' or 'no'")
        
        # Break loop if user doesn't want to continue
        if continue_choice in ['no', 'n']:
            print("\nThank you for using the Number Doubler! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
