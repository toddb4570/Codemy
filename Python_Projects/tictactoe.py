import os


def clear_screen():
	os.system("clear")


def print_board(board):

	print(f" {board[0]} | {board[1]} | {board[2]}")
	print("---+---+---")
	print(f" {board[3]} | {board[4]} | {board[5]}")
	print("---+---+---")
	print(f" {board[6]} | {board[7]} | {board[8]}")
	print("")

def check_winner(board, current_player):
	win_combinations = [
		[0,1,2], [3,4,5], [6,7,8], # by row
		[0,3,6], [1,4,7], [2,5,8], # by column 
		[0,4,8],[2,4,6] 			# by diagonal
	]

	# check for winner

	for combination in win_combinations:
		if board[combination[0]] == board[combination[1]] == board[combination[2]] == current_player:
			return True

	return False


def check_draw(board):
	return all(spot in ["X", "O"] for spot in board)

def play_tic_tac_toe():
	# initialize board
	board = [str(i) for i in range(1,10)]

	current_player = "X"

	while True:
		clear_screen()
		print_board(board)

		move = input(f"Player {current_player}, enter your move (1-9): ")
		if not move.isdigit() or int(move) < 1 or int(move) > 9:
			print("Invalid input. Please enter a number between 1 and 9. (Type <enter> to continue ...)")
			input("")
			continue

		move = int(move) - 1

		if board[move] in ["X", "O"]:
			print("That spot is already taken. Try again. (Type <enter> to continue ...)")
			input("")
			continue

		board[move] = current_player


		if check_winner(board, current_player):
			clear_screen()
			print_board(board)
			print(f"Player {current_player} wins!")
			break

		if check_draw(board):
			clear_screen()
			print_board(board)
			print("It is a draw!")
			break

		current_player = 'O' if current_player == 'X' else "X" 

play_tic_tac_toe()