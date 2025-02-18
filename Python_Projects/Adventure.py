import os
import random

os.system("clear")

def display_intro():
	print("Welcome to your adventure!!")
	print("You're on a quest to save the princess in the castle.")
	print("Navigate with N (north), S, E, W")
	print("Be careful!! Good luck.")

def check_for_pit():
	return random.random() < .2

def adventure_game():
	display_intro()

	steps = 0
	success = random.randint(1, 10)

	while True:
		direction = input("Choose a direction (N/S/E/W: ").upper()

		if direction not in ["N", "S", "E", "W"]:
			print("Invalid direction. Try again.")
			continue
		
		steps += 1

		if check_for_pit():
			print(f"Oh No! When you moved {direction} and fell into a pit!! Game over.")
			break

		if steps >= success:
			print("Success. You found and rescued the princess!! YOU WIN!!")
			break
		else:
			print(f"Moving {direction} was a safe choice.")

def main():
	while True:

		adventure_game()

		replay = input("\n would you like to play again? ").lower()

		if replay != 'y':
			break

main()