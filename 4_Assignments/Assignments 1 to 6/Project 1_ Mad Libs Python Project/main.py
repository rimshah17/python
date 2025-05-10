class MadLibs:
    def __init__(self):
        # Collection of stories with placeholders
        self.stories = {
            "vacation": {
                "title": "My Crazy Vacation",
                "template": """Last summer, I went on a {adjective} vacation to {place}. 
I packed my {noun1} and {noun2} for the trip. 
During the journey, I saw a {adjective2} {animal} {verb1} by the road. 
At the hotel, the {occupation} greeted me with a {adjective3} smile and gave me a {food} as a welcome gift. 
I spent my days {verb2} at the {place2} and my evenings {verb3} under the {adjective4} stars.""",
                "prompts": [
                    "adjective", "place", "noun1", "noun2", "adjective2", "animal", 
                    "verb1 (present tense)", "occupation", "adjective3", "food", 
                    "verb2 (ending in -ing)", "place2", "verb3 (ending in -ing)", "adjective4"
                ]
            },
            "superhero": {
                "title": "The Adventures of Captain Random",
                "template": """In the city of {city}, there lived a {adjective} superhero named Captain {silly_word}.
Their secret identity was a {occupation} who loved {verb1} {plural_noun}.
One day, while {verb2} at the {place}, they discovered their superpower of shooting {plural_noun2} from their {body_part}!
Using their new power, they fought against the evil Dr. {funny_name}, who was trying to turn everyone into giant {animals}.
With the help of their trusty {adjective2} sidekick and a magical {object}, Captain {silly_word} saved the day!""",
                "prompts": [
                    "city", "adjective", "silly word", "occupation", "verb1 (present tense)", 
                    "plural noun", "verb2 (ending in -ing)", "place", "plural noun2", "body part",
                    "funny name", "animals (plural)", "adjective2", "object"
                ]
            }
        }

    def get_story_choice(self):
        """Let user choose a story"""
        print("\n📚 Available Stories:")
        for i, (key, story) in enumerate(self.stories.items(), 1):
            print(f"{i}. {story['title']}")
        
        while True:
            try:
                choice = int(input("\nChoose a story number: "))
                if 1 <= choice <= len(self.stories):
                    return list(self.stories.keys())[choice - 1]
                print("❌ Please choose a valid story number!")
            except ValueError:
                print("❌ Please enter a number!")

    def get_words(self, prompts):
        """Get word inputs from user"""
        words = {}
        print("\n🎯 Please provide the following words:")
        
        for prompt in prompts:
            while True:
                word = input(f"Enter a {prompt}: ").strip()
                if word:
                    words[prompt] = word
                    break
                print("❌ Please enter something!")
        
        return words

    def create_story(self, story_key, words):
        """Create the final story with user's words"""
        story = self.stories[story_key]
        template = story["template"]
        
        # Replace placeholders with user's words
        final_story = template
        for prompt, word in words.items():
            placeholder = "{" + prompt.split()[0] + "}"
            final_story = final_story.replace(placeholder, word)
        
        return story["title"], final_story

    def play(self):
        """Main game loop"""
        print("Welcome to Mad Libs! 📝")
        print("Let's create a funny story together!")
        
        while True:
            # Choose story
            story_key = self.get_story_choice()
            story = self.stories[story_key]
            
            # Get words from user
            words = self.get_words(story["prompts"])
            
            # Create and display the story
            title, final_story = self.create_story(story_key, words)
            
            print("\n📖 Your Mad Libs Story:")
            print("=" * 40)
            print(f"Title: {title}")
            print("=" * 40)
            print(final_story)
            print("=" * 40)
            
            # Ask to play again
            while True:
                again = input("\nWould you like to create another story? (yes/no): ").lower().strip()
                if again in ['yes', 'no', 'y', 'n']:
                    break
                print("Please enter 'yes' or 'no'")
            
            if again in ['no', 'n']:
                print("\nThanks for playing Mad Libs! 👋")
                break

def main():
    game = MadLibs()
    game.play()

if __name__ == "__main__":
    main()
