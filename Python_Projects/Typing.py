import os
import time
import random

os.system("clear")


# List of sentences
sentences = [
	"The quick brown fox jumps over the lazy dog",
	"Python is an easy to learn [programming language.",
	"Artificial intelligence will shape the future of technology.",
	"Typing speed tests are quite stupid, and a waste of time.",
	"Consistent practice is key to mastering any skill."
]

# Figure out words/minute
def calculate_wpm(start_time, end_time, typed_text):

	time_take = end_time- start_time
	num_words = len(typed_text.split())
	wpm = num_words/time_take * 60

	return(round(wpm, 2))
	

def typing_speed_test():
	# Choose a random sentence
	sentence = random.choice(sentences)

	print("\n--- Typing Speed Test ---")
	print("When you are ready, the sentence will appear. Type the sentence as fast as you can:")


	input("Press enter when ready to start...(press <enter> when finished)")
	print(f"{sentence}")

	#try:
	start_time = time.time()

	typed_text = input()

	end_time = time.time()

	wpm = calculate_wpm(start_time, end_time, typed_text)

	print(f"Your typing speed is {wpm} words/minute.")
	if typed_text == sentence:
		print("Great job! No errors!!")
	else:
		print("However you had some errors.")

	#except ValueError:
		#print("opps")

def main():
	while True:

		os.system("clear")
		typing_speed_test()
		retry = input("\nDo you wish to try again? (y/n)?").lower()
		if retry != 'y':
			print("Thank you for using the Typing Speed test. Later Duder!")
			break



main()