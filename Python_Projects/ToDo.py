import os

os.system("clear")

def add_task(tasks, task):
	tasks.append({"task": task, "completed": False})
	print(f"Task \"{task}\" has been added")
	return tasks

def view_tasks(tasks):
	if not tasks:
		print("No tasks in list.")
	else:
		print("\nTo-Do list:")
		for idx, task_info in enumerate(tasks, 1):
			status = "Done" if task_info["completed"] else "Not Done"
			print(f"{idx}. {task_info["task"]} - {status}")
		print()

def remove_task(tasks):

	if tasks:
		view_tasks(tasks)
		task_index = int(input("Enter the task number to remove: ")) - 1

		if 0 <= task_index < len(tasks):
			removed_task = tasks.pop(task_index)
			print(f"Removed task: {removed_task['task']}")

		else:
			print("Invalid task number.")
	else:
		print("\nThere are no tasks to remove.")

	return tasks

def complete_task(tasks):
	if tasks:
		view_tasks(tasks)
		task_index = int(input("Enter the task number to complete: ")) - 1

		if 0 <= task_index < len(tasks):
			tasks[task_index]["completed"] = True
			print(f'Completed task: {tasks[task_index]["task"]}')

		else:
			print("Invalid task number.")
	else:
		print("\nThere are no tasks to complete.")

	return tasks

def to_do_list_app():
	tasks = []

	while True:

		os.system("clear")

		print("\n--- To-Do List Menu ---")
		print("1. Add Task")
		print("2. View Tasks")
		print("3. Remove Task")
		print("4. Complete Task")
		print("5. Quit")

		choice = input("Choose an option: ")

		if choice == '1':
			task = input("Enter the task: ")
			tasks = add_task(tasks, task)
			input("Press enter to continue ...")

		elif choice == '2':
			view_tasks(tasks)
			input("Press enter to continue ...")

		elif choice == '3':
			tasks = remove_task(tasks)
			input("Press enter to continue ...")

		elif choice == '4':
			tasks = complete_task(tasks)
			input("Press enter to continue ...")

		elif choice == '5':
			break

		else:
			print(f"Invalid Option ({choice}). Please try again.")
			input("Press enter to continue ...")

to_do_list_app()

