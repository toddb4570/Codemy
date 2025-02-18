
import os

os.system("clear")

def is_palindrome(string):
	clean_string = ''

	for character in string:
		if character.isalnum():
			clean_string += character.lower()

	return clean_string == clean_string[:: -1]

user_input = input("Enter a word or phrase to check if it is pal: ")

if is_palindrome (user_input):
	print(f"{user_input} is a palindrome")
else:
	print(f"{user_input} is NOT a palindrome")
