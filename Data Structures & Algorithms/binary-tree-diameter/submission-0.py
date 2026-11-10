# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def traversal(root):
            nonlocal res
            if not root:
                return 0
            left_num=traversal(root.left)
            right_num=traversal(root.right)
            res=max(res,left_num+right_num)
            return max(left_num,right_num)+1
        traversal(root)
        return res