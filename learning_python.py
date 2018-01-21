# 打印菱形
def print_diamond(n):
    for i in range(1,n+1):
        print ' '*(n-i), '*'*(2*i-1)
    for i in range(n-1,0,-1):
        print ' '*(n-i), '*'*(2*i-1)


# 替换空格
def replaceSpace(s):
    temp = ''
    if type(s) != str:
        return
    for i in s:
        if i == ' ':
            temp += '%20'
        else:
            temp += i
    return temp


# 重建二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root

sl = Solution() 
result = sl.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
result.left.left.right.val


# 两个栈实现一个队列
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
         
    def push(self, node):
        # write code here
        self.stackA.append(node)
         
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
        
        
# 跳台阶

# 递归
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number-1) + self.jumpFloor(number-2)
        
# 迭代
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
