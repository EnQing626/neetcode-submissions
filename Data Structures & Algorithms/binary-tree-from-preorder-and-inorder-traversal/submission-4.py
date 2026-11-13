# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. 用哈希表记录 inorder 中每个值对应的索引，O(1) 查找
        in_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            # 递归终止条件
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # 前序遍历的第一个元素就是当前子树的根节点
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # 在哈希表中 O(1) 找到根节点在中序遍历中的位置
            root_index = in_map[root_val]
            # 计算左子树的节点数量
            left_size = root_index - in_start
            
            # 递归构建左子树和右子树（通过传递边界索引替代切片）
            root.left = helper(
                pre_start + 1, 
                pre_start + left_size, 
                in_start, 
                root_index - 1
            )
            root.right = helper(
                pre_start + left_size + 1, 
                pre_end, 
                root_index + 1, 
                in_end
            )
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)