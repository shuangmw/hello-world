# Print Diamond
def print_diamond(n):
    for i in range(1,n+1):
        print ' '*(n-i), '*'*(2*i-1)
    for i in range(n-1,0,-1):
        print ' '*(n-i), '*'*(2*i-1)


# Reconstruct Binary Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        # 找到中序队列中根节点的下标
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i + 1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root

sl = Solution()
result = sl.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
result.left.left.right.val


# Fibonacci
# Solution 1: Recursion
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number-1) + self.jumpFloor(number-2)
# Solution 2: loop
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            t1, t2 = 1, 2
            i = 3
            while(i<=number):
                total = t1+t2
                t1 = t2
                t2 = total
                i += 1
            return total


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


# String Permutation
def permutation(a):
    if not a:
        return []
    if len(a) == 1:
        return [a]
    result = []
    for i in range(len(a)):
        for j in permutation(a[:i] + a[i+1:]):
            result.append(a[i] + j)
    return result
