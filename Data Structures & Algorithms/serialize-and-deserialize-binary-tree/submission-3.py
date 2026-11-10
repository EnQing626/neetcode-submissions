# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        results = []
        if not root:
            return ""

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            #result = []
            for _ in range(size):
                cur = que.popleft()
                if cur:
                    results.append(str(cur.val))
                    que.append(cur.left)
                    que.append(cur.right)
                else:
                    results.append('None')
                #if cur.left:
                #    que.append(cur.left)
                #if cur.right:
                #    que.append(cur.right)
            #results.append(result)

        return '[' + ','.join(results) + ']'
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        dataList = data[1:-1].split(',')
        root = TreeNode(int(dataList[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                queue.append(node.right)
            i += 1
        return root