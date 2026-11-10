class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        result=0
        sum_land = 0  # 陆地数量
        cover = 0  # 相邻数量
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    sum_land+=1
                    if i-1>=0 and grid[i-1][j]==1:
                        cover+=1
                    if j-1>=0 and grid[i][j-1]==1:
                        cover+=1
        result=4*sum_land-2*cover
        return result