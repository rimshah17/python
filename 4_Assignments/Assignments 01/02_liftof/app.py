import time
import os

def clear_screen():
    """Clear the console screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def rocket_countdown(seconds):
    """Countdown with detailed rocket animation"""
    rocket_stages = [
        # Stage 1: Initial position
        """
           🌟
          /\\
         /  \\
        /    \\
       /      \\
      |  USA  |
      |  ==   |
      |  ==   |
      |      |
     /|      |\\
    / |      | \\
   /  |      |  \\
  /   |      |   \\
 /    |      |    \\
/     |      |     \\
      """,
        # Stage 2: Small flame
        """
           🌟
          /\\
         /  \\
        /    \\
       /      \\
      |  USA  |
      |  ==   |
      |  ==   |
      |      |
     /|      |\\
    / |      | \\
   /  |      |  \\
  /   |      |   \\
 /    |  🔥  |    \\
/     | 🔥🔥 |     \\
      """,
        # Stage 3: Medium flame
        """
           ⭐
          /\\
         /  \\
        /    \\
       /      \\
      |  USA  |
      |  ==   |
      |  ==   |
      |      |
     /|      |\\
    / |      | \\
   /  |  🔥  |  \\
  /   | 🔥🔥 |   \\
 /    |🔥🔥🔥|    \\
/     |🔥🔥🔥|     \\
      """,
        # Stage 4: Large flame
        """
           💫
          /\\
         /  \\
        /    \\
       /      \\
      |  USA  |
      |  ==   |
      |  ==   |
      |      |
     /|  🔥  |\\
    / | 🔥🔥 | \\
   /  |🔥🔥🔥|  \\
  /   |🔥🔥🔥|   \\
 /    |🔥🔥🔥|    \\
/     |🔥🔥🔥|     \\
      """,
        # Stage 5: Liftoff flame
        """
           🌠
          /\\
         /  \\
        /    \\
       /      \\
      |  USA  |
      |  ==   |
      |  ==   |
     /|  🔥  |\\
    / | 🔥🔥 | \\
   /  |🔥🔥🔥|  \\
  /   |🔥🔥🔥|   \\
 /    |🔥🔥🔥|    \\
/     |🔥🔥🔥|     \\
      🔥🔥🔥🔥
      """
    ]

    # Pre-launch sequence
    print("\nInitiating launch sequence...")
    time.sleep(1)
    print("Performing system checks...")
    time.sleep(1)
    print("All systems go!")
    time.sleep(1)

    # Countdown with rocket animation
    for i in range(seconds, -1, -1):
        clear_screen()
        
        # Display current rocket stage
        if i > 0:
            print(rocket_stages[i % len(rocket_stages)])
            print(f"\n⏰ T-minus: {i} seconds")
            print("\nStatus: Pre-launch checks complete")
            print("Engines: Warming up")
            print("Fuel systems: Nominal")
            print("Weather conditions: Optimal")
        
        # Special liftoff animation
        elif i == 0:
            clear_screen()
            print("""
                🌠   🌠   🌠
                    🚀
                   ╱|╲
                  ╱ | ╲
                 ╱  |  ╲
                ╱   |   ╲
               ╱    |    ╲
              ╱     |     ╲
             ╱    🔥🔥🔥    ╲
            ╱    🔥🔥🔥🔥    ╲
            
               🌍 LIFTOFF! 🌍
            
            Mission Status: Launched
            Altitude: Increasing
            Speed: Accelerating
            """)
        
        # Add launch sound effect (visual representation)
        if i <= 3:
            print("\n🔊 *RUMBLE* 🔊")
        
        time.sleep(1)

    # Post-launch messages
    time.sleep(1)
    print("\nLaunch successful! 🎉")
    print("Mission control tracking nominal flight path.")
    time.sleep(1)

def main():
    """Main program loop"""
    print("🚀 Welcome to NASA Launch Control 🚀")
    
    while True:
        try:
            seconds = int(input("\nEnter countdown time (5-10 seconds): "))
            if 5 <= seconds <= 10:
                rocket_countdown(seconds)
                break
            else:
                print("Please enter a number between 5 and 10.")
        except ValueError:
            print("Please enter a valid number.")
        
        while True:
            again = input("\nInitiate another launch sequence? (yes/no): ").lower().strip()
            if again in ['yes', 'no', 'y', 'n']:
                break
            print("Please enter 'yes' or 'no'")
        
        if again in ['no', 'n']:
            print("\nMission Control signing off! 👨‍🚀")
            break

if __name__ == "__main__":
    main()

