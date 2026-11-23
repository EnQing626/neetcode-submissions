class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        used=[[False]*n for _ in range(m)]
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        res=0
        def dfs(x,y):
            for dir in dirs:
                next_x=dir[0]+x
                next_y=dir[1]+y
                if next_x<0 or next_x>=m or next_y<0 or next_y>=n:
                    continue
                if not used[next_x][next_y] and grid[next_x][next_y]=="1":
                    used[next_x][next_y]=True
                    dfs(next_x,next_y)

        for i in range(m):
            for j in range(n):
                if not used[i][j] and grid[i][j]=="1":
                    # if i==0 and j==1:
                    #     print("i:"+str(i))
                    #     print("j:"+str(j))
                    #     print("Before dfs:"+str(used))
                    res+=1
                    used[i][j]=True
                    dfs(i,j)
                    # if i==0 and j==1:
                    #     print("After dfs:"+str(used))
        return res