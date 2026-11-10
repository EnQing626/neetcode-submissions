# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traversal(root1:TreeNode,root2:TreeNode):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val!=root2.val:
                return False
            left_part=traversal(root1.left,root2.left)
            right_part=traversal(root1.right,root2.right)
            issame=left_part and right_part
            return issame
        result=traversal(p,q)
        return result