class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==0:
            return 0
        dp=[[0]*4 for _ in range(n)]
        dp[0][0]=-prices[0]
        for i in range(1,n):
            #持有股票
            dp[i][0]=max(dp[i-1][0],max(dp[i-1][1],dp[i-1][3])-prices[i])
            #持有钱，一直持有钱or冷冻期后一天
            dp[i][1]=max(dp[i-1][1],dp[i-1][3])
            #持有钱，刚卖股票
            dp[i][2]=dp[i][0]+prices[i]
            #冷冻期
            dp[i][3]=dp[i-1][2]
        return max(dp[-1][0],dp[-1][1],dp[-1][2],dp[-1][3])