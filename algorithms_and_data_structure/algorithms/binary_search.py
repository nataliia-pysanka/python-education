"""
Binary search algorithm
"""


# def binary_search(sorted_lst, find_item):
#     """
#     Searchs the item in the sorted list and returns it or None
#     :param sorted_lst: [int or float]
#     :param find_item: int or float
#     :return: int or float or None
#     """
#     if len(sorted_lst) == 0 or \
#             not isinstance(sorted_lst[0], (int, float)) or \
#             not isinstance(find_item, (int, float)):
#         return None
#     lst = sorted_lst
#     start = 0
#     finish = len(lst) - 1
#     middle = int(len(lst) / 2)
#     if find_item == lst[middle]:
#         return lst[middle]
#     if finish == start:
#         return None
#     if find_item > lst[middle]:
#         new_lst = lst[middle:]
#         return binary_search(new_lst, find_item)
#     new_lst = lst[: middle]
#     return binary_search(new_lst, find_item)

def binary_search(lst, find_item):
    """
    Searches the item in the sorted list and returns it or None
    :param lst: [int or float]
    :param find_item: int or float
    :return: int or float or None
    """
    if len(lst) == 0 or \
            not isinstance(lst[0], (int, float)) or \
            not isinstance(find_item, (int, float)):
        return None
    if find_item > lst[-1] or find_item < lst[0]:
        return None
    start = 0
    finish = len(lst) - 1
    while start <= finish:
        middle = int((start + finish) / 2)
        item = lst[middle]
        if find_item <= item:
            finish = middle - 1
            continue
        if find_item > item:
            start = middle + 1
            continue
    if find_item == lst[start]:
        return start
    return None
