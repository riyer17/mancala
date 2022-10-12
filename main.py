from gameBoard import GameBoard
from player import Player

player1 = Player("olee")
player2 = Player("rohan")

board = GameBoard(player1, player2)
board.print_board()