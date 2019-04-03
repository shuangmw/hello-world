def binary_search_first(array, key):
    """e.g. find 5 in [4,5], returns 1. Note that mid is closer to left"""

    if not array:
        return -1

    left = 0
    right = len(array) - 1
    while left < right:
        mid = left + (right-left)//2
        if array[mid] < key:
            left = mid + 1
        elif array[mid] > key:
            right = mid - 1
        else:
            right = mid  # array stops to reduce when only 1 item left.
                         # use '<' to avoid endless loop.

    if array[left] == key:
        return left
    else:
        return -1 


if __name__ == '__main__':
    array = [5,6]
    key = 6
    result = binary_search_first(array, key)
    print result
