# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        if not root:
            return ""
        from collections import deque
        que=deque([root])
        while que:
            size=len(que)
            for i in range(size):
                cur=que.popleft()
                if cur:
                    res.append(str(cur.val))
                    que.append(cur.left)
                    que.append(cur.right)
                else:
                    res.append('null')
        return '['+','.join(res)+']'
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        datalist=data[1:-1].split(',')
        root=TreeNode(int(datalist[0]))
        from collections import deque
        que=deque([root])
        i=1
        while que:
            cur=que.popleft()
            if datalist[i]!='null':
                cur.left=TreeNode(int(datalist[i]))
                que.append(cur.left)
            i+=1
            if datalist[i]!='null':
                cur.right=TreeNode(int(datalist[i]))
                que.append(cur.right)
            i+=1
        return root

