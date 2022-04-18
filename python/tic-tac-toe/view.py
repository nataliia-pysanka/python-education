"""
Module with view classes for Tic Tac Toe game
"""
from abc import ABC, abstractmethod


class View(ABC):
    """
    Abstract class for viewing
    """
    @abstractmethod
    def show_board(self, board):
        """
        Function shows the play board on the terminal
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def show_lines(self, lines):
        """
        Function shows the list of strings in the terminal
        :return:
        """
        raise NotImplementedError


class Terminal(View):
    """
    Class for viewing information about game in the terminal
    """
    def show_lines(self, lines):
        for line in lines:
            print(line)

    def show_board(self, board):
        lst = ['╔' + ('═' * 6 + '╦') * (board.size - 1) + '═' * 6 + '╗']
        count = 0
        st_line = ''
        for cell in board.board:
            count += 1
            st_line += f'║ {str(board.board[cell]).rjust(3)}  '
            if count % board.size == 0:
                lst.append(st_line + '║')
                if count < len(board.board):
                    lst.append(
                        '╠' + ('═' * 6 + '╬') * (
                                board.size - 1) + '═' * 6 + '╣'
                    )
                else:
                    lst.append(
                        '╚' + ('═' * 6 + '╩') * (
                                board.size - 1) + '═' * 6 + '╝'
                    )
                st_line = ''
        for item in lst:
            print(item)
