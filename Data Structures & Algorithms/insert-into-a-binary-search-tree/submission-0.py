# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        pre=None
        cur=root
        while cur:
            if val>cur.val:
                pre=cur
                cur=cur.right
            elif val<cur.val:
                pre=cur
                cur=cur.left
        if val>pre.val:
            pre.right=TreeNode(val)
        else:
            pre.left=TreeNode(val)
        return root