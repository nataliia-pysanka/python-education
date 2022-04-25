"""
Module with models for game Tic Tac Toe
"""
from abc import ABC, abstractmethod
from util import NoMenuItem


class Board:
    """
    Class is a  game board.
    It initializes board of size from 3 to 15 like a dictionary where each cell
    had unique number and value ""; returns the value of cell (""/"O"/"X") and
    sets the value
    """
    def __init__(self, size=3, count=3):
        self.size = size if size in range(3, 16) else 3
        self.count = count if count <= self.size else 3
        self.board = {x: '' for x in range(1, self.size ** 2 + 1)}

    def __repr__(self):
        return 'Tic-Tac-Toe game'

    def __getitem__(self, item):
        if item in range(1, self.size ** 2 + 1):
            return self.board[item]
        return None

    def __setitem__(self, item, value):
        if item in self.board:
            self.board.update({item: value})
        else:
            raise IndexError


class TicTacToe:
    """
    Class is a game Tic Tac Toe. Get menu and checks is the input item valid
    """
    MENU = {
          '1': 'play',
          '2': 'look the log',
          '3': 'clear the log',
          '4': 'escape'
    }

    @property
    def menu(self):
        """
        Property returns menu
        :return:
        """
        return TicTacToe.MENU

    def is_valid_item(self, index):
        """
        Method checks if the index in the menu
        :param index: str
        :return: bool
        """
        if index in self.MENU:
            return True
        raise NoMenuItem(print('No item in menu'))


class Player(ABC):
    """
    Class-creator for player. Initializes player with name and sign;
    works with the motions, remembers the whole motions and wins
    """
    motions = []

    def __init__(self, name, sign):
        Player.motions = []
        self.name = name
        self.sign = sign
        self.wins = 0

    @abstractmethod
    def motion(self, size):
        """
        Function returns the motion of player
        :return:
        """

    @staticmethod
    def clear():
        """
        Function clears the list of motions for new game
        :return:
        """
        Player.motions = []


class Human(Player):
    """
    Class for human-player. Returns the motion of player
    """
    def __str__(self):
        return self.name

    def motion(self, size):
        """Function returns the cell number of the board"""
        index_num = size ** 2
        while True:
            print(f'Motions: {Player.motions}')
            motion = input(f'Player "{self}" input number of cell [1:'
                           f'{index_num}] >> ')
            try:
                motion = int(motion)
            except ValueError:
                continue
            if motion < 1 or motion > index_num or motion in Player.motions:
                continue
            Player.motions.append(motion)
            return int(motion)
