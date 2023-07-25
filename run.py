import time
import sys
from random import randint


def print_out(data):
    """
    The function will display text as it typed in real
    time rather than dispaly all message at once
    """
    for letter in data:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


class GameBoard:

    def __init__(self, size):
        self.size = size
        self.board = [["-" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
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


def game_level():
    """
    function checks user input and defines the size of the game board
    need to add validation here
    """

    while True:
        message = """
    Please choose your gaming experience by choosing one of three options:
    choose 'b' for beginner
    choose 'i' for intermediate
    or  choose 'e' for expert.\n
    """
        print_out(message)
        global user_name
        user_name = input(f"Please enter username: ")
        user_input = input(f"Please indicate your game experience: ")
        user_experience = user_input.lower()

        try:
            if user_experience == "b":
                print_out(f"Thank you {user_name}. Your game experience level is beginner.\n")
                return 5
            elif user_experience == "i":
                print_out("Thank you. Your game experience level is intermediate.\n")
                return 10
            elif user_experience == "e":
                print_out("Thank you. Your game experience level is expert.\n")
                return 10
            else:
                raise ValueError
        except ValueError as e:
           print_out(f"Invalid data. You provided '{user_experience}', this is not recognised value.\n")


# -------------------------------------------------------------------------------
# def print_board(board):
#     """
#     Function builds game board
#     """
#     alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]

#     # if n is a paramter, take n number of characters from the alphabet
#     alphabet = ''.join(alphabet[:size])

#     column_values = []
#     for num in range(size):
#         column_values.append(num + 1)

#     print(" ", *column_values)

    
#     # loop over the zipped lists, row is the index, cell is the list in the loop
#     for index, row in enumerate(zip(alphabet, GameBoard.board)):
#         # there are two items in the list, 
#         # row[0] is the alphabet character, row[1] is the board row
#         # the character can be printed as is
#         # the board list must be joined as a string
#         print(
#             f'{row[0]} ', ' '.join(x for x in row[1])
#         )
# -----------------------------------------------------------------------------------
# Sample variables for trials
# -------------------------------------------------
size = 5
b = 0
num_ships = 5
user_board = GameBoard(size)
computer_board = GameBoard(size)
computer_ships = []
user_ship = []
computer_guess = []
# -------------------------------------------------
def game_decision_tree():
    """
    function that informs user about the board size, number of ships and gives option to choose ships
    """
    print_out(f"Thank you {user_name}. You can now place ships on the on the board.")
    print_out(f"The game board will have {size} rows and {size} columns." )
    print_out(f"You can place {num_ships} ships on the board.")
    print_out(f"You can choose location of the ships on the board or they will be set random.")
    user_decision = input(f"Do you wish to place the ships on the board Y/N: ").upper()
    print_out(user_decision)

# def random_ship_location(data):
#     """
#     randomly choose ships on the board
#     """

#     b = 0
#     while b < num_ships:
#         x = randint(0, size - 1)
#         y = randint(0, size -1)
#         if data.board[x][y] == "-":
#             data.board[x][y] = "@"
#             pair = (x, y)
#             computer_ships.append(pair)
#         else:
#             continue
#         b += 1

def random_ship_shot(data):
    """
    randomly shoot at ships
    """
    x = randint(0, size - 1)
    y = randint(0, size -1)
    pair = (x, y)

    # if data.board[x][y] == "-":
    #     data.board[x][y] = "0"
    #     print("miss")
    #     pair = (x, y)
    #     computer_guess.append(pair)
    # elif data.board[x][y] == "@":
    #     data.board[x][y] = "#"
    #     print("hit")
    #     pair = (x, y)
    #     computer_guess.append(pair)
    global num_ships
    if pair in computer_guess:
        print("shoot again")
    else:
        if pair not in computer_ships:
            data.board[x][y] = "0"
            print("miss\n")
            computer_guess.append(pair)
        else:
            data.board[x][y] = "#"
            print("Hit\n")
            computer_guess.append(pair)
            num_ships -= 1

# def validate_shot(data):
    

def player_choose_ships():
    """
    user can choose location of his own ships (need validation)
    # not working
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
    while True:
        ship_loc = input("please enter ship location: ")
        validate_coordinates(ship_loc)

        if validate_coordinates(ship_loc):
            print("Great, you choose your ship!")
            break
    return ship_loc


def validate_coordinates(values):
    """
    Function validates users ships coardinates
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])

    try:
        if len(values) > 3:
            print("bad batch")
            raise ValuepytError
        if len(values) == 3 and int(values[2]) != 0 and int(values[1]) != 1:
            print("incorrect value")
            raise ValueError
        if len(values) < 2:
            print("too short")
            raise ValueError
        if values[0].upper() not in ''.join(alphabet[:size]):
            print(f"{values[0].upper()} is not a column name on the game board")
            raise ValueError
        if values[1].isnumeric() == False:
            print(f" '{values[1]}' not a number")
            raise ValueError
        if int(values[1]) > size:
            print(f"{values[1]} is not a row number. Please choose number between 1 and {size}")
            raise ValueError

    
    except ValueError:
        print("Please enter valid coordinates.")
        return False
    
    return True


def tansform_coordinates(data):
    """
    Function checks if user coordinates are correct format 
    if yes, it returns values for x and y 
    # not working
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])
 
    if len(data) <= 3:
        if data[0].upper() in ''.join(alphabet[:size]):
            if len(data) == 3:
                if int(data[1]) == 1 and data[2] == 0:
                    return True
                elif len(data) < 3:
                    if int(data[1]) in range(size + 1):
                        return True


def random_ship_location(data):
    """
    randomly choose ships on the board
    """

    b = 0
    while b < num_ships:
        x = randint(0, size - 1)
        y = randint(0, size -1)
        if data.board[x][y] == "-":
# comment out to see if works when not display ships but check the list instead
            # data.board[x][y] = "@" 
            pair = (x, y)
            # data.append(pair)
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
# print(computer_ships)
# print("*" * 40)
# computer_board.print_board()
# print(computer_board.board[1][2])
# print(computer_ships)

# pair = (7, 3)
# if pair in computer_ships:
#     print("Yes")
# else:
#     print("no")
# word = "aa2"
# if word[1].isnumeric() == False:
#     print("bad")
# else:
#     print("goodS")

ship_coordinates = player_choose_ships()
print(ship_coordinates)

# ship_loc = input("please enter ship location: ")
# print(ship_loc)
# print(len(ship_loc))
# get_x_cordinate(ship_loc)
   

# -------------------------------------
# game trial function
def game_set():
    
    computer_board.print_board()
    random_ship_location(computer_board)
    # computer_board.print_board()


def play_game():
    
    random_ship_shot(computer_board)
    computer_board.print_board()


def main():

    global num_ships
    # intro()
    game_set()
    b = 0
    while b < 100 and num_ships > 0:
        play_game()
        print(num_ships)
        b += 1
    else:
        print("Game Over")

# main()
# -------------------------------------------------------