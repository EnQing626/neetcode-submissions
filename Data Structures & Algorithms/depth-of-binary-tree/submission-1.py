# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result=0
        def traversal(root):
            nonlocal result
            if not root:
                return 0
            left_part=traversal(root.left)
            right_part=traversal(root.right)
            result=max(left_part,right_part)+1
            return result
        traversal(root)
        return result