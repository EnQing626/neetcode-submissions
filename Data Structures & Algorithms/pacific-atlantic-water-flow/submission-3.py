class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        used_pacific=[[False]*n for _ in range(m)]
        used_atlantic=[[False]*n for _ in range(m)]
        dirs=[(-1, 0), (0, 1), (1, 0), (0, -1)]  # 四个方向
        result=[]
        def dfs(i,j,used):
            for dir in dirs:
                next_i=i+dir[0]
                next_j=j+dir[1]
                if next_i<0 or next_i>=m or next_j<0 or next_j>=n:
                    continue
                if not used[next_i][next_j] and heights[i][j]<=heights[next_i][next_j]:
                    used[next_i][next_j]=True
                    dfs(next_i,next_j,used)
        for i in range(m):
            used_pacific[i][0]=True
            dfs(i,0,used_pacific)
            used_atlantic[i][n-1]=True
            dfs(i,n-1,used_atlantic)
        for j in range(n):
            used_pacific[0][j]=True
            dfs(0,j,used_pacific)
            used_atlantic[m-1][j]=True
            dfs(m-1,j,used_atlantic)
        
        for i in range(m):
            for j in range(n):
                if used_pacific[i][j] and used_atlantic[i][j]:
                    result.append([i,j])
        return result
