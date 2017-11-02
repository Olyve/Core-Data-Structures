#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return

    if array[index] == item:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left_index = 0
    right_index = len(array) - 1
    current_index = 0

    while left_index <= right_index:
        # Check if left or right index is item we want
        if array[left_index] == item:
            return left_index
        elif array[right_index] == item:
            return right_index

        # Get middle index and cast to int to remove floating points
        current_index = int((left_index + right_index) / 2)
        current_item = array[current_index]

        if current_item == item:
            return current_index
        elif item < current_item:
            right_index = current_index
            left_index += 1
        elif item > current_item:
            left_index = current_index
            right_index -= 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left == None and right == None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None
    elif array[left] == item:
        return left
    elif array[right] == item:
        return right

    current_index = int((left + right) / 2)
    current_item = array[current_index]
    
    if current_item == item:
        return current_index
    elif item < current_item:
        return binary_search_recursive(array, item, left + 1, current_index)
    elif item > current_item:
        return binary_search_recursive(array, item, current_index, right - 1)
