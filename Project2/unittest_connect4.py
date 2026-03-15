"""
George Athanasopoulos
Unit Test Project – Drop Chip Game
Part 2 – unittest
ET721 Software Development Practicum
"""

import unittest
from main import Connect4


class TestConnect4(unittest.TestCase):

    
    def setUp(self):
        self.game = Connect4()

    
    def test_horizontal_win(self):
        for col in range(4):
            self.game.board[5][col] = 'X'

        self.assertTrue(self.game.check_win('X'))

    
    def test_vertical_win(self):
        for row in range(4):
            self.game.board[row][2] = 'O'

        self.assertTrue(self.game.check_win('O'))

    
    def test_diagonal_down_right(self):
        for i in range(4):
            self.game.board[i][i] = 'X'

        self.assertTrue(self.game.check_win('X'))

    
    def test_diagonal_up_right(self):
        for i in range(4):
            self.game.board[5 - i][i] = 'O'

        self.assertTrue(self.game.check_win('O'))

    
    def test_no_win(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][1] = 'O'
        self.game.board[5][2] = 'X'
        self.game.board[5][3] = 'O'

        self.assertFalse(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))

    

    
    def test_successful_chip_drop(self):
        result = self.game.drop_chip(1)

        self.assertTrue(result)
        self.assertEqual(self.game.board[5][0], 'X')

    
    def test_full_column(self):
        for row in range(self.game.ROWS):
            self.game.board[row][0] = 'X'

        result = self.game.drop_chip(1)

        self.assertFalse(result)

    
    def test_invalid_column(self):
        self.assertFalse(self.game.drop_chip(0))
        self.assertFalse(self.game.drop_chip(8))

    
    def test_full_board(self):
        for row in range(self.game.ROWS):
            for col in range(self.game.COLS):
                self.game.board[row][col] = 'X'

        self.assertTrue(self.game.is_full())
        self.assertFalse(self.game.drop_chip(1))


if __name__ == "__main__":
    unittest.main()
