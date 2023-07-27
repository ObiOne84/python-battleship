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
shots = 5
guesses = []
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


def random_ship_shot(data):
    """
    randomly shoot at ships
    """
    x = randint(0, size - 1)
    y = randint(0, size -1)
    pair = (x, y)

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


def player_choose_ships():
    """
    user can choose location of his own ships

    """

    while True:
        ship_loc = input("please enter ship location: ")

        if validate_coordinates(ship_loc):
            print("Great, you choose your ship!")
            break
    return ship_loc.upper()


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
        if len(values) == 3 and int(values[1] + values[2]) != 10:
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


def return_x_value(data):
    """
    Function return x coordinate for the ship or shot
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])
 
    if data[0] in ''.join(alphabet[:size]):
        x = alphabet.index(data[0])
        return x


def return_y_value(data):
    """
    Function return y coordinate for the ship or shot
    """
    if len(data) == 3:
        y = int(data[1] + data[2]) - 1
        return y
    else:
        y = int(data[1]) - 1
        return y


def user_ship_location(data, x, y):
    """
    Append ship  to the game board as per user coordinates 
    """

    if data.board[x][y] == "-":
        data.board[x][y] = "@" 
        pair = (x, y)
        # data.append(pair)
        user_ship.append(pair)
    elif data.board[x][y] == "@":
        print("You already placed ship here")


def user_shots(data, x, y):
    """
    Check the position of the ships, and 
    """

    pair = (x, y)
    if data.board[x][y] == "-":
        data.board[x][y] = "0"
        print("Sorry, you missed")
        guesses.append(pair)
        shots -= 1
    elif data.board[x][y] == "@":
        data.board[x][y] = "X"
        guesses.append(pair)
        print("That's a HIT")
    else:
        print("Sorry, you already shot here! Try again!")
       

def user_shots_two(data, x, y):
    """
    Function record user shots, and check against board
    reduce the number of shots after each round
    and ships after each hit
    """
    global num_ships
    global shots
    pair = (x, y)

    if pair in guesses:
        print("shoot again")
    else:
        if pair not in user_ship:
            data.board[x][y] = "0"
            print("miss\n")
            guesses.append(pair)
            shots -= 1
            return False
    
        else:
            data.board[x][y] = "X"
            print("Hit\n")
            guesses.append(pair)
            num_ships -= 1
            shots -= 1
            return False


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
            data.board[x][y] = "@" 
            pair = (x, y)
            # data.append(pair)
            computer_ships.append(pair)
        else:
            continue
        b += 1


# -------------------------------------------------------
# Test area
# print("*" * 40)


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
user_board = GameBoard(size)
user_board.print_board()

while len(user_ship) < num_ships:
    z = player_choose_ships()
    x = return_x_value(z)
    y = return_y_value(z)
    user_ship_location(user_board, x, y)
    user_board.print_board()
    print(f"You have placed {len(user_ship)} ship/s.")
print("Great, now it is time to play a game.\n")

while shots > 0:
    z = player_choose_ships()
    x = return_x_value(z)
    y = return_y_value(z)
    user_shots_two(user_board, x, y)
    user_board.print_board()
    print(f"You have {shots} shots left.")
else:
    print("Game Over")


print(len(guesses))
print(num_ships)
print(user_ship)
print(guesses)
print(shots)
# -------------------------------------
# game trial function
# def game_set():
    
#     computer_board.print_board()
#     random_ship_location(computer_board)
    # computer_board.print_board()


# def play_game():
    
    # random_ship_shot(computer_board)
    # computer_board.print_board()


# def main():

#     global num_ships
    # intro()
    # game_set()
    # b = 0
    # while b < 100 and num_ships > 0:
    #     play_game()
    #     print(num_ships)
    #     b += 1
    # else:
    #     print("Game Over")

# main()
# -------------------------------------------------------
