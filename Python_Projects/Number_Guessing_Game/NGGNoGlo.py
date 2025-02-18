# Todd Barkus 20250107
# Webinar project by John Elder
# https://members.codemy.com/l/python-projects/ (with modifications)

from tkinter import *
import os
import random

low_value = 1
high_value = 10

def reset_game(guess_entry, result_label, submit_button, play_again_button, state):

	state['number_to_guess'] = random.randint(low_value, high_value)

	state['number_of_guesses'] = 0

	# Remove result label
	result_label.config(text="")

	# Clear the entry box
	guess_entry.delete(0, END)

	# Set the submit button back to normal
	submit_button.config(state=NORMAL)

	# Hide the play again button ... again
	play_again_button.pack_forget()

def check_guess(guess_entry, result_label, submit_button, play_again_button, state):


	# Use error handling
	try:
		guess = int(guess_entry.get())
		state['number_of_guesses'] +=1

		if guess < state['low_value'] or guess > state['high_value']:
			result_label.config(text=f"{guess} is out of range - Try again")

		elif guess < state['number_to_guess']:
			result_label.config(text=f"{guess} is too low - Try again")

		elif guess > state['number_to_guess']:
			result_label.config(text=f"{guess} is too high - Try again")

		else:
			result_label.config(text=f"Correct! The number was {guess} and you guessed it in {state['number_of_guesses']} attempts!")
			submit_button.config(state=DISABLED)
			play_again_button.pack()


	except ValueError:
		result_label.config(text="Invalid input.")

	# Clear the entry box
	guess_entry.delete(0, END)

def setup_gui():

	root = Tk()
	root.title("Guessing Game")
	root.geometry('500x350')
	low_value = 1
	high_value = 10

	#set game state
	state = {'number_to_guess': None, 'number_of_guesses': 0, 'low_value': low_value, 'high_value': high_value}

	# Create a label
	instruction_label = Label(root, text=f"Guess a number between {low_value} and {high_value}.", font=("Helvetica", 18))
	instruction_label.pack(pady=20)

	# Create an entry box
	guess_entry = Entry(root, font=("Helvetica", 18))
	guess_entry.pack(pady=10)

	# Create another label
	result_label = Label(root, text="")
	result_label.pack(pady=20)

	# Create some buttons
	submit_button = Button(root, text="Submit Guess", 
		command=lambda: check_guess(guess_entry, result_label, submit_button, play_again_button, state))
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play again?", 
		command=lambda: reset_game(guess_entry, result_label, submit_button, play_again_button, state))
	play_again_button.pack()
	# Hide the button for now
	play_again_button.pack_forget()

	reset_game(guess_entry, result_label, submit_button, play_again_button, state)

	root.mainloop()

#call main function
setup_gui()

