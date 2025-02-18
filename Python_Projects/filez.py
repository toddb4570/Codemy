import os

os.system("clear")

def create_file():
	text = input("Enter text for file: ")
	file_name = input("Enter a file name: ")
	file_location = input("Enter the location: ")

	if not os.path.exists(file_location):
		os.makedirs(file_location)

	file_path = os.path.join(file_location, file_name)

	with open(file_path, 'w') as  file:
		file.write(text)

	print(f"File '{file_name}' saved successfully at {file_location}.")

def open_file():
	file_name = input("Enter a file name: ")
	file_location = input("Enter the location: ")
	file_path = os.path.join(file_location, file_name)

	if os.path.exists(file_path):

		with open(file_path, 'r') as  file:
			print("\nFile Contents:")
			print(file.read())

	else:
		print(f"File '{file_name}' not found at {file_location}.")




def file_manager():
	while True:
		print("\n--- File Manager ---")
		print("1. Create (and save) a file")
		print("2. Open (and read) a file")
		print("3. Quit")

		choice = input("Choose an option: ")

		if choice == "1":
			create_file()
		elif choice == "2":
			open_file()
		elif choice == "3":
			break
		else:
			print(f"You selected {Choice}, but it is not an option.")


file_manager()
