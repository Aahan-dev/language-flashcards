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
        """Display flashcards randomly for the user to learn."""
        if not self.flashcards:
            print("No flashcards available. Please add some first.")
            return

        