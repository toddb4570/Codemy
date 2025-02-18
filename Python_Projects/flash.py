import random
import os


# function to generate a math problem
def generate_flashcard(operation):
	
	num1 = random.randint(1, 10)
	num2 = random.randint(1, 10)

	if operation == "addition":
		correct_answer = num1 + num2
		question = f'{num1} + {num2} = ?'

	elif operation == "subtraction":
		correct_answer = num1 - num2
		question = f'{num1} - {num2} = ?'

	elif operation == "multiplication":
		correct_answer = num1 * num2
		question = f'{num1} * {num2} = ?'

	elif operation == "division":
		# ensure 2nd number is not zero and num1 is divisible by num2
		while num2 == 0 or num1 % num2 != 0:
			num1 = random.randint(1, 10)
			num2 = random.randint(1, 10)
		correct_answer = num1 // num2
		question = f'{num1} / {num2} = ?'


	return question, correct_answer

def main_menu():
	os.system("clear")
	print("\n--- Math Flashcard App ---")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. QUIT")

	choice = input("Choose and option between 1 and 5: ")

	return choice

# Do the operation
def flashcard_session(operation):
	while True:
		os.system("clear")
		question, correct_answer = generate_flashcard(operation)
		
		print(f"Flashcard is : {question}")

		user_answer = input("Your answer: ")

		verror = 0

		try:
			user_answer = int(user_answer)
		except ValueError:
			input("Please enter a valid number. (hit <ENTER> to continue)")
			verror = 1

		if not verror:
			if user_answer == correct_answer:
				print("Correct!!")
			else:
				print(f"Wrong. The correct answer is {correct_answer}.")


		next_step = input(f"\nWould you like another {operation} flashcard? (y/n)").lower()

		if next_step == "n":
			break;


def math_flashcard_app():
	while True:
		choice = main_menu()

		if choice == "1":
			flashcard_session("addition")
		elif choice == "2":
			flashcard_session("subtraction")
		elif choice == "3":
			flashcard_session("multiplication")
		elif choice == "4":
			flashcard_session("division")
		elif choice == "5":
			break
		else:
			input("Invalid choice. Try again. (hit <ENTER> to continue)")


math_flashcard_app()