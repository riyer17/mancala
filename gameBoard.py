from player import Player


class GameBoard:

    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.board = [4] * 12
        self.score1 = 0
        self.score2 = 0

    def print_board(self):
        tabs = "\t" * 4
        tempPrint = "Number of Seeds for p1: \t"
        for x in range(6):
            tempPrint = tempPrint + str(self.board[x]) + "\t\t"
        print(tempPrint)
        tempPrint = "House Numbers: " + tabs
        for j in range(0, 6):
            tempPrint = tempPrint + str(12 - j) + "\t\t"
        print(tempPrint)
        print("\n", tabs, "\t\t\tp1 score = ", self.score1, tabs, "p2 score = ", self.score2)
        tempPrint = "\nNumber of Seeds for p2: \t"
        for i in reversed(range(-6, 0)):
            tempPrint = tempPrint + str(self.board[i]) + "\t\t"
        print(tempPrint)
        tempPrint = "House Numbers: " + tabs
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

        if self.determine_if_win() is not None:
            if self.determine_if_win() == self.player1:
                print("Congratulations, Player 1, you have won!")
            else:
                print("Congratulations, Player 2, you have won!")
            quit()
        self.print_board()

    def get_score(self, player):
        if player == self.player1:
            return self.score1
        else:
            return self.score2

    def determine_if_win(self):
        if self.score1 >= 25:
            return self.player1
        elif self.score2 >= 25:
            return self.player2
        numSeedsInBoard = 0;
        for x in range(0, 12):
            numSeedsInBoard += self.board[x]
        if numSeedsInBoard == 1:
            if self.score1 > self.score2:
                return self.player1
            else:
                return self.player2
        return None
