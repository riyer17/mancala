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

    # runs each move and deals with user input
    # no actual calculation is happening in this function
    def runMove(self, player):
        # Prompts player to move
        playerInput = 0;
        if player == player1:
            playerInput = int(input("\nPlayer 1, Which house would you like to pick up seeds from?"))
            # keeps asking player1 to enter a valid number until they do
            while not 1 <= playerInput <= 6:
                print("Please enter a house that is on your side of the board.")
                playerInput = int(input("\nPlayer 1, Which house would you like to pick up seeds from?"))
        else:
            playerInput = int(input("\nPlayer 2, Which house would you like to pick up seeds from?"))
            # keeps asking player2 to enter a valid number until they do
            while not 7 <= playerInput <= 12:
                print("Please enter a house that is on your side of the board.")
                playerInput = int(input("\nPlayer 2, Which house would you like to pick up seeds from?"))
        self.gameBoard.move(12-playerInput, player) # changes the index to match the direction of the GameBoard's list


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

# a bunch of printing: prints the rules and everything the player needs to know
print("This is how the house numbering works: ")
print("p1: 12  11  10  9   8   7\np2: 1   2   3   4   5   6")
print("There are 24 seeds and 6 houses in this game of Oware. Each player may only pick up seeds from houses on their "
      "side. The first player who captures 24 seeds wins. "
      "\nMoves: A player picks up all the seeds in a house on their side and sows them in the houses "
      "counterclockwise, skipping the score houses and the house the seeds were picked from if there were more than "
      "twelve. "
      "\nCapturing: If the player lands in their opponent’s house and brings the count to 2 or 3, the player captures "
      "the seeds in that house and adds them to their scorehouse. If the house previous to the one they landed in was "
      "also brought to a count of 2 or 3, the player may capture those seeds as well; they can continue capturing, "
      "going backwards, until they reach a house in which they did not bring the count to 2 or 3. "
      "\nFeeding: If one player has no seeds left, the other player must make a move that will bring a seed to their "
      "side. If no such move is possible, the player captures all seeds on their own side and ends the game.")

counter = 0
# while loop for alternating between players, and if the game goes more than 100 moves (essentially an
# infinite loop), the game ends
while counter < 100:
    # alternates between players
    if counter%2 == 0:
        game.runMove(player1)
    else:
        game.runMove(player2)
    counter+=1;
