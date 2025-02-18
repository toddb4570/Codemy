
import string
import os


os.system("clear")

digit = "Todd"
print (digit.isdigit())

def validate_password(password):
	if len(password) < 8:
		return False, "Password must be at least 8 characters long."
	if not any(char.isdigit() for char in password):
		return False, "Password have at least one digit."
	if not any(char.islower() for char in password):
		return False, "Password have at least one lowercase letter."
	if not any(char.isupper() for char in password):
		return False, "Password have at least one uppercase letter."
	if not any(char in string.punctuation for char in password):
		return False, "Password have at least one special character."

	return True, "Password is strong"


def show_password_rules():

	print("Password Rules:")
	print("1. Must be at least 8 characters long.")
	print("2. Must contain at least one digit (0-9).")
	print("3. Must contain at least one lower case (a-z).")
	print("4. Must contain at least one upper case (A-Z).")
	print(f"5. Must contain at least one special character {string.punctuation}.")
	print()

def password_validator():
	show_password_rules()

	password = input("Please enter your password: ")

	AllOK, message = validate_password(password)

	if AllOK:
		print("Success: ", message)
	else:
		print("vALIDATION FAILED: ", message)

password_validator()