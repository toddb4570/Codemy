

def are_anagrams(word1, word2):
	return sorted(word2) == sorted(word1)

def find_anagrams(word, word_list):
	word = word.lower()

	return [w for w in word_list if are_anagrams(word, w.lower()) and w.lower() != word]

def anagram_solver():
	word_list = ["listen", "google", "dog", "silent", "barkus", "enlist", "god", "tinsel", "evil"]

	word = input("Enter word: ")

	anagrams = find_anagrams(word, word_list)

	if anagrams:
		print(f"Anagrams for \"{word}\" are: {', '.join(anagrams)}")
	else:
		print(f"No anagrams for \"{word}\" found.")



anagram_solver()