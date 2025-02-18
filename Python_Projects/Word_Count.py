import os

os.system("clear")

def count_words(string):
	words = string.split()
	word_cnt = len(words)

	return word_cnt

def count_characters_with_spaces(string):
	return(len(string))
	

def count_characters_without_spaces(string):
	string.replace(" ", "")
	return len(string.replace(" ", ""))

def word_count_program():
	string = input("Enter a string: ")
	word_cnt = 0
	ccwithspaces = 0

	word_cnt = count_words(string)
	ccwithspaces = count_characters_with_spaces(string)
	ccwithoutspaces = count_characters_without_spaces(string)

	print(f"Word Count = {word_cnt}")
	print(f"Character count w/spaces: {ccwithspaces}")
	print(f"Character count wo/spaces: {ccwithoutspaces}")


word_count_program()