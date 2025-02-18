import os
import random


os.system("clear")

#creating a list of words
word_list = ['python', 'javascript', 'ruby', 'perl', 'hangman', 'developer', 'coder', 'variable', 'syntax', 'function']

def get_random_word():
	return random.choice(word_list)

# Display the current state of the guessed word
def display_word(word, guessed_letters):
	
	return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


def play_hangman():
	word = get_random_word()

	word_length = len(word)

	# Keep track of guesses
	guessed_letters = set()
	incorrect_guesses = set()
	lives = 6 # Number of incorrect guesses allowed

	print ("Welcome to Hangman!")
	print (f"the word has {word_length} letters.")

	# main game loop
	while lives > 0:
		print("\n" + display_word(word, guessed_letters))
		print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
		print(f'Lives remaining: {lives}')

		guess = input("Guess a letter: ").lower()

		# validate guesses

		if len(guess) != 1 or not guess.isalpha():
			print("Invalid input. Please enter a single letter.")
			os.system("clear")
			continue

		if guess in guessed_letters or guess in incorrect_guesses:
			os.system("clear")
			print(f" You already guessed '{guess}''. Try a different letter.")
			continue

		if guess in word:
			os.system("clear")
			guessed_letters.add(guess)
			print(f"Good guess! The letter '{guess}'' is in the word")
		else:
			os.system("clear")
			incorrect_guesses.add(guess)
			lives -= 1
			print(f"Bad guess! The letter '{guess}' isn't in the word")

		if all(letter in guessed_letters for letter in word):
			print(f"\nCongrats!! You guessed the word!! It was \"{word}\".")
			break

	if lives == 0:
			print(f"\nYou ran out of lives! The word was: \"{word}\".")



play_hangman()