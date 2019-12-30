import unittest 
from unittest.mock import patch

from tic_tac_toe import *


class TicTacToeTest(unittest.TestCase):

	def test_is_winner_x(self):
		board = []
		
		for i in range(9):
			board.append("X")
			
		self.assertTrue(is_winner(board, "X"))
		
	def test_is_winner_o(self):
		board = []
		
		for i in range(9):
			board.append("O")
			
		self.assertTrue(is_winner(board, "O"))
		
	def test_is_free_True(self):
		board = []
		
		for index in range(9):
			board.append(" ")
			self.assertEqual(is_free(board, index), True)
			
	def test_is_free_False(self):
		board = []
		
		for index in range(9):
			board.append("#")
			self.assertFalse(is_free(board, index))

	def test_computer_move(self):
		board = []
		for x in range(9):
			board.append(" ")
		self.assertEqual(type(computer_move(board)), int)	
		
	def test_copy_board(self):
		self.assertEqual(copy_board([]), [])
		
	@patch('random.choice')
	def test_random_move_random(self, mocked_choice):
		mocked_choice.return_value = 1000
		board = []
		for i in range(9):
			board.append(" ")
		self.assertEqual(random_move(board, range(9)), 1000)
		
	def test_random_move_None(self):
		board = []
		for i in range(9):
			board.append(" ")
		self.assertEqual(random_move(board, []), None)
	
	@patch('builtins.input')	
	def test_user_move(self, mocked_input):
		mocked_input.return_value = "2"
		board = [" " for i in range(9)]
		self.assertEqual(user_move(board), 2)
		
	def test_full_True(self):
		board = ["#" for x in range(9)]
		self.assertTrue(full(board))
		
	def test_full_False(self):
		board = [" " for x in range(9)]
		self.assertFalse(full(board))

if __name__ == '__main__':
	unittest.main()
	
