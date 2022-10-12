from player import Player
from player import Human
from gameBoard import GameBoard


class Game:
    player1 = None;
    player2 = None;
    gameBoard = None;

    def __init__(self):
        self.player1 = Player("player1");
        self.player2 = Player("player2");
        self.gameBoard = GameBoard("player1", "player2");

    # parameter is whatever player is making a move
    def runMove(self, player):
        # Prompts player to move
        playerInput = int(input("Which house would you like to pick up seeds from?"))
        player.move(12-playerInput) # changes the index to match the direction of the GameBoard's list
        # Runs the move and the GameBoard makes changes
        # Print the gameboard at the end of each move
        self.gameBoard.printBoard()


    # def runGame(self):
    player1Type = input("Player 1: Human or computer?")
    if (player1Type.containsIgnoreCase("human")):
        player1 = Human();
    else:
        player1 = Computer();
    player2Type = input("Player 2: Human or computer?")
    if (player2Type.containsIgnoreCase("human")):
        player2 = Human();
    else:
        player2 = Computer();

    print("This is how the house numbering works: ")
    print("12  11  10  9   8   7\n1   2   3   4   5   6")
    counter = 0
    while (counter < 100):
        if (counter%2 == 0):
            runMove(player1)
        else:
            runMove(player2)