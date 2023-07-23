import time
import sys
import random


class GameBoard:

    def __init__(self, size):
        self.size = size
        self.board = [["-" for x in range(size)] for y in range(size)]
        # self.num_ships = num_ships
        # self.name = name
        # self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        """
        Function builds game board
        """
        alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]

        # if n is a paramter, take n number of characters from the alphabet
        alphabet = ''.join(alphabet[:size])

        column_values = []
        for num in range(size):
            column_values.append(num + 1)

        print(" ", *column_values)

    
        # loop over the zipped lists, row is the index, cell is the list in the loop
        for index, row in enumerate(zip(alphabet, self.board)):
            # there are two items in the list, 
            # row[0] is the alphabet character, row[1] is the board row
            # the character can be printed as is
            # the board list must be joined as a string
            print(
                f'{row[0]} ', ' '.join(x for x in row[1])
            )

    # def guess(self, x, y):
    #     self.guesses.append((x, y))
    #     self.board[x][y] = "X"

    #     if (x, y) in self.ships:
    #         self.board[x][y] = "*"
    #         return "Hit"
    #     else:
    #         return "Miss"
    
    # def add_ship(self, x, y, type="computer"):
    #     if len(self.ships) >= self.num_ships:
    #         print("Error: you cannot add any more ships!")
    #     else:
    #         self.ships.append((x, y))
    #         if self.type == "player":
    #             self.board[x][y] = "O"

def print_board(board):
    """
    Function builds game board
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]

    # if n is a paramter, take n number of characters from the alphabet
    alphabet = ''.join(alphabet[:size])

    column_values = []
    for num in range(size):
        column_values.append(num + 1)

    print(" ", *column_values)

    
    # loop over the zipped lists, row is the index, cell is the list in the loop
    for index, row in enumerate(zip(alphabet, GameBoard.board)):
        # there are two items in the list, 
        # row[0] is the alphabet character, row[1] is the board row
        # the character can be printed as is
        # the board list must be joined as a string
        print(
            f'{row[0]} ', ' '.join(x for x in row[1])
        )
size = 10

user_board = GameBoard(size)

user_board.print_board()