def binary_search_last_less(array, key):
    """e.g. for key 5 in [4,6], returns 0."""

    if not array:
        return -1
    left = 0
    right = len(array) - 1
    while left < right:
        mid = left + (right-left)//2
        if array[mid] >= key:
            right = mid - 1
        else:
            # length of 1 or 2 would case endless loop.
            # process seperately.
            if left == mid:  # case when 2 items left
                if array[right] < key:
                    return right
                else:
                    return left
            else:
                left = mid

    # case when 1 item left
    if array[left] < key:
        return left
    else:
        return -1

if __name__ == "__main__":
    array = [4,5,6]
    key = 3
    result = binary_search_last_less(array, key)
    
    print result
