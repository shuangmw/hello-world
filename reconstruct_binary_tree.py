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
