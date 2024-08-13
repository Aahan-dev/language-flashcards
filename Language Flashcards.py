import random

class Flashcard:
    def __init__(self, word, translation): # Initialize the flashcard with a word and its translation.
        self.word = word
        self.translation = translation

    def __str__(self): # Returns the flashcards as a string        
        return f"{self.word} -> {self.translation}"

class FlashcardApp:
    def __init__(self): # Initialize the flashcard application with an empty list of flashcards.
        self.flashcards = []

    def add_flashcard(self, word, translation):# Adds Flashcards to a set        
        flashcard = Flashcard(word, translation)
        self.flashcards.append(flashcard)  # Add the flashcard to the list
        print(f"Flashcard added: {flashcard}")

    def learn(self): # Learns flashcards
        
        if not self.flashcards: 
            print("No flashcards available. Please add some first.")
            return
        print("\nStarting Flashcard Learning!")
        random.shuffle(self.flashcards)  # Shuffle the flashcards for random order


        for flashcard in self.flashcards:# Iterate through the flashcards
            input(f"Word: {flashcard.word} (Press Enter to see the translation)")# Display the word and wait for user input
            print(f"Translation: {flashcard.translation}\n")# Display the translation


def main():# Main function to run the flashcard application.
    
    app = FlashcardApp()  # Create an instance of FlashcardApp


    while True:
        print("\nLanguage Flashcards")
        print("1. Add Flashcard")
        print("2. Learn Flashcards")
        print("3. Exit")


        choice = input("Choose an option: ")


        if choice == '1':
            word = input("Enter the word to learn: ")
            translation = input("Enter the translation: ")
            app.add_flashcard(word, translation)  # Add a new flashcard


        elif choice == '2':
            app.learn()  # Start learning with flashcards


        elif choice == '3':
            print("Exiting the Flashcard application. Goodbye!")
            break  # Exit the loop


        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()  # Run the main function

        