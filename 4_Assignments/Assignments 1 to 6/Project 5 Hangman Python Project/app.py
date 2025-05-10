import random

class Hangman:
    def __init__(self):
        self.words = ['python', 'hangman', 'programming', 'developer', 'challenge']
        self.max_attempts = 6
        self.reset_game()

    def reset_game(self):
        """Reset the game state for a new round"""
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_attempts = 0
        self.display_word = ['_' for _ in self.word_to_guess]

    def display_current_state(self):
        """Display the current state of the word and attempts"""
        print("\nCurrent word: " + ' '.join(self.display_word))
        print(f"Incorrect attempts: {self.incorrect_attempts}/{self.max_attempts}")
        print("Guessed letters: " + ', '.join(self.guessed_letters))

    def get_player_guess(self):
        """Get a valid letter guess from the player"""
        while True:
            guess = input("Guess a letter: ").lower().strip()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print("❌ You've already guessed that letter. Try again.")
                else:
                    return guess
            else:
                print("❌ Please enter a single letter.")

    def update_game_state(self, guess):
        """Update the game state based on the player's guess"""
        self.guessed_letters.append(guess)
        if guess in self.word_to_guess:
            for index, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.display_word[index] = guess
            print("✅ Good guess!")
        else:
            self.incorrect_attempts += 1
            print("❌ Incorrect guess!")

    def check_game_over(self):
        """Check if the game is over (win or lose)"""
        if '_' not in self.display_word:
            print(f"\n🎉 Congratulations! You've guessed the word: {self.word_to_guess}")
            return True
        elif self.incorrect_attempts >= self.max_attempts:
            print(f"\n💀 You've run out of attempts! The word was: {self.word_to_guess}")
            return True
        return False

    def play(self):
        """Main game loop"""
        print("🎮 Welcome to Hangman! 🎮")
        self.reset_game()

        while True:
            self.display_current_state()
            guess = self.get_player_guess()
            self.update_game_state(guess)

            if self.check_game_over():
                play_again = input("\nPlay again? (y/n): ").lower().strip()
                if play_again in ['y', 'yes']:
                    self.reset_game()
                else:
                    print("Thanks for playing! 👋")
                    break

def main():
    game = Hangman()
    game.play()

if __name__ == "__main__":
    main()
