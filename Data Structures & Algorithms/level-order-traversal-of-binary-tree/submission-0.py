# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results=[]
        if not root:
            return results
        from collections import deque
        que = deque([root])
        while que:
            size=len(que)
            result=[]
            for i in range(size):
                cur_node=que.popleft()
                result.append(cur_node.val)
                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)
            results.append(result)
        return results