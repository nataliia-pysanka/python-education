"""
Module for the controller classes
"""
from util import NoMenuItem


class Controller:
    """
    Class controller for the session of the game
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_board(self):
        """
        Method shows model via view
        :return:
        """
        self.view.show_board(self.model)

    def make_motion(self, index, sign):
        """
        Method calls model and changes value of the cell
        :param index:
        :param sign:
        :return:
        """
        self.model[index] = sign

    def check_motion(self, motion, sign):
        """
        Function checks if the cell in the line with similar signs
        :param motion: int
        :param sign: str
        :return: bool
        """
        rng = range(-(self.model.count - 1), self.model.count)

        cell = 1
        h_slice = []
        for _ in range(1, self.model.size + 1):
            if motion in range(cell, cell + self.model.size):
                h_slice.extend(range(cell, cell + self.model.size))
                break
            cell += self.model.size

        h_lst = [cell for cell in rng if motion + cell in h_slice]
        v_lst = [self.model.size * cell for cell in rng
                 if (motion + self.model.size * cell)
                 in range(1, self.model.size ** 2 + 1)]
        dr_lst = [(self.model.size + 1) * cell for cell in rng]
        dl_lst = [(self.model.size - 1) * cell for cell in rng
                 if (motion + (self.model.size - 1) * cell) >= self.model.size]

        index_lst = [h_lst, v_lst, dr_lst, dl_lst]
        for lst in index_lst:
            win = 0
            for index in lst:
                if self.model[motion + index] == sign:
                    win += 1
                if win == 3:
                    return True
        return False


class GameController:
    """
    Class controller for the game menu
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def choose_menu(self, text):
        """
        Method displays game menu via view and returns item of the menu
        :param text: str
        :return: int
        """
        menu = ['Menu:']
        for key, value in self.model.menu.items():
            menu.append(f' {key} - {value}')
        self.view.show_lines(menu)
        while True:
            try:
                item = input(text)
                self.model.is_valid_item(item)
            except NoMenuItem:
                continue
            return item

    def show_lines(self, lines):
        """
        Method calls view to display list of data
        :param lines:
        :return:
        """
        self.view.show_lines(lines)
