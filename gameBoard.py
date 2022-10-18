from player import Player


# class that controls the gameboard and movement of seeds on the gameboard
class GameBoard:

    # defines the how to construct a gameboard object
    # requires 2 player objects to construct a gameboard object
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.board = [4] * 12
        self.score1 = 0
        self.score2 = 0

    # a method that prints the gameboard
    def print_board(self):
        tabs = "\t" * 4
        tempPrint = "Number of Seeds for p1: \t"
        # adds the number of seeds in each house for player 1 in a formatted way to a temp string to print out
        # needed a temp string because print adds a new line after every print
        for x in range(6):
            tempPrint = tempPrint + str(self.board[x]) + "\t\t"
        print(tempPrint)
        tempPrint = "House Numbers: " + tabs
        # adds the number of each house for player 1 to a temp string
        # will print bellow the number of seeds in each house to let the player know how to choose a house to pick from
        for j in range(0, 6):
            tempPrint = tempPrint + str(12 - j) + "\t\t"
        print(tempPrint)
        print("\n", tabs, "\t\t\tp1 score = ", self.score1, tabs, "p2 score = ", self.score2)
        tempPrint = "\nNumber of Seeds for p2: \t"
        # adds the number of seeds in each house for player 2 in a formatted way to a temp string to print out
        for i in reversed(range(-6, 0)):
            tempPrint = tempPrint + str(self.board[i]) + "\t\t"
        print(tempPrint)
        tempPrint = "House Numbers: " + tabs
        # adds the number of each house for player 1 to a temp string
        for k in range(1, 7):
            tempPrint = tempPrint + str(k) + "\t\t"
        print(tempPrint)

    def move(self, pickUpHouse, player):
        # this is function that changes the gameboard according to the player's move
        numOfSeeds = self.board[pickUpHouse]
        self.board[pickUpHouse] = 0
        for i in range(numOfSeeds, 0, -1):
            self.board[pickUpHouse - i] += 1
        counter = 0
        while (self.board[pickUpHouse - numOfSeeds + counter] == 2) or (
                self.board[pickUpHouse - numOfSeeds - counter] == 3):
            if player == self.player1:
                self.score1 += self.board[pickUpHouse - numOfSeeds + counter]
            else:
                self.score2 += self.board[pickUpHouse - numOfSeeds + counter]
            self.board[pickUpHouse - numOfSeeds + counter] = 0
            counter += 1

        # if (self.board[pickUpHouse-numOfSeeds] == 2) or (self.board[pickUpHouse-numOfSeeds] == 3):
        # player.score += self.board[pickUpHouse-numOfSeeds]
        self.print_board()

    # method that gets the score of a player passed in as a parameter
    def get_score(self, player):
        # checks if the passed in player is player1, if so returns score1
        if player == self.player1:
            return self.score1
        # otherwise the passed in player is player2, so the method returns score 2
        else:
            return self.score2

    # method that determines if someone has won the game
    def determine_if_win(self):
        # if score1 is greater than or equal to 25 then player 1 wins
        if self.score1 >= 25:
            return self.player1
        # if score2 is greater than or equal to 25 then player 2 wins
        elif self.score2 >= 25:
            return self.player2
        numSeedsInBoard = 0;
        # counts the number of seeds in the entire board
        for x in range(0, 12):
            numSeedsInBoard += self.board[x]
        # checks if there is only a single seed in the entire board
        if numSeedsInBoard == 1:
            # if there's only one seed in the board then if score1 is higher than score two then player 1 wins
            if self.score1 > self.score2:
                return self.player1
            # else player 2 wins because their score is higher than player 1
            else:
                return self.player2
        # if none of these cases are true then return none because the game should continue
        return None
