import time

class CountdownTimer:
    def __init__(self):
        self.seconds = 0

    def get_time_input(self):
        """Get a valid time input from the user"""
        while True:
            try:
                self.seconds = int(input("Enter the number of seconds for the countdown: "))
                if self.seconds > 0:
                    return
                print("❌ Please enter a positive integer.")
            except ValueError:
                print("❌ Please enter a valid number.")

    def start_countdown(self):
        """Start the countdown timer"""
        print(f"\n⏳ Starting countdown for {self.seconds} seconds...")
        for remaining in range(self.seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')  # Print on the same line
            time.sleep(1)  # Wait for 1 second
        print("🎉 Time's up!")

    def play(self):
        """Main method to run the countdown timer"""
        self.get_time_input()
        self.start_countdown()

def main():
    timer = CountdownTimer()
    timer.play()

if __name__ == "__main__":
    main()
