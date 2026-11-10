class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # 路径压缩
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_y] = root_x

        for u, v in edges:
            union(u, v)

        # 统计独立集合的个数
        return len(set(find(x) for x in range(n)))