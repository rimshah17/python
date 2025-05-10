import random
import time

class NumberGuessingGame:
    def __init__(self):
        self.difficulty_levels = {
            'easy': {'range': (1, 50), 'attempts': 10},
            'medium': {'range': (1, 100), 'attempts': 7},
            'hard': {'range': (1, 200), 'attempts': 5}
        }
        self.high_scores = {}  # Store best scores for each difficulty

    def get_difficulty(self):
        """Get user's chosen difficulty level"""
        print("\n🎮 Choose your difficulty level:")
        print("1. Easy   (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard   (1-200, 5 attempts)")
        
        while True:
            choice = input("\nEnter your choice (1-3): ").strip()
            if choice == '1':
                return 'easy'
            elif choice == '2':
                return 'medium'
            elif choice == '3':
                return 'hard'
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

    def get_guess(self, min_num, max_num):
        """Get and validate user's guess"""
        while True:
            try:
                guess = int(input(f"\nEnter your guess ({min_num}-{max_num}): "))
                if min_num <= guess <= max_num:
                    return guess
                print(f"❌ Please enter a number between {min_num} and {max_num}.")
            except ValueError:
                print("❌ Please enter a valid number.")

    def give_hint(self, guess, target, min_num, max_num):
        """Provide helpful hints to the user"""
        if guess < target:
            if target - guess > (max_num - min_num) // 2:
                return "📈 Much higher!"
            return "📈 Higher!"
        else:
            if guess - target > (max_num - min_num) // 2:
                return "📉 Much lower!"
            return "📉 Lower!"

    def play_game(self):
        """Main game logic"""
        difficulty = self.get_difficulty()
        min_num, max_num = self.difficulty_levels[difficulty]['range']
        max_attempts = self.difficulty_levels[difficulty]['attempts']
        target_number = random.randint(min_num, max_num)
        attempts = 0
        
        print(f"\n🎲 I've picked a number between {min_num} and {max_num}.")
        print(f"🎯 You have {max_attempts} attempts to guess it.")
        
        while attempts < max_attempts:
            attempts += 1
            print(f"\n📝 Attempt {attempts}/{max_attempts}")
            
            guess = self.get_guess(min_num, max_num)
            
            if guess == target_number:
                print(f"\n🎉 Congratulations! You've guessed the number in {attempts} attempts!")
                self.update_high_score(difficulty, attempts)
                return True
            
            hint = self.give_hint(guess, target_number, min_num, max_num)
            print(hint)
            
            # Show remaining attempts
            if attempts < max_attempts:
                print(f"❗ {max_attempts - attempts} attempts remaining")
        
        print(f"\n😔 Game Over! The number was {target_number}.")
        return False

    def update_high_score(self, difficulty, attempts):
        """Update high scores for the difficulty level"""
        if difficulty not in self.high_scores or attempts < self.high_scores[difficulty]:
            self.high_scores[difficulty] = attempts
            print(f"🏆 New high score for {difficulty} difficulty: {attempts} attempts!")

    def show_high_scores(self):
        """Display high scores for all difficulty levels"""
        if not self.high_scores:
            print("\n📊 No high scores yet!")
            return
        
        print("\n🏆 High Scores:")
        for difficulty, score in self.high_scores.items():
            print(f"{difficulty.capitalize()}: {score} attempts")

def main():
    game = NumberGuessingGame()
    
    print("Welcome to the Number Guessing Game! 🎮")
    print("Can you guess the number I'm thinking of?")
    
    while True:
        game.play_game()
        game.show_high_scores()
        
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'no', 'y', 'n']:
                break
            print("Please enter 'yes' or 'no'")
        
        if play_again in ['no', 'n']:
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
