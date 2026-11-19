class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        res=0
        count=0
        used=[[False]*n for _ in range(m)]
        dirs=[(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(x,y):
            nonlocal count
            count+=1
            for dir in dirs:
                next_x=x+dir[0]
                next_y=y+dir[1]
                if next_x>=0 and next_x<m and next_y>=0 and next_y<n and used[next_x][next_y]==False and grid[next_x][next_y]==1:
                    used[next_x][next_y]=True
                    dfs(next_x,next_y)
        for i in range(m):
            for j in range(n):
                if not used[i][j] and grid[i][j]==1:
                    used[i][j]=True
                    count=0
                    dfs(i,j)
                    res=max(res,count)
        return res