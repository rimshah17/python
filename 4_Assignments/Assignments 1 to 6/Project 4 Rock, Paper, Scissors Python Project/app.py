import random
import time

class RockPaperScissors:
    def __init__(self):
        self.moves = {
            'r': '🪨 Rock',
            'p': '📄 Paper',
            's': '✂️ Scissors'
        }
        self.winning_combinations = {
            'r': 's',  # rock beats scissors
            'p': 'r',  # paper beats rock
            's': 'p'   # scissors beats paper
        }
        self.scores = {'player': 0, 'computer': 0, 'ties': 0}
        
    def display_welcome(self):
        """Display welcome message and game instructions"""
        print("\n🎮 Welcome to Rock, Paper, Scissors! 🎮")
        print("\nHow to play:")
        print("Enter 'r' for Rock 🪨")
        print("Enter 'p' for Paper 📄")
        print("Enter 's' for Scissors ✂️")
        print("Enter 'q' to quit")
        
    def get_player_move(self):
        """Get and validate player's move"""
        while True:
            move = input("\nYour move: ").lower().strip()
            if move in ['r', 'p', 's', 'q']:
                return move
            print("❌ Invalid move! Please enter 'r', 'p', 's', or 'q'")
            
    def get_computer_move(self):
        """Generate computer's move"""
        return random.choice(['r', 'p', 's'])
        
    def determine_winner(self, player_move, computer_move):
        """Determine the winner of the round"""
        if player_move == computer_move:
            self.scores['ties'] += 1
            return "🤝 It's a tie!"
        elif self.winning_combinations[player_move] == computer_move:
            self.scores['player'] += 1
            return "🎉 You win!"
        else:
            self.scores['computer'] += 1
            return "💻 Computer wins!"
            
    def display_moves(self, player_move, computer_move):
        """Display both moves with dramatic effect"""
        print("\nRock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print(f"\nYou chose: {self.moves[player_move]}")
        print(f"Computer chose: {self.moves[computer_move]}")
        
    def display_scores(self):
        """Display current scores"""
        print("\n📊 Score Board:")
        print(f"You: {self.scores['player']} | Computer: {self.scores['computer']} | Ties: {self.scores['ties']}")
        
    def play_round(self):
        """Play one round of the game"""
        player_move = self.get_player_move()
        
        # Check if player wants to quit
        if player_move == 'q':
            return False
            
        computer_move = self.get_computer_move()
        self.display_moves(player_move, computer_move)
        
        result = self.determine_winner(player_move, computer_move)
        print(f"\n{result}")
        self.display_scores()
        
        return True
        
    def play(self):
        """Main game loop"""
        self.display_welcome()
        
        while True:
            if not self.play_round():
                break
                
            while True:
                again = input("\nPlay again? (y/n): ").lower().strip()
                if again in ['y', 'n', 'yes', 'no']:
                    break
                print("Please enter 'y' (yes) or 'n' (no)")
                
            if again in ['n', 'no']:
                print("\n🏆 Final Scores:")
                self.display_scores()
                print("\nThanks for playing! 👋")
                break

def main():
    game = RockPaperScissors()
    game.play()

if __name__ == "__main__":
    main()
