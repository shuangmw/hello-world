def binary_search_first(array, key):
    if not array:
        return -1
    
    left = 0
    right = len(array) - 1
    while left < right:
        mid = left + (right-left)//2
        if array[mid] < key:
            left = mid + 1
        else:
            right = mid

    if array[left] == key:
        return left
    else:
        return -1 


if __name__ == '__main__':
    array = [-1,1,3,6,6,7,10]
    key = 6
    result = binary_search_first(array, key)
    print result
