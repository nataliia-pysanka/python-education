"""
Tests for time_of_day() method
"""
from datetime import datetime
from unittest.mock import Mock
from functions import time_of_day


night = datetime(year=2022, month=4, day=26, hour=0, minute=0, second=18)
morning = datetime(year=2022, month=4, day=26, hour=11, minute=59, second=59)
afternoon = datetime(year=2022, month=4, day=26, hour=13, minute=0, second=1)
evening = datetime(year=2022, month=4, day=26, hour=18, minute=0, second=0)

datetime = Mock()
# def test_time_of_day_raises_exception_on_arg():
#     """
#     Inputs non integer argument to the method
#     """
#     with pytest.raises(TypeError):
#         time_of_day('test')


def test_time_of_day_night():
    """
    Inputs time 00:00:18
    """
    datetime.now.return_value = night
    assert time_of_day() == "night"


def test_time_of_day_morning():
    """
    Inputs time 11:59:59
    """
    datetime.now.return_value = morning
    assert time_of_day() == "morning"


def test_time_of_day_afternoon():
    """
    Inputs time 13:00:01
    """
    datetime.now.return_value = afternoon
    assert time_of_day() == "afternoon"


def test_time_of_day_not_night():
    """
    Inputs time 18:00:00
    """
    datetime.now.return_value = evening
    assert time_of_day() == "night"
