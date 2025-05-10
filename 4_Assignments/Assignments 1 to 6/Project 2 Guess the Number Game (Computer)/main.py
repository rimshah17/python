class ComputerGuesser:
    def __init__(self):
        self.min_number = 1
        self.max_number = 100
        self.guesses = 0
        
    def reset(self):
        """Reset the game state"""
        self.guesses = 0
        
    def make_guess(self):
        """Make a guess using binary search"""
        return (self.min_number + self.max_number) // 2
        
    def update_range(self, feedback):
        """Update the search range based on user feedback"""
        current_guess = self.make_guess()
        if feedback in ['higher', 'h']:
            self.min_number = current_guess + 1
        elif feedback in ['lower', 'l']:
            self.max_number = current_guess - 1
            
    def play(self):
        """Main game loop"""
        print("\n🤖 Welcome to Number Guessing Game - Computer Edition!")
        print(f"Think of a number between {self.min_number} and {self.max_number}")
        print("\nQuick commands:")
        print("- 'h' or 'higher' for higher")
        print("- 'l' or 'lower' for lower")
        print("- 'c' or 'correct' for correct")
        input("\nPress Enter when you're ready...")
        
        while True:
            self.guesses += 1
            current_guess = self.make_guess()
            
            print(f"\n🤔 My guess is: {current_guess}")
            
            while True:
                feedback = input("Is this correct, higher, or lower? (c/h/l): ").lower().strip()
                if feedback in ['correct', 'c', 'higher', 'h', 'lower', 'l']:
                    break
                print("❌ Please enter 'c' (correct), 'h' (higher), or 'l' (lower)")
            
            if feedback in ['correct', 'c']:
                print(f"\n🎉 I got it! The number was {current_guess}")
                print(f"It took me {self.guesses} guesses!")
                break
            elif self.min_number > self.max_number:
                print("\n❌ Hey, something's not right! Are you sure you're giving me correct feedback?")
                print("The number range is impossible based on your responses.")
                break
            
            self.update_range(feedback)
        
        # Ask to play again
        while True:
            again = input("\nPlay again? (y/n): ").lower().strip()
            if again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'y' (yes) or 'n' (no)")
        
        if again in ['yes', 'y']:
            self.min_number = 1
            self.max_number = 100
            self.reset()
            self.play()
        else:
            print("\nThanks for playing! 👋")

def main():
    game = ComputerGuesser()
    game.play()

if __name__ == "__main__":
    main()
