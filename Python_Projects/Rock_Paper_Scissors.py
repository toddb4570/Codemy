import random
import os

def play_again():

	while True:
		user_input = input("Do you want to play again? (yes/no): ").lower()

		if user_input in ["yes", "no"]:
			return user_input == "yes"

		else:
			print ("Invalid input. Please enter 'yes' or 'no'")


def determine_winner(user_choice, computer_choice):

	if (user_choice == computer_choice):
		return "It's a tie!!!"

	elif (user_choice == 'rock' and computer_choice == "scissors") or \
			(user_choice == 'scissors' and computer_choice == "paper") or \
			(user_choice == 'paper' and computer_choice == "rock"):
		return "You win!!!"

	else:
		return "Computer wins. :-("


def get_computer_choice():
	# Have the computer select
	choices = ["rock", "paper", "scissors"]

	return random.choice(choices)

def get_user_choice():
	choices = {1:"rock", 2:"paper", 3:"scissors"}

	try:
		user_input = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))

		if user_input in choices:
			return choices[user_input]

		else:
			print("Invalid Input. Please chose from the selection.")
			get_user_choice()

	except ValueError:
		print("Invalid Input. Please chose from the selection.")
		print(get_user_choice())

def play_game():

	while True:
		os.system("clear")

		user_choice =  get_user_choice()
		computer_choice = get_computer_choice()

		print(f"You chose: {user_choice}")
		print(f"The computer chose: {computer_choice}")

		result = determine_winner(user_choice, computer_choice)
		print(result)

		# end game
		if not play_again():
			print ("Thanks for playing.")
			break

play_game()

