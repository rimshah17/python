import random

class NumberGuessingGame:
    def __init__(self):
        self.min_number = 1
        self.max_number = 100
        self.target_number = None
        self.guesses = 0
        self.best_score = float('inf')
        
    def generate_number(self):
        """Generate a random target number"""
        self.target_number = random.randint(self.min_number, self.max_number)
        
    def get_valid_guess(self):
        """Get and validate user's guess"""
        while True:
            try:
                guess = input(f"\nEnter your guess ({self.min_number}-{self.max_number}): ").strip()
                
                # Check for quit command
                if guess.lower() in ['q', 'quit']:
                    return None
                    
                guess = int(guess)
                if self.min_number <= guess <= self.max_number:
                    return guess
                print(f"❌ Please enter a number between {self.min_number} and {self.max_number}")
            except ValueError:
                print("❌ Please enter a valid number")
    
    def provide_hint(self, guess):
        """Provide a hint based on the user's guess"""
        if guess < self.target_number:
            if self.target_number - guess > 20:
                return "📈 Much higher!"
            return "👆 Higher!"
        else:
            if guess - self.target_number > 20:
                return "📉 Much lower!"
            return "👇 Lower!"
    
    def play_round(self):
        """Play one round of the game"""
        self.generate_number()
        self.guesses = 0
        
        print("\n🎮 Let's play Number Guessing Game!")
        print(f"I'm thinking of a number between {self.min_number} and {self.max_number}")
        print("(Enter 'q' or 'quit' to end the game)")
        
        while True:
            guess = self.get_valid_guess()
            
            # Check if user wants to quit
            if guess is None:
                print("\nThanks for playing! 👋")
                return False
                
            self.guesses += 1
            
            if guess == self.target_number:
                print(f"\n🎉 Congratulations! You got it in {self.guesses} guesses!")
                
                # Update best score
                if self.guesses < self.best_score:
                    self.best_score = self.guesses
                    print("🏆 New best score!")
                print(f"Best score: {self.best_score} guesses")
                
                return True
            else:
                print(self.provide_hint(guess))
    
    def play(self):
        """Main game loop"""
        while True:
            if not self.play_round():
                break
                
            while True:
                again = input("\nPlay again? (y/n): ").lower().strip()
                if again in ['y', 'n', 'yes', 'no']:
                    break
                print("Please enter 'y' (yes) or 'n' (no)")
            
            if again in ['n', 'no']:
                print("\nThanks for playing! 👋")
                break

def main():
    game = NumberGuessingGame()
    game.play()

if __name__ == "__main__":
    main()
