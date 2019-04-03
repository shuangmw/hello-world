def binary_search_last(array, key):
    """e.g. find 5 in [5,5], returns 1."""

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
        # Note that mid is closer to left.
        # length of 1 or 2 both cause endless loop, if use 'left=mid' here.
        else:
            if left == mid:  # case when 2 items left
                if array[right] == key:
                    return right
                else:
                    return left
            else:
                left = mid

    # case when 1 item left
    if array[left] == key:
        return left
    else:
        return -1 


if __name__ == '__main__':
    array = [5,6,6,7]
    key = 6
    result = binary_search_last(array, key)
    print result
