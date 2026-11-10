class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # 路径压缩
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False  # 成环了
            parent[root_x] = root_y
            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return True