# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        def traversal(root):
            nonlocal maxSum
            if not root:
                return 0
            left_num=max(traversal(root.left),0)
            right_num=max(traversal(root.right),0)
            maxSum=max(maxSum,left_num+right_num+root.val)
            return max(left_num,right_num)+root.val
        traversal(root)
        return maxSum