# Quick Sort
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right-1
    key = array[right]
    while left < right:
        while left < right and array[left] <= key:
            left += 1
        while left < right and array[right] > key:
            right -= 1
        array[left], array[right] = array[right], array[left]
    array[left], key = key, array[left]
    quick_sort(array, low, left-1)
    quick_sort(array, left+1, high)
