# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result=[]
        def traversal(root):
            if not root:
                return None
            traversal(root.left)
            result.append(root.val)
            traversal(root.right)
        traversal(root)
        for i in range(1,len(result)):
            if result[i]<=result[i-1]:
                return False
        return True