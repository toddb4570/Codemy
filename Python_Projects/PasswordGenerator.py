import random
import string
import os

os.system("clear")

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

def generate_password(length):
	while True:
		# Ensure we meet the basic criteria of the 4 things needed
		password = [
			random.choice(string.digits), # at least 1 digit
			random.choice(string.ascii_lowercase), # at least 1 lowercase
			random.choice(string.ascii_uppercase), # at least 1 uppercase
			random.choice(string.punctuation), # at least 1 special
		]

		# get rest of password
		# Get remaining length
		remaining_length = length - 4

		password += random.choices(
						string.digits + string.ascii_lowercase +
						string.ascii_uppercase + string.punctuation,
						k=remaining_length)

		# shuffle the characters
		random.shuffle(password)
		password = ''.join(password)

		is_valid, message = validate_password(password)

		if is_valid:
			return password

def password_generator():

	while True:
		try:
			length = int(input("How long do you want the password (8 min)? "))

			if length < 8:
				print("Password must be at least 8 characters.")
				continue

			break

		except ValueError:
			print("Invalid input. Please enter a number.")

	password = generate_password(length)
	print(f"Generated Password: {password}")



password_generator()