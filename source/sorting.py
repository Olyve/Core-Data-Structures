#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    # Check that all adjacent items are in order, return early if not
    if len(items) <= 1:
        return True
        
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    while not is_sorted(items):
        # Swap adjacent items that are out of order
        for index in range(len(items) - 1):
            next_index = index + 1
            if items[index] > items[next_index]:
                items[index], items[next_index] = items[next_index], items[index]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) always have to merge the items by going through
    at least the majority of the items
    Memory usage: O(2n) Original list of items unsorted + new sorted list"""
    # Create two indexes to track position in lists
    left_index = 0 
    right_index = 0

    # Track len of both lists
    left_len = len(items1)
    right_len = len(items2)

    # Create list to hold final sorted items
    merged = []

    # Repeat until we reach the end of one of the lists
    while left_index < left_len  and right_index < right_len:
        # Store values for convenience
        left = items1[left_index]
        right = items2[right_index]

        # Compare and append the smaller of the two to merged
        if left < right:
            merged.append(left)
            left_index += 1
        elif left == right:
            merged.append(left)
            merged.append(right)
            left_index += 1
            right_index += 1
        elif right < left:
            merged.append(right)
            right_index += 1

    # Append remaining items of "non-empty" list to merged
    if left_index == left_len:
        merged.extend(items2[right_index:])
    elif right_index == right_len:
        merged.extend(items1[left_index:])

    # Return the final merged list
    return merged


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(2n^2 + n)
    Memory usage: O(2n)"""
    # Split items list into approximately equal halves
    middle_index = int(len(items) / 2)
    left = items[:middle_index]
    right = items[middle_index:]

    # Sort each half using any other sorting algorithm
    bubble_sort(left)   # O(n^2)
    bubble_sort(right)  # O(n^2)

    # Merge sorted halves into one list in sorted order
    items[:] = merge(left, right)   # O(n)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n)
    Memory usage: ??? """
    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return items

    # Split items list into approximately equal halves
    middle_index = int(len(items) / 2)
    left = items[:middle_index]
    right = items[middle_index:]

    # Sort each half by recursively calling merge sort
    merge_sort(left)    # O(log n)
    merge_sort(right)   # O(log n)

    # Merge sorted halves into one list in sorted order
    items[:] = merge(left, right)   # O(2n)


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    import time

    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    # Only print out smaller lists
    if len(items) <= 1000:
        print('Initial items: {!r}'.format(items))
        print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    # print('Sorting items with {}(items)'.format(sort.__name__))
    start = time.time()
    print('Sorting items using {}...'.format(sort.__name__))
    sort(items)
    if len(items) <= 1000:
        print('Sorted items:  {!r}'.format(items))
        print('Sorted order?  {!r}'.format(is_sorted(items)))
    print('Time to sort: {} seconds'.format(time.time() - start))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
