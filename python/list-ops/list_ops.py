def append(list1, list2):
    """
    Appends two lists using list concatenation.

    This function creates a new list by concatenating list1 and list2.
    It does not modify the original lists.

    Args:
    - list1 (list): The first list to be concatenated.
    - list2 (list): The second list to be concatenated.

    Returns:
    - list: A new list containing all elements of list1 followed by all elements of list2.
    """
    return list1 + list2


def concat(lists):
    """
    Recursively concatenate a series of lists into one flattened list.

    Args:
    - lists: A list of lists to be concatenated.

    Returns:
    - A new list containing all elements from the input lists, in order.
    """
    if not lists:
        return []
    return lists[0] + concat(lists[1:])


def filter(function, lst):
    """
    Filter a list based on a predicate function.

    Args:
    - function: A function that returns True for items to keep.
    - lst: The input list to filter.

    Returns:
    - A new list containing only the items for which the predicate returns True.
    """
    return [item for item in lst if function(item)]


def length(lst):
    """
    Recursively calculate the number of items in a list.

    Args:
    - lst: The list to count.

    Returns:
    - int: The number of elements in the list.
    """
    if not lst:
        return 0
    return 1 + length(lst[1:])


def map(func, lst):
    """
    Recursively apply a function to each element of a list and return the list of results.

    Args:
    - func (callable): A function that takes a single element of the list and returns a result.
                       The function should be pure, meaning no side effects, as this implementation
                       assumes only transformations are applied to elements.
    - lst (list): The list to map over. The list can be empty or contain any type of elements
                  compatible with the function.

    Returns:
    - list: A new list of results after applying `func` to each element in `lst`. If `lst` is empty, an empty list is returned.
    """
    if not lst:
        return []
    return [func(lst[0])] + map(func, lst[1:])


def foldl(function, list, accumulator):
    """
    Recursively reduces a list from left to right using a given function and an initial accumulator.

    Args:
    - function: A function that takes the current accumulator and an item, and returns the new accumulator value.
    - list: The list to be reduced.
    - accumulator: The initial value for the accumulator.

    Returns:
    - The final accumulator value after applying the function to each item from left to right.
    """
    if not list:
        return accumulator
    else:
        return foldl(function, list[1:], function(accumulator, list[0]))

def foldr(function, list, accumulator):
    """
    Reduces a list from right to left using a given function and an initial accumulator.

    Args:
    - function: A function that takes the current accumulator and an item, and returns the new accumulator value.
    - list: The list to be reduced.
    - accumulator: The initial value for the accumulator.

    Returns:
    - The final accumulator value after applying the function to each item from right to left.
    """
    for item in reversed(list):
            accumulator = function(accumulator, item)
    return accumulator


def reverse(lst):
    """
    Recursively reverse the order of elements in a list.

    Args:
    - The list to reverse.

    Returns:
    - A new list with the elements of lst in reversed order.
    """
    if not lst:
        return []
    return reverse(lst[1:]) + [lst[0]]
