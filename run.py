"""BattleShip"""
from random import randint
scores = {"computer": 0, "player": 0}


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
