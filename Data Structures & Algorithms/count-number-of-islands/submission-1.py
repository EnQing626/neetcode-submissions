class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        visited=[[False]*n for _ in range(m)]
        result=0
        def dfs(i,j):
            for dir in dirs:
                nextx=i+dir[0]
                nexty=j+dir[1]
                if nextx<0 or nextx>=m or nexty<0 or nexty>=n:
                    continue
                if not visited[nextx][nexty] and grid[nextx][nexty]=='1':
                    visited[nextx][nexty]=True
                    dfs(nextx,nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':
                    visited[i][j]=True
                    result+=1
                    dfs(i,j)
        return result