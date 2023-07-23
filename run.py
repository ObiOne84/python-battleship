import time
import sys
from random import randint


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
b = 0
num_ships = 10
user_board = GameBoard(size)
computer_board = GameBoard(size)

def player_choose_ships():
    # user can choose location of his own ships (need validation)
    user_board.print_board()
    while b < num_ships:
        x = int(input("please enter number 0-9: "))
        y = int(input("pluse enter number 0-9: "))
        if user_board.board[x][y] == "-":
            user_board.board[x][y] = "@"
            user_board.print_board()
        else:
            print("ship is already there")
        b += 1

computer_ships = []
def random_ship_location(data):
    b = 0
    #  randomly choose ships on the board
    while b < num_ships:
        x = randint(0, size - 1)
        y = randint(0, size -1)
        if data.board[x][y] == "-":
            data.board[x][y] = "@"
            pair = (x, y)
            computer_ships.append(pair)
        else:
            continue
        b += 1



random_ship_location(computer_board)
# random_ship_location(user_board)
# print("Szymon Board")
# user_board.print_board()
# print("*" * 40)
# print("Computer Board")
# computer_board.print_board()
# print("*" * 40)
# computer_board.print_board()
# print(computer_board.board[1][2])
print(computer_ships)
pair = (7, 3)
if pair in computer_ships:
    print("Yes")
else:
    print("no")
