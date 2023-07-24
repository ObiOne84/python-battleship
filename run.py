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
                f'{row[0]}', ' '.join(x for x in row[1])
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

# Sample variables for trials
# -------------------------------------------------
size = 10
b = 0
num_ships = 10
user_board = GameBoard(size)
computer_board = GameBoard(size)
computer_ships = []
# -------------------------------------------------

def random_ship_location(data):
    """
    randomly choose ships on the board
    """

    b = 0
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

def player_choose_ships():
    """
    user can choose location of his own ships (need validation)
    """
    # b = 0
    # while b < num_ships:
    #     x = int(input("please enter number 0-9: "))
    #     y = int(input("pluse enter number 0-9: "))
    #     if user_board.board[x][y] == "-":
    #         user_board.board[x][y] = "@"
    #         user_board.print_board()
    #     else:
    #         print("ship is already there")
    #     b += 1
    # while b < num_ships:
    #     ship_loc = int(input("please enter ship location: "))
    #     transfor_coordinates(ship_loc)
    #     if user_board.board[x][y] == "-":
    #         user_board.board[x][y] = "@"
    #         user_board.print_board()
    #     else:
    #         print("ship is already there")
    #     b += 1
    b = 0
    while b < num_ships:
        while True:
            ship_loc = input("please enter ship location: ")
            tansform_coordinates(ship_loc)
            break
        b += 1
  
        

def tansform_coordinates(data):
    """
    Function checks if user coordinates are correct format 
    if yes, it returns values for x and y
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])
    while True:
        try:
            if len(data) <= 3:
                if data[0].upper() in ''.join(alphabet[:size]):
                    if len(data) == 3:
                        if int(data[1]) == 1 and data[2] == 0:
                            return True
                        else:
                            raise ValueError
                    elif len(data) < 3:
                        if int(data[1]) in range(size + 1):
                            return True
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                else:
                    raise ValueError
        except ValueError as e:
            print(f"Invalid data. You provided '{data}', this is not recognised value.\n")
            break


def random_ship_location(data):
    """
    randomly choose ships on the board
    """

    b = 0
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


def validate_ship_loc(board, x, y):
    """
    function validates user input for ship location
    """
    n = 5
    b = 0
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
      
    x = input(f"Provide your element: ")
  
            # b = 0
            # while b < n:

            # x = input(f"Provide your element: ")
            # y = input(f"Second number: ")
            # board[int(x) - 1][int(y) - 1] = "X"
            # b += 1
       
    try:
        if len(x) <= 3:
            # print(len(x))
            for symbols in alphabet:
                if x[0].upper() in symbols:
                    print(symbols.index(x[0].upper()))
                    if len(x) == 3:
                        if int(x[1]) in range(n + 1) and x[2] == 0:
                            print(int(x[1] + x[2]) - 1)
                            board[symbols.index(x[0].upper())][int(x[1] + x[2]) - 1] = "@"   
                    elif len(x) < 3:
                        if int(x[1]) in range(n + 1):
                            print(int(x[1]) - 1)
                            board[symbols.index(x[0].upper())][int(x[1]) - 1] = "@"   
                    else:
                        raise ValueError
        else:
            raise ValueError
    except ValueError as e:
        text_print_control(f"Invalid data. You provided '{x}', this is not recognised value.\n")


# -------------------------------------------------------
# Test area
# random_ship_location(computer_board)
# random_ship_location(user_board)
# print("Szymon Board")
# user_board.print_board()
# print("*" * 40)
# print("Computer Board")
# computer_board.print_board()
# print("*" * 40)
# computer_board.print_board()
# print(computer_board.board[1][2])
# print(computer_ships)
# pair = (7, 3)
# if pair in computer_ships:
#     print("Yes")
# else:
#     print("no")
player_choose_ships()


# alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
# alphabet = ''.join(alphabet[:n])

# if data[0].upper() in ''.join(alphabet[:n]):
#     print(data[0].upper())
#     print(alphabet.index(data[0].upper()))
# else:
#     print("out of range")
    
# print(''.join(alphabet[:n]))


# -------------------------------------------------------
