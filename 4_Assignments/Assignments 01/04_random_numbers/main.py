import random

def get_random_number(start, end):
    """Generate a random number between start and end"""
    return random.randint(start, end)

def get_random_float(start, end):
    """Generate a random float between start and end"""
    return random.uniform(start, end)

def flip_coin():
    """Simulate a coin flip"""
    return "Heads" if random.random() < 0.5 else "Tails"

def roll_dice(sides=6):
    """Roll a dice with specified number of sides"""
    return random.randint(1, sides)

def main():
    print("Welcome to Random Number Generator!")
    
    while True:
        print("\nChoose an option:")
        print("1. Generate a random integer")
        print("2. Generate a random float")
        print("5. Flip a coin")
        print("6. Roll a dice")
        
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            
            if choice == 1:
                # Get range from user
                print("\nLet's generate a random integer!")
                start = int(input("Enter the starting number: "))
                end = int(input("Enter the ending number: "))
                
                # Validate input
                if start >= end:
                    print("Starting number must be less than ending number!")
                    continue
                
                # Generate and display random number
                result = get_random_number(start, end)
                print(f"\nRandom number between {start} and {end} is: {result}")
                
            elif choice == 2:
                # Get range for float
                print("\nLet's generate a random float!")
                start = float(input("Enter the starting number: "))
                end = float(input("Enter the ending number: "))
                
                # Validate input
                if start >= end:
                    print("Starting number must be less than ending number!")
                    continue
                
                # Generate and display random float
                result = get_random_float(start, end)
                print(f"\nRandom float between {start} and {end} is: {result:.4f}")
                
            elif choice == 5:
                # Flip a coin
                result = flip_coin()
                print(f"\nCoin flip result: {result}")
                
            elif choice == 6:
                # Roll a dice
                sides = int(input("\nEnter number of sides for the dice (default is 6): ") or "6")
                if sides <= 0:
                    print("Number of sides must be positive!")
                    continue
                
                result = roll_dice(sides)
                print(f"\nDice roll result ({sides}-sided): {result}")
                
            else:
                print("Invalid choice! Please select a valid option.")
                continue
            
            # Ask to continue
            again = input("\nGenerate another random result? (yes/no): ").lower()
            if again != 'yes' and again != 'y':
                print("Thank you for using Random Number Generator!")
                break
                
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()
