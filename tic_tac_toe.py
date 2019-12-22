import random

def print_board(board):
	print([board[0], board[1], board[2]])
	print([board[3], board[4], board[5]])
	print([board[6], board[7], board[8]])
	
	
def make_move(board, index, letter):
	board[index] = letter
	
	
def is_winner(board, letter):
	combination = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
	[0, 3, 6], [1, 4, 7], [2, 5, 8],
	[0, 4, 8], [6, 4, 2]]
	
	for element in combination:
		if board[element[0]] == board[element[1]] == board[element[2]] == letter:
			return True
		
		
def copy_board(board):
	copy_board = []
	for element in board:
		copy_board.append(element)
	return copy_board
	
	
def is_free(board, index):
	if board[index] == " ":
		return True
	else:
		return False
		
		
def random_move(board, moves):
	result = []
	for move in moves:
		if is_free(board, move):
			result.append(move)
			
	if len(result) != 0:
		return random.choice(result)
	else:
		return None
		

def computer_move(board):
	for move in range(9):
		board_copy = copy_board(board)
		if is_free(board_copy, move):
			make_move(board_copy, move, "O")
			if is_winner(board_copy, "O"):
				return move
				
	for move in range(9):
		board_copy = copy_board(board)
		if is_free(board_copy, move):
			make_move(board_copy, move, "X")
			if is_winner(board_copy, "X"):
				return move
				
	move = random_move(board, [0, 2, 6, 8])
	if move != None:
		return move
		
	if is_free(board, 5):
		return 5
	
	return random_move(board, [1, 3, 5, 7])
	
	
def user_move(board):
	move = " "
	while True:
		move = input("Input move: ")
		if move in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
			if is_free(board, int(move)):
				return int(move)
				
				
def full(board):
	full = 0
	for index in range(9):
		if board[index] != " ":
			full += 1
			
	if full == 9:
		return True
	
	else:
		return False

if __name__ == '__main__':
	board = []
	for i in range(9):
		board.append(" ")
	while True:
		
		print_board(board)
		
		if is_winner(board, "O"):
			print("O is win")
			break
			
		if full(board):
			exit()
			
		make_move(board, user_move(board), "X")
		
		if is_winner(board, "X"):
			print("X is win")
			break
			
		print()
	
		print_board(board)
		
		if full(board):
			exit()
		
		make_move(board, computer_move(board), "O")
			
		print()
		
