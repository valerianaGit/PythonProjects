# HANGMAN GAME 
import random
words = ["demure", "cutesy", "mindful"]
score = 6
word = random.choice(words)
uncovered_word = ["_"] * len(word)
hangman_stages = [
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
]


while score > 0 and "_" in uncovered_word:
    print("Score ", score)
    print(hangman_stages[score])
    letter_input = input("Enter a letter\n")
    if letter_input in word:
        for i, char in enumerate(word):
            if char == letter_input:
                uncovered_word[i] = letter_input
        print("You got it! ", "".join(uncovered_word))
    else:
        score -= 1
        print("Not a match, Your current score is ", score)
if "_" not in uncovered_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Score ", score)
    print(hangman_stages[score])
    print("Game over, the word was ", word)
