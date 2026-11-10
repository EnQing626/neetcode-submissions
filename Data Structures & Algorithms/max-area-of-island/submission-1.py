class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False]*n for _ in range(m)]
        dirs=[(-1, 0), (0, 1), (1, 0), (0, -1)]  # 四个方向
        count=0
        result=0

        def dfs(x,y):
            nonlocal count
            count+=1
            for dir in dirs:
                nextx=x+dir[0]
                nexty=y+dir[1]
                if nextx<0 or nextx>=m or nexty<0 or nexty>=n:
                    continue
                if not visited[nextx][nexty] and grid[nextx][nexty]==1:
                    visited[nextx][nexty]=True
                    #count+=1
                    dfs(nextx,nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]==1:
                    visited[i][j]=True
                    count=0
                    dfs(i,j)
                    result=max(result,count)
        return result