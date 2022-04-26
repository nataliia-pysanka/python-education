from datetime import datetime


def even_odd(x):
    """Checks number if it even or odd.

    Args:
        x (int): number to check.

    Returns:
        str: result of check. `even` if given number is even
            and `odd` if the number is odd.
    """
    if (x % 2 == 0):
        return "even"
    else:
        return "odd"


def sum_all(*numbers):
    """Sums all given numbers together.

    Args:
        *args (int or float): variable length argument list.


    Returns:
        int or float: the result of adding all numbers together.
    """
    result = 0
    for num in numbers:
        result += num
    return result


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
