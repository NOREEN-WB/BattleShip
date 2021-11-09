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
