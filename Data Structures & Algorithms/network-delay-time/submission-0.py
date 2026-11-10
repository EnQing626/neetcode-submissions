class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 初始化邻接矩阵
        grid = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        for p1, p2, val in times:
            grid[p1][p2] = val

        # 初始化距离数组和访问数组
        minDist = [float('inf')] * (n + 1)
        visited = [False] * (n + 1)

        minDist[k] = 0  # 起始点到自身的距离为0

        for _ in range(1, n + 1):  # 遍历所有节点
            minVal = float('inf')
            cur = -1

            # 选择距离源点最近且未访问过的节点
            for v in range(1, n + 1):
                if not visited[v] and minDist[v] < minVal:
                    minVal = minDist[v]
                    cur = v

            if cur == -1:  # 如果找不到未访问过的节点，提前结束
                break

            visited[cur] = True  # 标记该节点已被访问

            # 更新未访问节点到源点的距离
            for v in range(1, n + 1):
                if not visited[v] and grid[cur][v] != float('inf') and minDist[cur] + grid[cur][v] < minDist[v]:
                    minDist[v] = minDist[cur] + grid[cur][v]
        ans=max(minDist[1:])
        return -1 if ans==float('inf') else ans