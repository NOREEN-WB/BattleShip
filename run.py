"""BattleShip"""
from random import randint
scores = {"computer": 0, "player": 0}


class Board:
    """Board Class"""
    def __init__(self, size, player_name, typee, num_ships):
        self.size = size
        self.num_ships = num_ships
        self.player_name = player_name
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.typee = typee
        self.ships = []
        self.guesses = []

    def battle_board(self):
        """spacing between dot's"""
        for row in self.board:
            print(" ".join(row))

    def add_ship(self, _x, _y):
        """
        Adding Ship
        """
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((_x, _y))
            if self.typee == "player":
                self.board[_x][_y] = "@"

    def guess(self, _x, _y):
        """guessing th number"""
        self.guesses.append((_x, _y))
        self.board[_x][_y] = "X"

        if(_x, _y) in self.ships:
            self.board[_x][_y] = "*"
            return "Hit"
        else:
            return "Miss"


def random_point(size):
    """random point"""
    return randint(0, size-1)


def populate_board(board):
    """populating the board"""
    if board.player_name != "computer":
        print(f"{board.player_name}'s board:")
        while True:
            # player_board = [["." for x in range(size)] for y in range(size)]
            _x = random_point(board.size)
            _y = random_point(board.size)
            if(_x, _y) in board.ships:
                print("")
            else:
                board.add_ship(_x, _y)
                if len(board.ships) == 4:
                    break
        print("\n")
        board.battle_board()
    else:
        print(f"\n{board.player_name}'s board")
        for _ in range(board.num_ships):
            _x = random_point(board.size)
            _y = random_point(board.size)
            board.add_ship(_x, _y)
        board.battle_board()


def validate_coordinates(_x, _y, board):
    """Validating coordinates"""
    try:
        if _x in range(board.size) and _y in range(board.size):
            return True
        else:
            raise ValueError(
                f"Value Must be between 0 and {board.size}"
            )
    except ValueError as _e:
        print(f"Invalid data: {_e}, please try again\n")
        return False


def play_game(player_board, computer_board):
    """playing game"""
    while True:
        try:
            _x = int(input('Enter X Coordinate:\n '))
            _y = int(input('Enter Y Coordinate:\n '))
        except ValueError:
            print('Not a number')
        else:
            if (_x, _y) in computer_board.guesses:
                print("You connot hit a coordinate twice")
            else:
                if validate_coordinates(_x, _y, computer_board):
                    print(f"player guessed: ({_x},{_y})")
                    player_guess = computer_board.guess(_x, _y)
                    if player_guess == "Hit":
                        print("player Hit a ship")
                        scores["player"] += 1
                    else:
                        print("player missed this time")
                    while True:
                        _x = random_point(computer_board.size)
                        _y = random_point(computer_board.size)
                        if (_x, _y) not in player_board.guesses:
                            if validate_coordinates(_x, _y, player_board):
                                print(f"computer guessed: ({_x},{_y})")
                                computer_guess = player_board.guess(_x, _y)
                                if computer_guess == "Hit":
                                    print("computer Hit a ship")
                                    scores["computer"] += 1
                                    break
                                else:
                                    print("computer missed this time")
                                    break
                    print("-" * 35)
                    print("After this round, the scores are:")
                    print(
                        player_board.player_name, ": ",
                        scores["player"], "computer: ", scores["computer"])
                    print("-" * 35)
                    if scores["player"] == computer_board.num_ships:
                        print(f"{player_board.player_name} Won\n")
                        computer_board.battle_board()
                        new_game()
                    if scores["computer"] == player_board.num_ships:
                        print("Computer Won\n")
                        player_board.battle_board()
                        new_game()
                    inputt = input("enter any key to continue or n to quit: \n")
                    if inputt == "n":
                        new_game()
                    else:
                        print(f"\n{player_board.player_name}'s board: ")
                        player_board.battle_board()
                        print("computer's board: ")
                        computer_board.battle_board()
                        print("\n")



def new_game():
    """
    Initilising battleship game
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(" Welcome to ULTIMATE BATTLESHIPS!!")
    print(" Board Size: 5. Number of ships: 4")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    player_board = Board(size, player_name, "player", num_ships)
    computer_board = Board(size, "computer", "computer", num_ships)

    populate_board(player_board)
    populate_board(computer_board)

    play_game(player_board, computer_board)
new_game()
