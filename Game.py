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
        if player == player1:
            playerInput = int(input("\nPlayer 1, Which house would you like to pick up seeds from?"))
        else:
            playerInput = int(input("\nPlayer 2, Which house would you like to pick up seeds from?"))
        self.gameBoard.move(12-playerInput, player) # changes the index to match the direction of the GameBoard's list
        # Runs the move and the GameBoard makes changes
        # Print the gameboard at the end of each move


game = Game()
player1Type = input("Player 1: Human or computer?")
if "human" in player1Type.lower():
    player1 = Human("player1")
# else:
    # player1 = Computer();
player2Type = input("Player 2: Human or computer?")
if "human" in player2Type.lower():
    player2 = Human("player2")
# else:
    # player2 = Computer();

print("This is how the house numbering works: ")
print("p1: 12  11  10  9   8   7\np2: 1   2   3   4   5   6")
counter = 0
while counter < 100:
    if counter%2 == 0:
        game.runMove(player1)
    else:
        game.runMove(player2)
    counter+=1;
