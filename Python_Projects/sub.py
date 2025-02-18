import subprocess
import os

def run_file(filename):
	try:
		subprocess.run(["python", filename], check=True)

	except subprocess.CalledProcessError:
		print(f"Error: could not run {filename}")


def main_menu():
	while True:

		#os.system("clear")

		print("\n--- Main Menu ---")
		print("1. Adventure.py")
		print("2. Arrow.py")
		print("3. ArrowTK.py")
		print("4. Get_Time.py")
		print("5. Hangman.py")
		print("6. Images.py")
		print("7. Palindrome_Checker.py")
		print("8. PasswordGenerator.py")
		print("9. PasswordValidator.py")
		print("10. Rock_Paper_Scissors.py")
		print("11. ToDo.py")
		print("12. Typing.py")
		print("13. Word_Count.py")
		print("14. anagram.py")
		print("15. draw.py")
		print("16. filez.py")
		print("17. flash.py")
		print("18. tictactoe.py")
		print("[Q]uit")

		choice = input("enter your selection: ")

		if choice == "5":
			run_file('Hangman.py')

		elif choice == "17":
			run_file('flash.py')

		elif choice == "Q":
			break

		else:
			print("I didn't implement all of them. Too tedious. Choose again.")


main_menu()