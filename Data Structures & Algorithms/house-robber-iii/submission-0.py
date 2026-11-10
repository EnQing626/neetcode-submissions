# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traversal(root:TreeNode):
            if not root:
                return (0,0)
            left_node=traversal(root.left)
            right_node=traversal(root.right)
            #butou
            root_norob=max(left_node[0],left_node[1])+max(right_node[0],right_node[1])
            #tou
            root_rob=left_node[0]+right_node[0]+root.val
            return (root_norob,root_rob)
        dp=traversal(root)
        return max(dp)