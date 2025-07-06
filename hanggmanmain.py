import random

# List of predefined words
word_list = ["apple", "bread", "chair", "plant", "house"]

# Choose a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create a display version of the word with underscores
display_word = ["_"] * len(secret_word)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("\nCurrent word: ", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
        # Reveal the guessed letter in the word
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_guesses - incorrect_guesses} guesses left.")

# Final game result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nSorry, you ran out of guesses. The word was:", secret_word)
