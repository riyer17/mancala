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

    def get_score(self, player):
        if player == self.player1:
            return self.score1
        else:
            return self.score2
