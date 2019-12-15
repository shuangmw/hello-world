# Quick Sort

# BUG
# def quick_sort(array, left, right):
#     if left >= right:
#         return
#     low = left
#     high = right-1
#     key = array[right]
#     while left < right:
#         while left < right and array[left] <= key:
#             left += 1
#         while left < right and array[right] > key:
#             right -= 1
#         array[left], array[right] = array[right], array[left]
#     array[left], key = key, array[left]
#     quick_sort(array, low, left-1)
#     quick_sort(array, left+1, high)

def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo  # nums left of i should be smaller than pivot,
            # so that could be swapped with pivot.
    
    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
    
    nums[i], nums[hi] = nums[hi], nums[i]
    return i


def quickSort(nums, lo, hi):
    if lo < hi:
        pi =  partition(nums, lo, hi)
    
        quickSort(nums, lo, pi-1)
        quickSort(nums, pi+1, hi)


a = [3,5,8,1,2,9,4,7,6]
print a
quickSort(a, 0, 8)
print a
