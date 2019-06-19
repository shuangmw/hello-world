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

def quickSort(nums, low, high):

    def partition(nums, low, high):
        i = low - 1
        pivot = nums[high]

        for j in range(low, high):
            if nums[j] <= pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i + 1

    if low < high:
        pi = partition(nums, low, high)

        quickSort(nums, low, pi-1)
        quickSort(nums, pi+1, high)


a = [3,5,8,1,2,9,4,7,6]
print a
quickSort(a, 0, 8)
print a
