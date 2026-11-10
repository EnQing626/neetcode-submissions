class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m=len(heights)
        n=len(heights[0])
        a_visited=[[False]*n for _ in range(m)]
        p_visited=[[False]*n for _ in range(m)]
        dirs=[(-1, 0), (0, 1), (1, 0), (0, -1)]  # 四个方向
        result=[]
        def dfs(visited,x,y):
            for dir in dirs:
                nextx=x+dir[0]
                nexty=y+dir[1]
                if nextx<0 or nexty<0 or nextx>=m or nexty>=n:
                    continue
                if not visited[nextx][nexty] and heights[nextx][nexty]>=heights[x][y]:
                    visited[nextx][nexty]=True
                    dfs(visited,nextx,nexty)
        for i in range(m):
            p_visited[i][0]=True
            dfs(p_visited,i,0)
            a_visited[i][n-1]=True
            dfs(a_visited,i,n-1)
        for j in range(n):
            p_visited[0][j] = True
            dfs(p_visited,0,j)
            a_visited[m-1][j] = True
            dfs(a_visited,m-1,j)
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result