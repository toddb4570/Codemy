# Todd Barkus 20250107
# Webinar project guessing_game()
# https://members.codemy.com/l/python-projects/ (with modifications)

import os
import random
from tkinter import *

#initialize the game state variables
number_to_guess = None
number_of_guesses = 0
low_value = 1
high_value = 10

def reset_game():
	global number_to_guess, number_of_guesses, low_value, high_value

	number_to_guess = random.randint(low_value, high_value)

	# Remove the label
	result_label.config(text="")

	# Clear entry box
	guess_entry.delete(0, END)

	# Set the submit
	submit_button.config(state=NORMAL)

	# Hide the play again button...again
	play_again_button.pack_forget()	

def check_guess():
	global number_of_guesses

	# Use error handling
	try:
		guess = int(guess.entry.get())
		number_of_guesses +=1

		if guess < number_to_guess:
			result_label.config(text="Too low - Try again")

		elif guess > number_to_guess:
			result_label.config(text="Too high - Try again")

		else:
			result_label.config(text=f"Correct! The number was {guess} and you guessed it in {number_of_guesses} attempts!")
			submit_button.config(state=DISABLED)
			pay_again.button.pack()


	except ValueError:
		result_label.config(text="Invalid input.")



def setup_gui():

	global low_value, high_value
	root = Tk()
	root.title("Guessing Game")
	root.geometry('500x350')

	# Create a label
	instruction_label = Label(root, text=f"Guess a number between {low_value} and {high_value}.",
		font=("Helvetica", 18))
	instruction_label.pack(pady=20)

	# Create an entry box
	guess_entry = Entry(root, font=("Helvetica", 18))
	guess_entry.pack(pady=10)

	# Create another label
	result_label = Label(root, text="")
	result_label.pack(pady=20)

	# Create buttons
	submit_button = Button(root, text="Submit Guess", command=check_guess)
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?", command=reset_game)
	play_again_button.pack()
	# Hide the button
	play_again_button.pack_forget()
	print("Done in setup_gui")

	reset_game()

	root.mainloop()
	
setup_gui()