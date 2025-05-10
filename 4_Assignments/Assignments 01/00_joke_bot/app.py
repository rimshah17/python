import random

# List of jokes stored as dictionaries with setup and punchline
jokes = [
    {
        "setup": "Why did the programmer quit his job?",
        "punchline": "Because he didn't get arrays (a raise)!"
    },
    {
        "setup": "What's a computer's favorite snack?",
        "punchline": "Microchips!"
    },
    {
        "setup": "Why do programmers always mix up Halloween and Christmas?",
        "punchline": "Because Oct 31 equals Dec 25!"
    },
    {
        "setup": "How many programmers does it take to change a light bulb?",
        "punchline": "None, that's a hardware problem!"
    },
    {
        "setup": "What do you call a bear that codes?",
        "punchline": "A pandas developer!"
    },
    {
        "setup": "Why do Python programmers wear glasses?",
        "punchline": "Because they can't C#!"
    },
    {
        "setup": "What's a programmer's favorite place in the house?",
        "punchline": "The living ROM!"
    },
    {
        "setup": "What did the Java code say to the C code?",
        "punchline": "You've got no class!"
    },
    {
        "setup": "Why did the database administrator leave his wife?",
        "punchline": "Because she had too many relationships!"
    },
    {
        "setup": "What did the HTML say to the CSS?",
        "punchline": "You make me look good!"
    }
]

def get_random_joke():
    """Return a random joke from the jokes list"""
    return random.choice(jokes)

def tell_joke():
    """Tell a joke with a pause between setup and punchline"""
    joke = get_random_joke()
    print("\nHere's a joke for you:")
    print(joke["setup"])
    input("Press Enter to hear the punchline...")
    print(joke["punchline"])
    print()

def main():
    """Main function to run the joke bot"""
    print("Welcome to ProgrammerJokeBot! 🤖")
    print("I specialize in programming and tech humor!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Hear a programming joke")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            tell_joke()
            response = input("Would you like to hear another joke? (yes/no): ").lower().strip()
            if response not in ["yes", "y"]:
                print("\nThanks for debugging my jokes! Keep coding! 👨‍💻")
                break
        elif choice == "2":
            print("\nGoodbye! Remember to always git-commit to laughing! 👋")
            break
        else:
            print("\nError 404: Valid choice not found. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
