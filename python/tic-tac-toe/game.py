"""
Module __main__
"""
import random
from model import TicTacToe, Board, Player, Human
from controller import Controller, GameController
from view import Terminal
from util import Session, cls

LOG_FILE = 'tic-tac-toe.log'
SIGN = ('X', "O")


def play_session(player):
    """
    Function creates a new board for the game session, takes the motion from
    the player and transfers it to the board
    :param player:
    :return: object Player
    """
    board = Board(size=3)
    board_view = Terminal()
    board_controller = Controller(board, board_view)
    move = bool(random.choice([0, 1]))
    while True:
        print(f'Player "{player[move]}" moves with {SIGN[move]}-sign')
        board_controller.show_board()
        motion = player[move].motion(board.size)
        board_controller.make_motion(motion, SIGN[move])

        if board_controller.check_motion(motion, SIGN[move]):
            board_controller.show_board()
            return player[move]
        move = not move
        if len(Player.motions) == board.size ** 2:
            return None


def play():
    """
    Function creates players and starts new game session for them
    :return:
    """
    cls()
    player = (Human(input("Input name for X player >> "), SIGN[0]),
              Human(input("Input name for O player >> "), SIGN[1]))
    with Session(player) as session:
        while True:
            winner = play_session(player)
            if winner:
                winner.wins += 1
                print(f'Winner is {winner}')
                session.winner_log(winner)
            else:
                session.no_winner_log()
            item = input("Do you want to play again (y/n) >> ")
            if item == 'y':
                Player.clear()
                continue
            if item == 'n':
                return True
            break
    return True


def look_log():
    """
    Function prints the log-file to the screen
    :return: True
    """
    cls()
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        log = file.readlines()
        if not log:
            log.append("The log file is empty")
        log.append("Press Enter to back in the menu >> ")
        game_controller.show_lines(log)
        input()
        return True


def clear_log():
    """
    Function clears the log-file
    :return: True
    """
    cls()
    with open(LOG_FILE, 'w', encoding='utf-8') as _:
        msg = ["The log file was cleared",
               "Press Enter to back in the menu >> "]
        game_controller.show_lines(msg)
        input()
        return True


def escape():
    """
    Function makes escape from game
    :return: False
    """
    return False


def get_menu(item):
    """
    Return the name of function for chosen menu item
    :param item:
    :return: func
    """
    if item == '1':
        return play
    if item == '2':
        return look_log
    if item == '3':
        return clear_log
    if item == '4':
        return escape
    return other


def other():
    """
    Back to the main menu if user input non-menu item
    :return: True
    """
    return True


def main():
    """
    Main function calls the controller methods for chosen menu item
    :return: func()
    """
    cls()
    item = game_controller.choose_menu('Choose your motion >> ')
    motion = get_menu(item)
    return motion()


if __name__ == '__main__':
    game = TicTacToe()
    game_view = Terminal()
    game_controller = GameController(game, game_view)
    cls()
    ON_GAME = True
    while ON_GAME:
        ON_GAME = main()
