# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def goodNodes_(self, root: TreeNode, mx=-inf) -> int:
        if root is None:
            return 0
        # 👈 确保这里调用的是 goodNodes_ 
        left = self.goodNodes_(root.left, max(mx, root.val))
        right = self.goodNodes_(root.right, max(mx, root.val))
        return left + right + (mx <= root.val)
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodes_(root)
