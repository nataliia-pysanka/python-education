"""
Tests for time_of_day() method
"""
from datetime import datetime
from unittest.mock import Mock
import pytest


def time_of_day():
    """Identifies current time of day.
    Returns:
        str: current time of day. Could be: "night", "morning", "afternoon".
    """
    now = datetime.now()
    if now.hour >= 0 and now.hour < 6:
        return "night"
    if now.hour >= 6 and now.hour < 12:
        return "morning"
    if now.hour >= 12 and now.hour < 18:
        return "afternoon"
    return "night"


night = datetime(year=2022, month=4, day=26, hour=0, minute=0, second=18)
morning = datetime(year=2022, month=4, day=26, hour=11, minute=59, second=59)
afternoon = datetime(year=2022, month=4, day=26, hour=13, minute=0, second=1)
evening = datetime(year=2022, month=4, day=26, hour=18, minute=0, second=0)

datetime = Mock()


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
