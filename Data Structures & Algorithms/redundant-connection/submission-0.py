class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # 初始化并查集

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # 路径压缩
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

    def is_same(self, u, v):
        return self.find(u) == self.find(v)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        un = UnionFind(len(edges)+1)
        for u,v in edges:
            if un.is_same(u,v):
                return [u,v]
            un.union(u,v)