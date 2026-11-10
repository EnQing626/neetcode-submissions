class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row=len(obstacleGrid)
        col=len(obstacleGrid[0])
        dp=[[0]*col for _ in range(row)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0  # 如果第一个格子就是障碍，return 0
        #initial row
        for i in range(1,col):
            if obstacleGrid[0][i]!=1:
                dp[0][i]=dp[0][i-1]
        #initial col
        for i in range(1,row):
            if obstacleGrid[i][0]!=1:
                dp[i][0]=dp[i-1][0]

        for i in range(1,row):
            for j in range(1,col):
                if obstacleGrid[i][j]!=1:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]