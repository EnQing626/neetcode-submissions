class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(heights), len(heights[0])
        dis = [[math.inf] * n for _ in range(m)]
        # (dis, i, j)
        h = [(0, 0, 0)]
        while h:
            d, i, j = heapq.heappop(h)
            if d > dis[i][j]:
                continue
            if i == m - 1 and j == n - 1:
                return d
            for di, dj in DIRS:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n:
                    new_dis = max(d, abs(heights[x][y] - heights[i][j]))
                    if new_dis < dis[x][y]:
                        dis[x][y] = new_dis
                        heapq.heappush(h, (new_dis, x, y))
        return -1