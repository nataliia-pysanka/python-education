"""
Module for utilities
"""
import logging.config
import logging
import os

logging.config.fileConfig("log.ini")
game_logger = logging.getLogger('gameLogger')
session_logger = logging.getLogger('sessionLogger')


class NoMenuItem(Exception):
    """
    Custom class for exception
    """
    def __init__(self, text):
        super().__init__(self)
        self.txt = text


class Session:
    """
    Class creates session for two players and logs the information about
    session into the logfile
    """

    def __init__(self, players):
        self.x_player, self.y_player = players

    def __enter__(self):
        players_log(self.x_player, self.y_player)
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        end_session_log(self.x_player.wins, self.y_player.wins)

    def winner_log(self, player):
        """
        Methods writes the name of game winner to the log-file
        :param player:
        :return:
        """
        game_logger.info('The winner is player "%s"', player)

    def no_winner_log(self):
        """
        Method writes to the log-file "There is no winner!"
        :return:
        """
        game_logger.info("There is no winner!")


def cls():
    """
    Clear terminal screen
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def players_log(x_player, y_player):
    """
    Methods writes the names of players in new session to the log-file
    :param x_player:
    :param y_player:
    :return:
    """
    game_logger.info('The players are: "%s" and "%s"', x_player, y_player)


def end_session_log(x_player_wins, y_player_wins):
    """
    Method writes the score of the session to the log-file
    :param x_player_wins: int
    :param y_player_wins: int
    :return:
    """
    session_logger.info('The result of session is %s:%s',
                        x_player_wins, y_player_wins)
