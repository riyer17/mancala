from gameBoard import GameBoard


class Player:
    # initializes a player object given a name
    def __init__(self, name):
        self.name = name


class Human:
    gameBoard = None;

    def __init__(self, name):
        self.name = name
        self.gameBoard = GameBoard("player1", "player2")


